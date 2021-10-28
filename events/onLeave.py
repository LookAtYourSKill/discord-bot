import datetime
import json
import discord
from discord.ext import commands

with open('./config.json', 'r') as config_file:
    config = json.load(config_file)

class onLeave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(id=config['leave_channel'])
        embed = discord.Embed(title=f'> Left',
                              description=f'{member.mention} left **{member.guild.name}**',
                              color=discord.Color.random(),
                              timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=f'{member.avatar_url}')
        embed.add_field(name=f'Total members',
                        value=f'{member.guild.member_count}',
                        inline=False)
        embed.set_footer(text=f'{member.name} left ')
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(onLeave(bot))