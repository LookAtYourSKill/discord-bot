import datetime
import sys
import discord
import pytz
from discord.ext import commands

bot = commands.Bot


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='user', aliases=['userinfo', 'info'], help='?userinfo [@user]')
    async def user(self, ctx, member: discord.Member):
        if member.mention is None:
            member = ctx.author.mention
        de = pytz.timezone('Europe/Berlin')
        embed = discord.Embed(title=f'> Userinfo für {member.display_name}',
                              description='',
                              color=0x4cd137,
                              timestamp=datetime.datetime.utcnow().astimezone(tz=de))

        embed.set_thumbnail(url=f'{member.avatar_url}')
        embed.add_field(name='**Name**',
                        value=f'```Name: {member.name}#{member.discriminator}\n'
                              f'Nick: {(member.nick if member.nick else "Nein")}\n'
                              f'ID: {member.id}```',
                        inline=False)
        embed.add_field(name='**Account**',
                        value=f'```Discord Beigetreten: {member.created_at.strftime("%d.%m.%Y")}\n'
                              f'Server Beigetreten: {member.joined_at.strftime("%d.%m.%Y")}\n'
                              f'Booster: {("Ja" if member.premium_since else "Nein")}\n'
                              f'Bot: {("Ja" if member.bot else "Nein")}```',
                        inline=False)
        embed.add_field(name='**Rollen**',
                        value=f'```Rollen des Users: {len(member.roles) - 1}\n'
                              f'Höchste Rolle: {member.top_role.name}```',
                        inline=False)
        embed.set_footer(text=f'Angefordert von {ctx.author.name}#{ctx.author.discriminator}',
                         icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(name='server', aliases=['serverinfo', 'guild'], help='?serverinfo [guildid]')
    async def server(self, ctx):
        de = pytz.timezone('Europe/Berlin')
        role_count = len(ctx.guild.roles)
        embed = discord.Embed(title=f' ',
                              description=' ',
                              color=0x4cd137,
                              timestamp=datetime.datetime.utcnow().astimezone(tz=de))

        embed.set_thumbnail(url=f'{ctx.guild.icon_url}')
        embed.add_field(name=f'> Info für {ctx.guild.name}',
                        value=f'```Name : {ctx.guild.name}\n'
                              f'ID : {ctx.guild.id}\n'
                              f'Owner ID : {ctx.guild.owner_id}\n'
                              f'Region : {ctx.guild.region}```',
                        inline=False)
        embed.add_field(name='**Daten**',
                        value=f'```Erstellt: {ctx.guild.created_at.strftime("%d.%m.%Y")}```',
                        inline=False)
        embed.add_field(name='**Member**',
                        value=f'```{ctx.guild.member_count}```',
                        inline=False)
        embed.add_field(name='**Roles**',
                        value=f'```Deafault Role : {ctx.guild.default_role}\n'
                              f'Alle Rollen : {str(role_count)}```',
                        inline=False)
        embed.set_footer(text=f'Angefordert von {ctx.author.name}#{ctx.author.discriminator}',
                         icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def members(self, ctx):
        embed = discord.Embed(title='**Server Member**', )
        embed.add_field(name='**Mitglieder**',
                        value=f'Auf diesem Server sind `{ctx.guild.member_count}` Mitlieder!')
        await ctx.send(embed=embed)

    @commands.command(name='bot', aliases=['botinfo'], help='?botinfo')
    async def bot(self, ctx):
        de = pytz.timezone('Europe/Berlin')
        python_version = '{}.{}.{}'.format(*sys.version_info[:3])
        embed = discord.Embed(title=f'> Bot Info ',
                              description='',
                              color=0x4cd137,
                              timestamp=datetime.datetime.utcnow().astimezone(tz=de))

        embed.add_field(name='**Besitzer**',
                        value='```LookAtYourSkill#0001 \nID : 493370963807830016```',
                        inline=True)
        embed.add_field(name='Versionen',
                        value=f'```Python: {python_version}\nDiscord: {discord.__version__}```',
                        inline=True)
        embed.add_field(name='**Server Anzahl**',
                        value=f'```{len(self.bot.guilds)}```',
                        inline=True)
        embed.set_footer(text=f'Angefrodert von {ctx.author.name}#{ctx.author.discriminator}',
                         icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(name='avatar', aliases=['av'], help='?avatar [@user]')
    async def avatar(self, ctx, member: discord.Member):
        if not member:
            member = ctx.author
        icon = member.avatar_url
        embed = discord.Embed(title='',
                              color=0x123456,
                              timestamp=datetime.datetime.utcnow())
        embed.set_author(name=f'{member.name}#{member.discriminator}',
                         icon_url=icon)
        embed.set_image(url=icon)
        embed.set_footer(icon_url=ctx.author.avatar_url,
                         text=f'Angefordert von {ctx.author.name}#{ctx.author.discriminator}')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))
