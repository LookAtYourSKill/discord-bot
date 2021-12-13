import discord
from discord.ext import commands


class server_setup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setup(self):
        pass

def setup(bot):
    bot.add_cog(server_setup(bot))
