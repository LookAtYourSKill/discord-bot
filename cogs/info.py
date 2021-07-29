import datetime
import sys
import discord
import pytz
from discord import message
from discord.ext import commands

bot = commands.Bot


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='user', aliases=['userinfo', 'info'], help='?userinfo [@user]')
    async def user(self, ctx, member: discord.Member):
        de = pytz.timezone('Europe/Berlin')
        embed = discord.Embed(title=f'> Userinfo für {member.display_name}',
                              description='',
                              color=0x4cd137,
                              timestamp=datetime.datetime.utcnow().astimezone(tz=de))

        embed.set_image(url=f'{member.avatar_url}')
        embed.add_field(name='Name',
                        value=f'```{member.name}#{member.discriminator}```',
                        inline=True)
        embed.add_field(name='Bot',
                        value=f'```{("Ja" if member.bot else "Nein")}```',
                        inline=True)
        embed.add_field(name='Nickname',
                        value=f'```{(member.nick if member.nick else "Nicht gesetzt")} ```',
                        inline=True)
        embed.add_field(name='Server Beigetreten',
                        value=f'```{member.joined_at.strftime("%d.%m.%Y")}```',
                        inline=True)
        embed.add_field(name='Discord Beigetreten',
                        value=f'```{member.created_at.strftime("%d.%m.%Y")}```',
                        inline=True)
        embed.add_field(name='Rollen',
                        value=f'```{len(member.roles) - 1}```',
                        inline=True)
        embed.add_field(name='Höchste Rolle',
                        value=f'```{member.top_role.name}```',
                        inline=True)
        embed.add_field(name='Farbe',
                        value=f'```{member.color}```',
                        inline=True)
        embed.add_field(name='Booster',
                        value=f'```{("Ja" if member.premium_since else "Nein")}```',
                        inline=True)
        embed.set_footer(text=f'Angefordert von {ctx.author.name}',
                         icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(name='server', aliases=['serverinfo', 'guild'], help='?serverinfo [guildid]')
    async def server(self, ctx):
        de = pytz.timezone('Europe/Berlin')
        role_count = len(ctx.guild.roles)
        list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]
        embed = discord.Embed(title=f'> Info für {ctx.guild.name}',
                              description='',
                              color=0x4cd137,
                              timestamp=datetime.datetime.utcnow().astimezone(tz=de))

        embed.set_thumbnail(url=f'{ctx.guild.icon_url}')
        embed.add_field(name='**Owner ID**',
                        value=f'```{ctx.guild.owner_id}```',
                        inline=True)
        embed.add_field(name='**Server ID**',
                        value=f'```{ctx.guild.id}```',
                        inline=True)
        embed.add_field(name='**Server Name**',
                        value=f'```{ctx.guild.name}```',
                        inline=True)
        embed.add_field(name='**Creation Date**',
                        value=f'```{ctx.guild.created_at.strftime("%d.%m.%Y")}```',
                        inline=True)
        embed.add_field(name='**Region**',
                        value=f'```{ctx.guild.region}```',
                        inline=True)
        #embed.add_field(name='**Bots**',
        #                value=f'```, ```'.join(list_of_bots),
        #                inline=True)
        embed.add_field(name='**Member Count**',
                        value=f'```{ctx.guild.member_count}```',
                        inline=True)
        embed.add_field(name='**Roles**',
                        value=str(role_count),
                        inline=True)
        embed.add_field(name='**Default Role**',
                        value=f'```{ctx.guild.default_role}```',
                        inline=True)
        embed.set_footer(text=f'Angefordert von {ctx.author.name}',
                         icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def members(self, ctx):
        embed = discord.Embed(title='**Server Member**',
                              description=f'Auf **diesem Server** sind `{ctx.guild.member_count}` member!')
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
                        value='```LookAtYourSkill#0001 \n493370963807830016```',
                        inline=True)
        embed.add_field(name='Versionen',
                        value=f'```Python: {python_version}\nDiscord: {discord.__version__}```',
                        inline=True)
        embed.add_field(name='**Server Anzahl**',
                        value=f'```{len(self.bot.guilds)}```',
                        inline=True)
        embed.set_footer(text=f'Angefrodert von {ctx.author}',
                         icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(name='avatar', aliases=['av'], help='?avatar [@user]')
    async def avatar(self, ctx, member: discord.Member):
        if not member:
            member = ctx.author
        icon = member.avatar_url
        embed = discord.Embed(
            title='',
            color=0x123456,
            timestamp=datetime.datetime.utcnow()) \
            .set_author(name=f'{member.name}#{member.discriminator}',
                        icon_url=icon) \
            .set_image(url=icon) \
            .set_footer(icon_url=ctx.author.avatar_url, text=f'Angefordert von {ctx.author.name}')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))
