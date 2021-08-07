import datetime
import discord
from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message, member: discord.Member = None):
        if message.content.startswith("@Ich seh dich"):
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
        channel = discord.utils.get(member.guild.channels, id=855515768341921818)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_ban(self, guild, member):
        logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.ban).flatten()
        channel = guild.get_channel(872945922743619657)
        logs = logs[0]
        if logs.target == member:
            embed = discord.Embed(title='BackUp Ban Log',
                                  color=discord.Color.random())
            embed.add_field(name=f'**Information**',
                            value=f'`{logs.user}` has just unbanned `{logs.target}`\n'
                                  f'The time : `{logs.created_at.strftime("%d.%m.%Y, %H:%M:%S")}`\n'
                                  f'The reason : `{logs.reason}`',
                            inline=False)
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_unban(self, guild, member):
        logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.unban).flatten()
        channel = guild.get_channel(872945922743619657)
        logs = logs[0]
        if logs.target == member:
            embed = discord.Embed(title='BackUp Unban Log',
                                  color=discord.Color.random())
            embed.add_field(name=f'**Information**',
                            value=f'`{logs.user}` has just unbanned `{logs.target}`\n'
                                  f'The time : `{logs.created_at.strftime("%d.%m.%Y, %H:%M:%S")}`',
                            inline=False)
            await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Events(bot))
