import discord
import random
from discord.ext import commands

client = discord.Client()

client = commands.Bot(command_prefix = '.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Your ping is {round(client.latency * 100)}ms')


@client.command()
async def play(ctx, *, pill):
    res = [
        "gunting",
        "batu",
        "kertas"]
    await ctx.send(f'Anda: {pill}\n Bot: {random.choice(res)}')
@client.event
async def on_ready():
    print('We are have logged as {0.user}'.format(client))



@client.event
async def Member_Guild_join(message):
    await message.channel.send('Member has joined')

client.run('NzgzMzgwMDk2MTYxMTUzMDI0.X8Z5kQ.n0VeiY6PZGeUiHC3FBDLmH_hQF0')