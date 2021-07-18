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
                              description='Verwende **!help [Command]** für Hilfe über einen Command \nund **!help ['
                                          'Modul]** für Hilfe über ein Modul.',
                              color=0x4cd137,
                              timestamp=datetime.datetime.utcnow().astimezone(tz=de))
        embed.add_field(name='**Moderation**',
                        value=f'`ban`, `unban`,`bannedUserList`, `mute`, `unmute`, `kick`, `slowmode`, `clear`',
                        inline=False)
        embed.add_field(name='**Infos**',
                        value=f'`server`, `user`, `bot`, `avatar`, `help`',
                        inline=False)
        embed.add_field(name='**Utilities**',
                        value=f'`invite`, `botinvite`, `ping`, `repeat`',
                        inline=False)
        embed.add_field(name='**Music**',
                        value=f'`join`, `leave`, `play`, `resume`, `pause`, `queue`, `loop`, `nowplaying`, `remove`, `skip`')
        embed.add_field(name='**Socials**',
                        value=f'`twitch`, `youtube`, `twitter`, `streamplan`',
                        inline=False)
        embed.set_footer(text=f'Angefordert von {ctx.author}',
                         icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                  description=f'**Unknown Command!**\n `Use !help to see all commands`',
                                  color=0x4cd137)
            await asyncio.sleep(1)
            await ctx.message.delete()
            await ctx.send(embed=embed, delete_after=5)


def setup(bot):
    bot.add_cog(Help(bot))
