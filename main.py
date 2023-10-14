import discord
from discord import app_commands
from discord.ext import commands

id_do_servidor =  #Coloque aqui o ID do seu servidor
id_cargo_atendente =  #Coloque aqui o ID do cargo de atendente
token_bot = "" #Coloque aqui seu Token do BOT | OBS: Não compartilhe em hipótese alguma o Token

class Dropdown(discord.ui.Select):
    def __init__(self):
        options = [
        discord.SelectOption(value="duvidas",label="Dúvidas", emoji="🤔"),
        discord.SelectOption(value="denuncias",label="Denúncias", emoji="📢"), 
        discord.SelectOption(value="punicoes",label="Punições", emoji="👨‍⚖️"),
        discord.SelectOption(value="sugestoes",label="Sugestões", emoji="🗳️"),
        discord.SelectOption(value="bugs",label="Reportar-Bug's", emoji="🙅"),
        discord.SelectOption(value="atendimento",label="Atendimento-Geral", emoji="🆘"),
        discord.SelectOption(value="assistencias",label="Assistências", emoji="👍"),
        discord.SelectOption(value="reclamacao",label="Reclamações", emoji="🤬"),
        discord.SelectOption(value="avaliacao",label="Avaliações", emoji="⭐"),
        discord.SelectOption(value="falta",label="Não achou sua opção? Use essa!", emoji="🥺"),
        ]
        super().__init__(
            placeholder="Selecione uma opção...",
            min_values=1,
            max_values=1,
            options=options,
            custom_id="persistent_view:dropdown_help"
        )
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "duvidas":
            await interaction.response.send_message(":ATENCAO:  **|** *Para tirar dúvidas gerais sobre nossa comunidade ou nossos bot's próprios ou não, use esse ticket e nos envie todos os dados necessários para uma análise detalhada como:*\n\n**-> Nome do seu servidor,Nome do bot em questão, Print do erro e/ou dúvida geral como[comandos de prefixo,tipo de bot,comandos em geral e etc](EM CASO DE NOSSOS BOT'S PRÓPRIOS);**\n\n**-> Em caso de outros bot's como: Loritta e afins e/ou canais ou demais dúvidas infome todos os dados pertinentes para que nossas equipes possam agilizar seu atendiemnto.**",ephemeral=True,view=CreateTicket())
        elif self.values[0] == "denuncias":
              await interaction.response.send_message("⚠️ **|** *Para fazer uma denúncia, vamos precisar do motivo da denúncia, autores do ocorrido e provas/prints.*\n\n**-> Não crie um ticket de denúncia apenas para testar a ferramenta ou para tirar dúvidas (existem outros espaços para isso!).**\n\n**-> Se quiser prosseguir com sua denúncia, crie um atendimento abaixo.**",ephemeral=True,view=CreateTicket())  
        elif self.values[0] == "punicoes":
              await interaction.response.send_message("⚠️ **|** *Para apelar ou revisar qualquer caso de punição, use  esse ticket para nos informar e mande print e o cargo e nome/nick do responsável de nossas equipes por lhe aplicar a mesma para uma revisão de seus superiores.*\n\n**->NOTA: Em caso de falha na apelação lhe será dito por esse ticket, então fique atento(a).**",ephemeral=True,view=CreateTicket())
        elif self.values[0] == "sugestoes":
              await interaction.response.send_message("⚠️ **|** *Para mandar uma ou mais sugestões as nossas equipes, use esse ticket e mande print(se achar necessário).*",ephemeral=True,view=CreateTicket())
        elif self.values[0] == "bugs":
              await interaction.response.send_message("⚠️ **|** *Para reportar um ou mais Bug's de nossa comunidade, porém, atente-se as instruções:*\n\n**->NOTA: Envie o máximo de detalhes sobre ele incluindo (descrição e fotos).**\n\n*Havendo isso em mãos, crie um ticket abaixo e faça o seu envio.*",ephemeral=True,view=CreateTicket())                
        elif self.values[0] == "atendimento":
              await interaction.response.send_message("⚠️ **|** *Para solicitar um atendimento geral, por problemas como(loja interativa,convites e etc), as nossas equipes use esse ticket .*",ephemeral=True,view=CreateTicket()) 
        elif self.values[0] == "assistencias":
              await interaction.response.send_message("⚠️ **|** *Para solicitar um assistencia exclusiva(deve possuir o cargo vip-elite), para qualquer problema ultilize esse ticket para ser atentido(a) de forma rápida e eficaz.*",ephemeral=True,view=CreateTicket())
        elif self.values[0] == "reclamacao":
              await interaction.response.send_message("⚠️ **|** *Se deseja fazer uma reclamação por algum resultado de nossas equipes ao qual discorde ou para reclamar de outros assuntos, use esse ticket; Más lembre-se, deve fornecer o maior numero de detalhes para uma averiguação mais rápida e precisa de sua reclamação. Contamos com vocês!",ephemeral=True,view=CreateTicket())
        elif self.values[0] == "avaliacao":
              await interaction.response.send_message("⚠️ **|** *Se Você quiser avaliar nossas equipes e atribuir notas a um de nossos colaboradores, abra seu ticket e informe as seguintes informações:*\n\n **-> NICK/MENÇÃO DO USUÁRIO, MOTIVO,GRAU DE SATISFAÇÃO(ENTRE: 1 E 5 ⭐), SE O PROBLEMA,DÚVIDAS E/OU AFINS FOI OU NÃO RESOLVIDO.**",ephemeral=True,view=CreateTicket())
        elif self.values[0] == "falta":
              await interaction.response.send_message("⚠️ **|** *NÃO use essa aba para tirar dúvidas de: BOT'S PRÓPRIOS, fazer reclamações e/ou afins.*\n\n**-> NOTA:Existem abas comunitárias acima para te ajudar! Use-as com carinho e paciência.\n\n Se você tiver alguma questão extraordinária que APENAS um membro de nossas equipes puder lhe auxiliar, clique abaixo para criar um ticket!**",ephemeral=True,view=CreateTicket())  


