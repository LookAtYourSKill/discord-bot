import discord
from discord.ext import commands


class onPing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ping(self, ctx, message, member):
        if message.content.startswith("@PagMan Bot#0264 "):
            embed = discord.Embed(title="Prefix", color=0xff00c8)
            embed.add_field(name="You pinged me",
                            value=f"My Prefix is **?**")
            await member.send(embed=embed)

def setup(bot):
    bot.add_cog(onPing(bot))