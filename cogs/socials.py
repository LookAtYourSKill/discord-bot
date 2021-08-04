import datetime

import discord
import pytz
from discord.ext import commands
from discord.ext.commands import Cog


class Socials(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def twitch(self, ctx):
        de = pytz.timezone('Europe/Berlin')
        embed = discord.Embed(title=f'> **Twitch von Wichtiger**',
                              description=f'Link: `https://www.twitch.tv/wichtiger`',
                              color=0xb200ff,
                              timestamp=datetime.datetime.utcnow().astimezone(tz=de))
        embed.set_thumbnail(url='https://static-cdn.jtvnw.net/jtv_user_pictures/0f21fa4c-51e9-4d77-bdea-dd80bb330052-profile_image-70x70.png')
        embed.set_footer(text=f'Angefordert von {ctx.author}',
                         icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def youtube(self, ctx):
        de = pytz.timezone('Europe/Berlin')
        embed = discord.Embed(title=f'> **Youtube von Wichtiger**',
                              description=f'Link: `https://www.youtube.com/wichtiger`',
                              color=0xff0000,
                              timestamp=datetime.datetime.utcnow().astimezone(tz=de))
        embed.set_thumbnail(url='https://static-cdn.jtvnw.net/jtv_user_pictures/0f21fa4c-51e9-4d77-bdea-dd80bb330052-profile_image-70x70.png')
        embed.set_footer(text=f'Angefordert von {ctx.author}',
                         icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def streamplan(self, ctx):
        de = pytz.timezone('Europe/Berlin')
        embed = discord.Embed(title=f'> **Hier geht zu Wichtigers Streamplan**',
                              description=f'Link: `https://www.twitch.tv/wichtiger/schedule`',
                              color=0xb200ff,
                              timestamp=datetime.datetime.utcnow().astimezone(tz=de))
        embed.set_thumbnail(url='https://static-cdn.jtvnw.net/jtv_user_pictures/0f21fa4c-51e9-4d77-bdea-dd80bb330052-profile_image-70x70.png')
        embed.set_footer(text=f'Angefordert von {ctx.author}',
                         icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def twitter(self, ctx):
        de = pytz.timezone('Europe/Berlin')
        embed = discord.Embed(title=f'> **Hier geht zu Wichtigers Twitter**',
                              description=f'Link: `https://twitter.com/WichtigerYT`',
                              color=0x00c5ff,
                              timestamp=datetime.datetime.utcnow().astimezone(tz=de))
        embed.set_thumbnail(
            url='https://static-cdn.jtvnw.net/jtv_user_pictures/0f21fa4c-51e9-4d77-bdea-dd80bb330052-profile_image-70x70.png')
        embed.set_footer(text=f'Angefordert von {ctx.author}',
                         icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Socials(bot)
                )