import discord
from discord.app_commands import commands


class ServerSetup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        embed = discord.Embed(
            title="👋 Thanks for adding CryptoWonder!",
            description="Welcome to **CryptoWonder**!\n\n"
                        "🔧 Use `/setup` to configure the bot.\n"
                        "📊 Use `/track` to monitor crypto prices.\n"
                        "📊 Use `/search` to search for a currency.\n"
                        "🛟 Need help? Join our [support server](https://discord.gg/yourserver).",
            color=discord.Color.blue()
        )
        embed.set_footer(text="CryptoLand Bot • Web3 Meets Discord")
        embed.set_thumbnail(url="https://your-image-link.com/logo.png")

        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                await channel.send(embed=embed)
                break

def setup(bot):
    bot.add_cog(ServerSetup(bot))
