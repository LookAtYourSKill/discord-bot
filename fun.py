import discord
from discord.ext import commands


class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def idk(self):
        pass


def setup(bot):
    bot.add_cog(fun())
