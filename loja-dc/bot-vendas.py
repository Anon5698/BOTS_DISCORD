from dotenv import load_dotenv
import disnake
from disnake.ext import commands
import mercadopago
import random
import string
import os
from env import ACCESS_TOKEN, ADMIN_CHANNEL_ID, PUBLIC_CHANNEL_ID, TOKEN_BOT

load_dotenv()

intents = disnake.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='', intents=intents)

# Agora você pode acessar a variável ACCESS_TOKEN
access_token = os.getenv("ACCESS_TOKEN")
mp = mercadopago.SDK(ACCESS_TOKEN)

# Dicionário para armazenar os produtos e suas mensagens
products = {}

def generate_unique_key(length=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def create_payment_preference(item_name, item_price):
    preference_data = {
        "items": [
            {
                "title": item_name,
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": float(item_price)
            }
        ]
    }
    preference = mp.preference().create(preference_data)
    return preference['response']['init_point']

@bot.slash_command(name="criarproduto", description="Cria um novo produto")
@commands.has_permissions(administrator=True)
async def criar_produto(ctx, nome: str, preco: float, url_imagem: str = None):
    if ctx.channel.id != ADMIN_CHANNEL_ID:
        await ctx.send("Este comando só pode ser usado no canal de administração!")
        return

    payment_url = create_payment_preference(nome, preco)
    embed_description = f"Preço: R${preco}"
    embed = disnake.Embed(title=nome, description=embed_description, color=0x00ff00)
    if url_imagem:
        embed.set_image(url=url_imagem)

    button = disnake.ui.Button(style=disnake.ButtonStyle.url, label="Comprar agora", url=payment_url)

    public_channel = bot.get_channel(PUBLIC_CHANNEL_ID)
    message = await public_channel.send(embed=embed, components=[disnake.ui.ActionRow(button)])

    product_key = generate_unique_key()
    products[product_key] = message.id
    await ctx.send(f"Produto criado com sucesso! A chave única para este produto é `{product_key}`.")

@bot.slash_command(name="editarproduto", description="Edita um produto existente")
@commands.has_permissions(administrator=True)
async def editar_produto(ctx, chave: str, nome: str = None, preco: float = None, url_imagem: str = None):
    if ctx.channel.id != ADMIN_CHANNEL_ID:
        await ctx.send("Este comando só pode ser usado no canal de administração!")
        return

    if chave not in products:
        await ctx.send("Chave de produto inválida.")
        return

    public_channel = bot.get_channel(PUBLIC_CHANNEL_ID)
    message_id = products[chave]
    message = await public_channel.fetch_message(message_id)
    embed = message.embeds[0]

    if nome:
        embed.title = nome
    if preco:
        payment_url = create_payment_preference(nome or embed.title, preco)
        embed.description = f"Preço: R${preco}"
    if url_imagem:
        embed.set_image(url=url_imagem)

    if preco or nome:
        payment_url = create_payment_preference(nome or embed.title, float(embed.description.split('R$')[1]))

    button = disnake.ui.Button(style=disnake.ButtonStyle.url, label="Comprar agora", url=payment_url)

    await message.edit(embed=embed, components=[disnake.ui.ActionRow(button)])

bot.run(TOKEN_BOT)
