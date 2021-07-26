import datetime
import discord
import pytz
from discord.ext import commands


class usage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def usage_ban(self, ctx):
        embed = discord.Embed(title='**ban [`@user`] <`reason`>**',
                              description='Bannt einen User! \n'
                                          '**Aliases:**`/`',
                              color=0x4cd137)
        embed.set_footer(text='[] verpflichtend | <> optional')
        await ctx.send(embed=embed)

    @commands.command()
    async def usage_unban(self, ctx):
        embed = discord.Embed(title='**unban [`@user`]**',
                              description='Entbannt einen User! \n'
                                          '**Aliases:**`/`',
                              color=0x4cd137)
        embed.set_footer(text='[] verpflichtend | <> optional')
        await ctx.send(embed=embed)

    @commands.command()
    async def usage_kick(self, ctx):
        embed = discord.Embed(title='**kick [`@user`] <`reason`>**',
                              description='Kickt einen User! \n'
                                          '**Aliases:**`/`',
                              color=0x4cd137)
        embed.set_footer(text='[] verpflichtend | <> optional')
        await ctx.send(embed=embed)

    @commands.command()
    async def usage_mute(self, ctx):
        embed = discord.Embed(title='**mute [`@user`] <`reason`>**',
                              description='Mutet einen User! \n'
                                          '**Aliases:**`/`',
                              color=0x4cd137)
        embed.set_footer(text='[] verpflichtend | <> optional')
        await ctx.send(embed=embed)

    @commands.command()
    async def usage_unmute(self, ctx):
        embed = discord.Embed(title='**unmute [`@user`] <`reason`>**',
                              description='Entmutet einen User! \n'
                                          '**Aliases:**`/`',
                              color=0x4cd137)
        embed.set_footer(text='[] verpflichtend | <> optional')
        await ctx.send(embed=embed)

    @commands.command()
    async def usage_slowmode(self, ctx):
        embed = discord.Embed(title='**slowmode [sec]**',
                              description='Macht ein Slowmode in den Channel! \n'
                                          '**Aliases:**`sm`',
                              color=0x4cd137)
        embed.set_footer(text='[] verpflichtend | <> optional')
        await ctx.send(embed=embed)

    @commands.command()
    async def usage_clear(self, ctx):
        embed = discord.Embed(title='**clear [amount]**',
                              description='Löscht die bestimmte Anzahl von Nachrichten! \n'
                                          '**Aliases:**`pruge`',
                              color=0x4cd137)
        embed.set_footer(text='[] verpflichtend | <> optional')
        await ctx.send(embed=embed)

    @commands.command()
    async def usage_bannedUserList(self, ctx):
        embed = discord.Embed(title='**bannedUserList**',
                              description='Zeigt die Leute an, welche gebannt sind! \n'
                                          '**Aliases:**`banned`',
                              color=0x4cd137)
        embed.set_footer(text='[] verpflichtend | <> optional')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(usage(bot))
