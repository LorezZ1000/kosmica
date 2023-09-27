import discord
import asyncio
from easy_pil import Editor, load_image_async, Font
from discord.ext import commands 
from discord import File

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='cc!',intents=intents)

cosmicpc = 'https://cdn.discordapp.com/attachments/1151996468689895546/1152046711431254147/kosmica.gif'
waring = 'https://cdn.discordapp.com/attachments/1151996468689895546/1152047538837409864/kosmicas.gif'

def has_high_role(ctx):
    required_role_name = "Nuke"
    role = discord.utils.get(ctx.guild.roles, name=required_role_name)
    print(f"User's roles: {[role.name for role in ctx.author.roles]}")
    if role in ctx.author.roles:
        return True
    return False

def has_high_roles(ctx):
    required_role_name = "Nuke"
    required_role_name2 = "My melody"
    required_role_name3 = "Ajudante"
    role = discord.utils.get(ctx.guild.roles, name=required_role_name)
    role2 = discord.utils.get(ctx.guild.roles, name=required_role_name2)
    role3 = discord.utils.get(ctx.guild.roles, name=required_role_name3)
    print(f"User's roles: {[role.name for role in ctx.author.roles]}")
    if role in ctx.author.roles or role2 in ctx.author.roles or role3 in ctx.author.roles:
        return True
    return False

@bot.event
async def on_member_join(member):
    
    channel = bot.get_channel(1151979648566186074)
    pfp = member.avatar.url
    background = Editor("pic1.jpg")
    profile_image = await load_image_async(str(pfp))
    profile = Editor(profile_image).resize((150,150)).circle_image()
    poppins = Font.poppins(size=50,variant='bold')
    
    poppins_small = Font.poppins(size=20,variant='light')
    
    background.paste(profile, (325,90))
    background.ellipse((325,90),150,150,outline='white',stroke_width=5)
    
    background.text((400,260), 'BEM VINDO A KOSMICA',color='white',font=poppins,align='center')
    background.text((400,325), f'{member.name}#{member.discriminator}',color='white',font=poppins_small,align='center')
    
    file = File(fp=background.image_bytes,filename="pic1.jpg")
    await channel.send(f'{member.mention} *bem vindo a Kosmica & Nanno*')
    await channel.send(file=file)
    
    role = discord.utils.get(member.guild.roles, name='RANDOM')
    await member.add_roles(role)
    await member.send('Bem vindo a kosmica!')
    await member.send('junte-se tambem a cosmic: https://discord.gg/39bC3rK')

@bot.event
async def on_message(message):
    if not message.author.bot:
        if any(link in message.content.lower() for link in ['https://discord.gg/','https://discord.com/', 'http://discord.com/', 'www.discord.com/','discord.gg/','http://discord.gg/']):
            logchan = bot.get_channel(1155619044611854366)
            role = discord.utils.get(message.author.guild.roles, name='Mute')
            await message.author.add_roles(role)
            await message.delete()
            nolin = await message.channel.send(f'{message.author.mention}, <:emoji_40:1154541387958722581> Você não pode se divulgar aqui bobão >:(')
            embed = discord.Embed(title='mensagem apagada!',color=discord.Color.red())
            embed.set_author(name='',icon_url=waring)
            embed.set_thumbnail(url=message.author.avatar.url)
            embed.add_field(name='autor:', value=f'{message.author.name}', inline=False)
            embed.add_field(name='mensagem:', value=f'> {message.content}',inline=False)
            await logchan.send(embed=embed)
            await asyncio.sleep(5)
            await message.author.remove_roles(role)
            await nolin.delete()

    await bot.process_commands(message)

@bot.event
async def on_ready():
    print('logado com sucesso!')

@bot.command()
@commands.check(has_high_roles)
async def mute(ctx,member: discord.Member, *,motivo=None):
    logchan = bot.get_channel(1154432782844579841)
    if motivo is None:
        motivo = "📝 Sem motivo!"
    muted_role = discord.utils.get(ctx.guild.roles, name='Mute')
    await member.add_roles(muted_role)
    embed = discord.Embed(title=f'{member.name} foi Mutado')
    embed.set_author(name="Kosmica mute", icon_url=waring)
    embed.set_thumbnail(url=cosmicpc)
    embed.add_field(name='Autor do mute :',value=f'{ctx.author.name}',inline=False)
    embed.add_field(name='motivo:',value=f'{motivo}',inline=False)
    embed.set_footer(text="Kosmica/Nanno ©")
    msg = await ctx.send(embed=embed)
    msg2 = await logchan.send(embed=embed)
    await ctx.message.delete()
    await asyncio.sleep(15)
    await msg.delete()

