import datetime
import json
import discord
from discord.ext import commands


class onLeave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        with open('utils/json/on_guild.json', 'r') as f:
            guild_data = json.load(f)

        if not guild_data[str(member.guild.id)]['leave_channel']:
            return

        else:
            channel = self.bot.get_channel(id=guild_data[str(member.guild.id)]['leave_channel'])
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
