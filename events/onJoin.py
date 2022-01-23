import datetime
import json

import discord
from discord.ext import commands

with open('./etc/config.json', 'r') as config_file:
    config = json.load(config_file)


class onJoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        #if member.bot:
        #    role = discord.utils.get(self.bot.guild.roles, id=config["bot_role"])
        #    await self.bot.add_role(self.bot, role)

        channel = self.bot.get_channel(id=config['welcome_channel'])
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

        days = (datetime.datetime.utcnow() - member.created_at).days
        if days < 7:
            embed = discord.Embed(title='Antialt Detection Kick',
                                  description=f'**Your Account** has to be **at least 7 days old!**\n'
                                              f'**Your Account** Age : `{days}` days old\n'
                                              f'**Must be** at least : `7` days old',
                                  color=discord.Color.red())
            await member.send(embed=embed)
            await member.kick(reason='Anti Alt Detection')

            embed = discord.Embed(title='Antialt Detection Kick',
                                  description=f'`{member}` wurde von der **Alt Detection gekickt!**',
                                  color=discord.Color.green())
            channel = self.bot.get_channel(id=config['moderation_log_channel'])
            await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(onJoin(bot))
