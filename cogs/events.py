import datetime
import discord
from discord.ext import commands

bot = commands.Bot(intense=discord.Intents.all(), command_prefix='?', help_command=commands.MinimalHelpCommand())
bot.remove_command('help')

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith('<@790965419670241281>'):
            embed = discord.Embed(title="Prefix", color=0xff00c8)
            embed.add_field(name="Wowowow a Ping",
                            value=f"Mein Prefix: **?**\n"
                                  f"Mit ?help kannst du dir alle command anschauen!",
                            inline=False)
            await message.author.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel = discord.utils.get(member.guild.channels, id=855515768341921818)
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
    bot.add_cog(Events(bot))
