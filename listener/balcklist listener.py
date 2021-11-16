import discord
from discord.ext import commands
import json


class blacklistListener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        with open("./utils/json/blacklist.json", 'r') as f:
            data = json.load(f)
        for bad_word in data["blacklist"]:
            if bad_word in message.content.lower():
                await message.delete()
                embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                      description='Deine Message `wurde gelöscht`, da du ein Wort `aus der Blacklist darin hattest!`\n**Bitte unterlasse dies!**')
                await message.channel.send(embed=embed, delete_after=5)


def setup(bot):
    bot.add_cog(blacklistListener(bot))
