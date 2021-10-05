import datetime
import discord
from discord.ext import commands


class onJoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(855515768341921818)
        embed = discord.Embed(title=f'> Welcome',
                              description=f'{member.mention} Joined **{member.guild.name}**',
                              color=discord.Color.random(),
                              timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=f'{member.avatar_url}')
        embed.add_field(name=f'Total members',
                        value=f'{member.guild.member_count}',
                        inline=False)
        embed.set_footer(text=f'{member.name} joined ')
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def antialt(self, member=None):
        days = (datetime.datetime.utcnow() - member.created_at).days
        if days < 7:
            embed = discord.Embed(title='**Antialt Detection Kick**',
                                  description=f'Your Account has to be at least 7 Days old!\n'
                                              f'Your Account Age : `{days}` days old\n'
                                              f'Must atleast be : `7` Days old')
            await member.send(embed=embed)
            await member.kick(reason='Anti Alt Detection')

            embed = discord.Embed(title='**Antialt Detection Kick**',
                                  description=f'{member} wurde von der Alt Detection gekickt.')

            channel = self.bot.get_channel(882721258301685790)
            await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(onJoin(bot))
