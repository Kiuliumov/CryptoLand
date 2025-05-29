from client import client
from discord.ext import commands
import os


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client.user.name))

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

bot.run("YOUR_BOT_TOKEN")