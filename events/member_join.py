import datetime
import discord
from discord.ext import commands

bot = commands.Bot


class on_member_join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel = bot.get_channel(855515768341921818)
        embed = discord.Embed(title=f'> Welcome',
                              description=f'{member.mention} Joined {member.guild.name}',
                              color=discord.Color.random(),
                              timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=f'{member.icon_url}')
        embed.add_field(name=f'Total members',
                        value=f'{member.guild.member_count}')
        embed.set_footer(text=f'{member.name} joined ')
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(on_member_join(bot))
