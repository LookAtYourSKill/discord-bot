import datetime
import discord
from discord.ext import commands

class onPing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith('<@790965419670241281>'):
            embed = discord.Embed(title="Prefix", color=0xff00c8)
            embed.add_field(name="Wowowow a Ping",
                            value=f"Mein Prefix: **?**\n"
                                  f"Mit ?help kannst du dir alle command anschauen!",
                            inline=False)
            await message.author.send(embed=embed)


def setup(bot):
    bot.add_cog(onPing(bot))
