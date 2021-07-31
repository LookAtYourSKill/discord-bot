import asyncio
import datetime
import discord
import pytz
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.user = None
        self.commands = None
        self.bot = bot

    @commands.command(name='help')
    async def help(self, ctx):
        de = pytz.timezone('Europe/Berlin')
        embed = discord.Embed(title=f'> Help',
                              description=f'`Prefix = ?`',
                              color=0x4cd137,
                              timestamp=datetime.datetime.utcnow().astimezone(tz=de))
        embed.add_field(name='**Moderation**',
                        value=f'`ban`, `unban`, `tempban`,`bannedUserList`, `mute`, `unmute`, `tempmute`, `kick`, `slowmode`, `clear`',
                        inline=False)
        embed.add_field(name='**Infos**',
                        value=f'`server`, `user`, `bot`, `avatar`, `members`, `help`',
                        inline=False)
        embed.add_field(name='**Utilities**',
                        value=f'`invite`, `botinvite`, `ping`, `repeat`, `embed`',
                        inline=False)
        embed.add_field(name='**Giveaway**',
                        value=f'`create`',
                        inline=False)
        embed.add_field(name='**Fun**',
                        value='`8ball`, `roll`, `slots`, `rps`')
        embed.add_field(name='**Usage**',
                        value=f'`usage_ + module`',
                        inline=False)
        embed.add_field(name='**Levels**',
                        value=f'`level`, `rank`',
                        inline=False)
        #embed.add_field(name='**Socials**',
        #                value=f'`twitch`, `youtube`, `twitter`, `streamplan`',
        #                inline=False)
        embed.set_footer(text=f'Angefordert von {ctx.author}',
                         icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                  description=f'**Unknown Command!**',
                                  color=0x4cd137)
            await asyncio.sleep(1)
            await ctx.message.delete()
            await ctx.send(embed=embed, delete_after=5)


def setup(bot):
    bot.add_cog(Help(bot))