@bot.command()
@commands.check(has_high_roles)
async def unmute(ctx,member: discord.Member):
    logchan = bot.get_channel(1154432782844579841)
    muted_role = discord.utils.get(ctx.guild.roles, name='Mute')
    await member.remove_roles(muted_role)
    embed = discord.Embed(title=f'{member.name} foi Desmutado')
    embed.set_author(name="Kosmica unmute", icon_url=waring)
    embed.set_thumbnail(url=cosmicpc)
    embed.add_field(name='Autor do unmute :',value=f'{ctx.author.name}',inline=False)
    embed.add_field(name='Obs:',value=f'se fizer merda toma dnv',inline=False)
    embed.set_footer(text="Kosmica/Nanno ©")
    msg = await ctx.send(embed=embed)
    msg2 = await logchan.send(embed=embed)
    await ctx.message.delete()
    await asyncio.sleep(15)
    await msg.delete()

@bot.command()
@commands.check(has_high_role)
async def ban(ctx,member: discord.Member,*,motivo=None):
    logchan = bot.get_channel(1154432840679825539)
    if motivo is None:
        motivo = "📝 Sem motivo!"
    await member.ban(reason=motivo)
    embed = discord.Embed(title=f'{member.name} foi Banido!')
    embed.set_author(name="Kosmica ban", icon_url=waring)
    embed.set_thumbnail(url=cosmicpc)
    embed.add_field(name='Autor do ban:',value=f'{ctx.author.name}',inline=False)
    embed.add_field(name='Motivo:',value=f'{motivo}',inline=False)
    embed.set_footer(text="Kosmica/Nanno ©")
    msg = await ctx.send(embed=embed)
    msg2 = await logchan.send(embed=embed)
    await ctx.message.delete()
    await asyncio.sleep(15)
    await msg.delete()

@bot.command()
@commands.check(has_high_role)
async def unban(ctx, id: int):
    logchan = bot.get_channel(1154432840679825539)
    user = await bot.fetch_user(id)
    await ctx.guild.unban(user)
    embed = discord.Embed(title=f'{user.name} foi Desbanido!')
    embed.set_author(name="Kosmica unban", icon_url=cosmicpc)
    embed.set_thumbnail(url=cosmicpc)
    embed.add_field(name='Autor do unban:',value=f'{ctx.author.name}',inline=False)
    embed.set_footer(text="Kosmica/Nanno ©")
    msg = await ctx.send(embed=embed)
    msg2 = await logchan.send(embed=embed)
    await ctx.message.delete()
    await asyncio.sleep(15)
    await msg.delete()



@bot.command()
@commands.check(has_high_role)
async def nuke(ctx):
    channel = ctx.channel
    channel_position = channel.position
    messages = []
    async for message in channel.history(limit=None):
        if len(messages) == 100:
            await channel.delete_messages(messages)
    if messages:
        await channel.delete.messages(messages)

    channel_name = channel.name

    channel_category = channel.category

    await channel.delete()

    new_channel = await ctx.guild.create_text_channel(name=channel_name, category=channel_category)

    autordosatos = ctx.author.name

    await new_channel.send(f"nuked by {autordosatos}")

    await new_channel.edit(position=channel_position, category=channel_category, reason="nuke")

@bot.command()
@commands.check(has_high_roles)
async def lock(ctx):
    if ctx.author.guild_permissions.manage_channels:
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)

        embed = discord.Embed(title=f'{ctx.author.name} Trancou o server!')
        embed.set_author(name="Kosmica lock", icon_url=waring)
        embed.set_thumbnail(url=cosmicpc)
        embed.add_field(name='Aviso:',value=f'esse chat foi trancado!',inline=False)
        embed.set_footer(text="Kosmica/Nanno ©")
        msg = await ctx.send(embed=embed)
        await ctx.message.delete()
        await asyncio.sleep(15)
        await msg.delete()

@bot.command()
@commands.check(has_high_roles)
async def unlock(ctx):
    if ctx.author.guild_permissions.manage_channels:
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        embed = discord.Embed(title=f'{ctx.author.name} Destrancou o server!')
        embed.set_author(name="Kosmica lock", icon_url=waring)
        embed.set_thumbnail(url=cosmicpc)
        embed.add_field(name='Aviso:',value=f'esse chat foi destrancado!',inline=False)
        embed.set_footer(text="Kosmica/Nanno ©")
        msg = await ctx.send(embed=embed)
        await ctx.message.delete()
        await asyncio.sleep(15)
        await msg.delete()

@bot.command()
async def avatar(ctx,member: discord.Member=None):
    if member is None:
        member = ctx.author
    avatar = member.avatar.url
    embed = discord.Embed(title=f'Avatar de {member.name}')
    embed.set_author(name="Kosmica avatar", icon_url=cosmicpc)
    embed.set_image(url=avatar)
    embed.set_footer(text=f"Kosmica/Nanno ©")
    buttonl = Button(label='url do avatar',url=avatar)
    view = View()
    view.add_item(buttonl)
    msg = await ctx.send(embed=embed,view=view)
    await ctx.message.delete()
    await asyncio.sleep(15)
    await msg.delete()

