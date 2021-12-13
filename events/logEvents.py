import json

import discord
from discord.ext import commands

with open('./config.json', 'r') as config_file:
    config = json.load(config_file)

class LogEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_ban(self, guild, member):
        logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.ban).flatten()
        channel = guild.get_channel(id=config['moderation_log_channel'])
        logs = logs[0]
        if logs.target == member:
            embed = discord.Embed(title='Ban Log',
                                  color=discord.Color.random())
            embed.add_field(name=f'**Information**',
                            value=f'`{logs.user}` has banned `{logs.target}`\n'
                                  f'User ID : `{logs.target.id}`\n'
                                  f'The time : `{logs.created_at.strftime("%d.%m.%Y, %H:%M:%S")}`\n'
                                  f'The reason : `{logs.reason}`',
                            inline=False)
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_unban(self, guild, member):
        logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.unban).flatten()
        channel = guild.get_channel(config['moderation_log_channel'])
        logs = logs[0]
        if logs.target == member:
            embed = discord.Embed(title='Unban Log',
                                  color=discord.Color.random())
            embed.add_field(name=f'**Information**',
                            value=f'`{logs.user}` has unbanned `{logs.target}`\n'
                                  f'User ID : `{logs.target.id}`\n'
                                  f'The time : `{logs.created_at.strftime("%d.%m.%Y, %H:%M:%S")}`',
                            inline=False)
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_kick(self, guild, member):
        logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.kick).flatten()
        channel = guild.get_channel(id=config['moderation_log_channel'])
        logs = logs[0]
        if logs.target == member:
            embed = discord.Embed(title='Kick Log',
                                  color=discord.Color.random())
            embed.add_field(name=f'**Information**',
                            value=f'`{logs.user}` has kicked `{logs.target}`\n'
                                  f'User ID : `{logs.target.id}`\n'
                                  f'The time : `{logs.created_at.strftime("%d.%m.%Y, %H:%M:%S")}`',
                            inline=False)
            await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(LogEvents(bot))
