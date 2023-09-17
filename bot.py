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
    await member.send('junte-se tambem a cosmic: https://discord.gg/39bC3rKmGH')

@bot.event
async def on_message(message):
    if not message.author.bot:
        if any(link in message.content.lower() for link in ['https://discord.gg/','https://discord.com/', 'http://discord.com/', 'www.discord.com/','discord.gg/','http://discord.gg/']):
            await message.delete()
            nolin = await message.channel.send(f'{message.author.mention}, não é permitido enviar links neste servidor.')
            await asyncio.sleep(5)
            await nolin.delete()

    await bot.process_commands(message)

@bot.event
async def on_ready():
    print('logado com sucesso!')
    
@bot.command()
@commands.check(has_high_roles)
async def mute(ctx,member: discord.Member, *,motivo=None):
    logchan = bot.get_channel(1152472986679517265)
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
    logchan = bot.get_channel(1152472986679517265)
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
    logchan = bot.get_channel(1152473027372662784)
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
    logchan = bot.get_channel(1152473027372662784)
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
    msg = await ctx.send(embed=embed)
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

bot.run('MTE1MTk3ODc3NTQ5MjQ0ODI1Ng.GKNjns.lPbJUUw-H5hdWHlji2lEIBPGFiRyRn0PiKb7kQ')