@bot.command()
@commands.check(has_high_role)
async def setrole(ctx,member: discord.Member,role: discord.Role):
    await member.add_roles(role)
    embed = discord.Embed(title=f'Você setou cargo em {member.name}')
    embed.set_author(name="Kosmica setrole", icon_url=cosmicpc)
    embed.set_thumbnail(url=cosmicpc)
    embed.add_field(name='Cargo:',value=f'{role.name}',inline=False)
    embed.set_footer(text=f"Kosmica/Nanno ©")
    msg = await ctx.send(embed=embed)
    await ctx.message.delete()
    await asyncio.sleep(15)
    await msg.delete()

@bot.command()
@commands.check(has_high_role)
async def remove(ctx,member: discord.Member,role: discord.Role):
    await member.remove_roles(role)
    embed = discord.Embed(title=f'Você tirou cargo de {member.name}')
    embed.set_author(name="Kosmica remove", icon_url=cosmicpc)
    embed.set_thumbnail(url=cosmicpc)
    embed.add_field(name='Cargo:',value=f'{role.name}',inline=False)
    embed.set_footer(text=f"Kosmica/Nanno ©")
    msg = await ctx.send(embed=embed)
    await ctx.message.delete()
    await asyncio.sleep(15)
    await msg.delete()

@bot.command()
async def beijar(ctx,member: discord.Member=None):
    autor = ctx.author
    if member is None:
        beijado = ctx.author.name
    else:
        beijado = member.name
    embed = discord.Embed(title=f'{ctx.author.name} beijou {beijado}')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1154418661428318259/1156074933340868678/bv8.gif?ex=6513a62e&is=651254ae&hm=2e1019e7982dbfb3ea1dd8fe43bea51c2aa8ec69de7148660240bbbb39c08b9b&')
    retr = Button(label='retribuir',custom_id='beijarbtn')
    async def callback(interaction: discord.Interaction):
        if interaction.user.name != beijado:
            await interaction.response.send_message('esse beijo não foi para você',ephemeral=True)
        else:
            embed = discord.Embed(title=f'{beijado} retribuiu beijo de {autor}')
            embed.set_image(url='https://cdn.discordapp.com/attachments/1154418661428318259/1156074933340868678/bv8.gif?ex=6513a62e&is=651254ae&hm=2e1019e7982dbfb3ea1dd8fe43bea51c2aa8ec69de7148660240bbbb39c08b9b&')
        await interaction.response.send_message(embed=embed)
        msg = autor.channel.send('ola')
        await asyncio.sleep(9)
        await msg.delete()

    retr.callback = callback
    view = View()
    view.add_item(retr)
    msg = await ctx.send(embed=embed,view=view)
    await ctx.message.delete()
    await asyncio.sleep(15)
    await msg.delete()

@bot.command()
async def menu_test(ctx):
    embed = discord.Embed(title='Abrir ticket')
    embed.add_field(name='algumas opções abaixo',value='', inline=False)
    embed.add_field(name='Suporte',value='> abre um ticket de ajuda para suporte',inline=False)
    embed.add_field(name='Ser staff',value='> envia formulario para a staff',inline=False)
    embed.set_image(url='https://cdn.discordapp.com/attachments/1154418661428318259/1156244954381824112/20230926_1203131.gif?ex=65144487&is=6512f307&hm=98e525d0414305f0b4c0031bc2d43563296798ef527884fb383fdcb8396a287f&')
    select = Select(
        placeholder='abrir ticket',
        options=[
         discord.SelectOption(label='Suporte',value='0x11'),
         discord.SelectOption(label='Ser staff',value="gayz")
    ]
)
    async def my_callback(interaction):
        if select.values[0] == "0x11":
            guild = interaction.guild
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                interaction.user: discord.PermissionOverwrite(read_messages=True),
                guild.get_role(1154431601141350410): discord.PermissionOverwrite(read_messages=True)
            }
            channel = await guild.create_text_channel("ticket-suporte", overwrites=overwrites)
            await interaction.response.send_message('seu ticket foi criado! te marcamos lá',ephemeral=True)
            fechar = Button(label='fechar ticket', style=discord.ButtonStyle.red)
            async def fecharbt(interaction):
                await channel.delete()
            view2 = View()
            view2.add_item(fechar)
            channel.send(view=view2)
            fechar.callback = fecharbt
            await channel.send(f'<@&1154431601141350410> {interaction.user.mention} *ticket aberto*',view=view2)
    select.callback = my_callback
    view = View()
    view.add_item(select)
    await ctx.send(embed=embed,view=view)

bot.run('')
