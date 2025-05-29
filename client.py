import discord
from discord.ext import commands


client: commands.Bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())