class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        self.add_item(Dropdown())

class CreateTicket(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=300)
        self.value=None

    async def is_user_atendendo(self, member):
        for role in member.roles:
              if role.id in id_cargo_atendente:
                   for channel in member.guild.text_channels:
                        if channel.type == discord.ChannelType.private_thread and channel.archived is False:
                            if channel.name.startswith(f"{member.name}"):
                                return True
                                return False
  
    @discord.ui.button(label="SUPPORT!",style=discord.ButtonStyle.green,emoji="➕")
    async def confirm(self,interaction: discord.Interaction, button: discord.ui.Button):
        self.value = True
        self.stop()
      

        ticket = None
        for thread in interaction.channel.threads:
            if f"{interaction.user.id}" in thread.name:
                if thread.archived:
                    ticket = thread
                else:
                    await interaction.response.send_message(ephemeral=True,content=f"Você já tem um atendimento em andamento!")
                    return

        async for thread in interaction.channel.archived_threads(private=True):
                  if f"{interaction.user.id}" in thread.name:
                      if thread.archived:
                          ticket = thread
                      else:
                          await interaction.edit_original_response(content=f"Você já tem um atendimento em andamento!",view=None)
                          return
        
        if ticket != None:
            await ticket.edit(archived=False,locked=False)
            await ticket.edit(name=f"{interaction.user.name} ({interaction.user.id})",auto_archive_duration=10080,invitable=False)
        else:
            ticket = await interaction.channel.create_thread(name=f"{interaction.user.name} ({interaction.user.id})",auto_archive_duration=10080)#,type=discord.ChannelType.public_thread)
            await ticket.edit(invitable=False)

        await interaction.response.send_message(ephemeral=True,content=f"Criei um ticket para você! {ticket.mention}")
        await ticket.send(f"📩 **|** {interaction.user.mention} **Ticket criado!**\n\n*-> Envie todas as informações possíveis sobre seu caso e aguarde até que um atendente responda.*\n\nApós a sua questão ser sanada, você pode usar: `/encerrar` , para encerrar o atendimento!\n\n-> Equipes responsáveis por te atender em suas necessidades:\n\n***📌  ┃ GERENTE, 🛠️ ┃ ADMINISTRADOR, 🔮 ┃ LÍDER DE EQUIPE, ⚔️ ┃ MODERADOR, 🛡️ ┃ SUPORTE, 🦥 ┃ ESTAGIÁRIO***") 

class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False #Nós usamos isso para o bot não sincronizar os comandos mais de uma vez

    async def setup_hook(self) -> None:
        self.add_view(DropdownView())

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #Checar se os comandos slash foram sincronizados 
            await tree.sync(guild = discord.Object(id=id_do_servidor)) # Você também pode deixar o id do servidor em branco para aplicar em todos servidores, mas isso fará com que demore de 1~24 horas para funcionar.
            self.synced = True
        print(f"Entramos como: {self.user}.") 

aclient = client()

tree = app_commands.CommandTree(aclient)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'setup', description='Setup')
@commands.has_permissions(manage_guild=True)
async def setup(interaction: discord.Interaction):
    #dropdown_view = DropdownView()  # Crie uma instância de DropdownView
    #await interaction.response.send_message("Mensagem do painel",view=DropdownView()) 
    
    embed = discord.Embed(
        colour=discord.Color.blurple(),
        title="🔔Central de ajuda da Comunidade!🔔",
        description="***• Nessa seção, você pode entrar em contato com a nossa equipe da comunidade!***"
    )
    embed.set_image(url="https://cdn.dribbble.com/users/31818/screenshots/1909960/ticket_2color.gif")

    await interaction.channel.send(embed=embed,view=DropdownView())

@tree.command(guild = discord.Object(id=id_do_servidor), name="encerrar",description='Feche o suporte atual.')
async def _encerrar(interaction: discord.Interaction):
    mod = interaction.guild.get_role(id_cargo_atendente)
    if str(interaction.user.id) in interaction.channel.name or mod in interaction.author.roles:
        await interaction.response.send_message(f"O ticket foi arquivado por: {interaction.user.mention}, obrigado por entrar em contato!")
        await interaction.channel.edit(archived=True,locked=True)
    else:
        await interaction.response.send_message("Isso não pode ser feito aqui...")

aclient.run(token_bot)
