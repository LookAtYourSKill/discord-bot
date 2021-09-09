import discord
from discord.ext import commands

class on_guild(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self):
        pass

    @commands.Cog.listener()
    async def on_guild_remove(self):
        pass