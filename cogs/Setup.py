import discord
from discord.ext import commands


class server_setup(commands.Cog):
    """
    `A Server setup commands, to make the bot ready for your server!`
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setup(self):
        """
        The setup commands
        """
        pass

def setup(bot):
    bot.add_cog(server_setup(bot))
