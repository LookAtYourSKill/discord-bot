import datetime
import json
import disnake as discord
from disnake.ext import commands
from disnake.utils import get


class onJoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open('utils/json/on_guild.json', 'r') as f:
            guild_data = json.load(f)

        if member.bot:
            if guild_data[str(member.guild.id)]["bot_role"]:
                role = get(member.guild.roles, id=guild_data[str(member.guild.id)]["bot_role"])
                await member.add_roles(role)
            else:
                return

        elif not guild_data[str(member.guild.id)]['welcome_channel']:
            days = (datetime.datetime.utcnow() - member.created_at).days
            if days < 7:
                embed = discord.Embed(title='Antialt Detection Kick',
                                      description=f'**Your Account** has to be **at least 7 days old!**\n'
                                                  f'**Your Account** Age : `{days}` days old\n'
                                                  f'**Must be** at least : `7` days old',
                                      color=discord.Color.red())
                await member.send(embed=embed)
                await member.kick(reason='Anti Alt Detection')

                if guild_data[str(member.guild.id)]["moderation_log_channel"]:
                    embed = discord.Embed(title='Antialt Detection Kick',
                                          description=f'`{member}` wurde von der **Alt Detection gekickt!**',
                                          color=discord.Color.green())
                    channel = self.bot.get_channel(id=guild_data[str(member.guild.id)]['moderation_log_channel'])
                    await channel.send(embed=embed)
                else:
                    return

        else:
            channel = self.bot.get_channel(id=guild_data[str(member.guild.id)]['welcome_channel'])
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

                if guild_data[str(member.guild.id)]["moderation_log_channel"]:
                    embed = discord.Embed(title='Antialt Detection Kick',
                                          description=f'`{member}` wurde von der **Alt Detection gekickt!**',
                                          color=discord.Color.green())
                    channel = self.bot.get_channel(id=guild_data[str(member.guild.id)]['moderation_log_channel'])
                    await channel.send(embed=embed)
                else:
                    return


def setup(bot):
    bot.add_cog(onJoin(bot))
