import discord
from discord.ext import commands

class Toggle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def toggle(self, extension):
        pass


def setup(bot):
    bot.add_cog(Toggle(bot))
