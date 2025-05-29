from client import client
from dotenv import load_dotenv
import os



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client.user.name))

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


load_dotenv()
token: str = os.getenv("TOKEN")

client.run(token)