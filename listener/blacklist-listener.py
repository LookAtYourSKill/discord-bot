import discord
from discord.ext import commands
import json


class blacklistListener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        with open("utils/json/blacklist.json", 'r') as f:
            data = json.load(f)
        try:
            for bad_word in data[str(message.guild.id)]["blacklist"]:
                if bad_word in message.content:
                    await message.delete()
                    embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                          description='Deine Message `wurde gelöscht`, da du ein Wort `aus der Blacklist darin hattest!`\n**Bitte unterlasse dies!**')
                    await message.channel.send(embed=embed, delete_after=5)

                    with open('utils/json/on_guild.json', 'r') as f:
                        guild_data = json.load(f)

                    log_channel = self.bot.get_channel(id=guild_data[str(message.author.guild.id)]["moderation_log_channel"])
                    embed = discord.Embed(
                        description=f'{message.author} hat ein Wort aus der Blacklist geschrieben!',
                        color=discord.Color.red())
                    await log_channel.send(embed=embed)
        except AttributeError:
            pass


def setup(bot):
    bot.add_cog(blacklistListener(bot))
