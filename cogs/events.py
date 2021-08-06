import datetime
import discord
from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message, member: discord.Member = None):
        if message.content.startswith("@PagMan Bot#0264 "):
            embed = discord.Embed(title="Prefix", color=0xff00c8)
            embed.add_field(name="You pinged me",
                            value=f"My Prefix is **?**",
                            inline=False)
            await member.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        embed = discord.Embed(title=f'> Welcome',
                              description=f'{member.mention} Joined {member.guild.name}',
                              color=discord.Color.random(),
                              timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=f'{member.icon_url}')
        embed.add_field(name=f'Total members',
                        value=f'{member.guild.member_count}')
        embed.set_footer(text=f'{member.name} joined ')
        channel = self.bot.get_channel(855515768341921818)
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Events(bot))
