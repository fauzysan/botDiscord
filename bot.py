import discord

client = discord.Client()

client.commands = command.discord(set_prefix = '*')

@client.event
async def on_ready()
    print('We Have logged as {0.user}.format (client))

@client.event
async def on_message(message)
    if message.author == client.user:
        return
    if message.content.startwith('$hello')
        await message.channel.send('hello juga')


client.run("NzgzMzgwMDk2MTYxMTUzMDI0.X8Z5kQ.n0VeiY6PZGeUiHC3FBDLmH_hQF0")