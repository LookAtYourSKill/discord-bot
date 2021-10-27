import discord
from discord.ext import commands


class linkBlocker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        invLink = ['http://, https://']

        for synonym in invLink:
            if synonym in message.content.lower():
                await message.delete()
                embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                      description='Hier sind **keine Links erlaubt**!')
                await message.channel.send(embed=embed, delete_after=5)

def setup(bot):
    bot.add_cog(linkBlocker(bot))

