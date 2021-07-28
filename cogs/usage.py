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
                                          '\n'
                                          '**Aliases:**`/`',
                              color=0x4cd137)
        embed.set_footer(text='[] verpflichtend | <> optional')
        await ctx.send(embed=embed)

    @commands.command()
    async def usage_unban(self, ctx):
        embed = discord.Embed(title='**unban [`@user`]**',
                              description='Entbannt einen User! \n'
                                          '\n'
                                          '**Aliases:**`/`',
                              color=0x4cd137)
        embed.set_footer(text='[] verpflichtend | <> optional')
        await ctx.send(embed=embed)

    @commands.command()
    async def usage_kick(self, ctx):
        embed = discord.Embed(title='**kick [`@user`] <`reason`>**',
                              description='Kickt einen User! \n'
                                          '\n'
                                          '**Aliases:**`/`',
                              color=0x4cd137)
        embed.set_footer(text='[] verpflichtend | <> optional')
        await ctx.send(embed=embed)

    @commands.command()
    async def usage_mute(self, ctx):
        embed = discord.Embed(title='**mute [`@user`] <`reason`>**',
                              description='Mutet einen User! \n'
                                          '\n'
                                          '**Aliases:**`/`',
                              color=0x4cd137)
        embed.set_footer(text='[] verpflichtend | <> optional')
        await ctx.send(embed=embed)

    @commands.command()
    async def usage_unmute(self, ctx):
        embed = discord.Embed(title='**unmute [`@user`] <`reason`>**',
                              description='Entmutet einen User! \n'
                                          '\n'
                                          '**Aliases:**`/`',
                              color=0x4cd137)
        embed.set_footer(text='[] verpflichtend | <> optional')
        await ctx.send(embed=embed)

    @commands.command()
    async def usage_slowmode(self, ctx):
        embed = discord.Embed(title='**slowmode [`sec`]**',
                              description='Macht ein Slowmode in den Channel! \n'
                                          '\n'
                                          '**Aliases:**`sm`',
                              color=0x4cd137)
        embed.set_footer(text='[] verpflichtend | <> optional')
        await ctx.send(embed=embed)

    @commands.command()
    async def usage_clear(self, ctx):
        embed = discord.Embed(title='**clear [`amount`]**',
                              description='Löscht die bestimmte Anzahl von Nachrichten! \n'
                                          '\n'
                                          '**Aliases:**`pruge`',
                              color=0x4cd137)
        embed.set_footer(text='[] verpflichtend | <> optional')
        await ctx.send(embed=embed)

    @commands.command()
    async def usage_bannedUserList(self, ctx):
        embed = discord.Embed(title='**bannedUserList**',
                              description='Zeigt die Leute an, welche gebannt sind! \n'
                                          '\n'
                                          '**Aliases:**`banned`',
                              color=0x4cd137)
        embed.set_footer(text='[] verpflichtend | <> optional')
        await ctx.send(embed=embed)

    @commands.command()
    async def usage_create(self, ctx):
        embed = discord.Embed(title='**create [`time`] [`prize`]**',
                              description='Erstellt ein Giveaway! \n'
                                          '\n'
                                          '**Zeiten:**\n'
                                          '`s` Sekunden\n'
                                          '`m` Minuten\n'
                                          '`h` Stunden\n'
                                          '`d` Tage\n'
                                          '`w` Wochen\n'
                                          '\n'
                                          '**Aliases:**`giveaway`',
                              color=0x4cd137)
        embed.set_footer(text='[] verpflichtend | <> optional')
        await ctx.send(embed=embed)

    @commands.command()
    async def usage_giveaway(self, ctx):
        embed = discord.Embed(title='**create [`time`] [`prize`]** \n',
                              description='Erstellt ein Giveaway! \n'
                                          '\n'
                                          '**Zeiten:**\n'
                                          '`s` Sekunden\n'
                                          '`m` Minuten\n'
                                          '`h` Stunden\n'
                                          '`d` Tage\n'
                                          '`w` Wochen\n'
                                          '\n'
                                          '**Aliases:**`create`',
                              color=0x4cd137)
        embed.set_footer(text='[] verpflichtend | <> optional')
        await ctx.send(embed=embed)

    @commands.command()
    async def usage_user(self, ctx):
        embed = discord.Embed(title='**user** [`@user`] \n',
                              description='Zeigt eine Userinfo über den User an! \n'
                                          '\n'
                                          '**Aliases:**`userinfo`, `info`',
                              color=0x4cd137)
        embed.set_footer(text='[] verpflichtend | <> optional')
        await ctx.send(embed=embed)

    @commands.command()
    async def usage_avatar(self, ctx):
        embed = discord.Embed(title='**avatar** [`@user`] \n',
                              description='Zeigt den Avatar des Users an! \n'
                                          '\n'
                                          '**Aliases:**`av`',
                              color=0x4cd137)
        embed.set_footer(text='[] verpflichtend | <> optional')
        await ctx.send(embed=embed)

    @commands.command()
    async def usage_repeat(self, ctx):
        embed = discord.Embed(title='**repeat** [`argument`] \n',
                              description='Gibt das wieder, was der User eingegeben hat! \n'
                                          '\n'
                                          '**Aliases:**`echo`, `mimic`, `copy`',
                              color=0x4cd137)
        embed.set_footer(text='[] verpflichtend | <> optional')
        await ctx.send(embed=embed)

    @commands.command()
    async def usage_embed(self, ctx):
        embed = discord.Embed(title='**embed** [`argument`] \n',
                              description='Gibt die Nachricht des Users als **Embed** wieder! \n'
                                          '\n'
                                          '**Aliases:**`/`',
                              color=0x4cd137)
        embed.set_footer(text='[] verpflichtend | <> optional')
        await ctx.send(embed=embed)

    @commands.command()
    async def usage_tempban(self, ctx):
        embed = discord.Embed(title='**tempban** [`@user`] [`time`] [`reason`] \n',
                              description='Bannt einen User für eine bestimmte Zeit! \n'
                                          '\n'
                                          '**Zeiten:**\n'
                                          '`s` Sekunden\n'
                                          '`m` Minuten\n'
                                          '`h` Stunden\n'
                                          '`d` Tage\n'
                                          '`w` Wochen\n'
                                          '\n'
                                          '**Aliases:**`tban`',
                              color=0x4cd137)
        embed.set_footer(text='[] verplichtend | <> optinal')
        await ctx.send(embed=embed)

    @commands.command()
    async def usage_tempmute(self, ctx):
        embed = discord.Embed(title='**tempmute** [`@user`] [`time`] [`reason`] \n',
                              description='Mutet einen User für eine bestimmte Zeit! \n'
                                          '\n'
                                          '**Zeiten:**\n'
                                          '`s` Sekunden\n'
                                          '`m` Minuten\n'
                                          '`h` Stunden\n'
                                          '`d` Tage\n'
                                          '`w` Wochen\n'
                                          '\n'
                                          '**Aliases:**`tmute`',
                              color=0x4cd137)
        embed.set_footer(text='[] verplichtend | <> optinal')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(usage(bot))
