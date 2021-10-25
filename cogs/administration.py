import asyncio
import discord
from discord.ext import commands

class Administration(commands.Cog):
    """
    `Admin commands`
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="setstatus")
    @commands.is_owner()
    @commands.cooldown(rate=30, per=1)
    async def setstatus(self, ctx: commands.Context, *, text: str):
        """
        Change or set the status for the bot
        """

        await self.bot.change_presence(activity=discord.Game(name=text))
        embed = discord.Embed(title='<:open:869959941321011260> Erfolgreich',
                              description=f'Successfully changed bot status to **{text}**')
        await ctx.send(embed=embed, delete_after=5)
        await asyncio.sleep(1)
        await ctx.message.delete()

    @commands.command(name='lock', aliases=['lockdown'])
    @commands.has_permissions(administrator=True)
    async def lock(self, ctx):
        """
        Lock a channel, so nobody can write in it
        """

        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        embed = discord.Embed(title='',
                              description=f'`{ctx.channel}` ist nun **im Lockdown**',
                              color=0x4cd137)
        embed.add_field(name='**Information**',
                        value=f'Channel im Lockdown : `{ctx.channel}`\n'
                              f'In Lockdown gesetzt von : `{ctx.author}`')
        await ctx.send(embed=embed, delete_after=5)
        await asyncio.sleep(1)
        await ctx.message.delete()

        channel = self.bot.get_channel(id=872945922743619657)
        await channel.send(embed=embed)

    @commands.command(name='release', aliases=['unlock'])
    @commands.has_permissions(administrator=True)
    async def unlock(self, ctx):
        """
        Unlock the channel you locked before
        """

        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)

        embed = discord.Embed(title='',
                              description=f'`{ctx.channel}` ist nun **nicht mehr im Lockdown**',
                              color=0x4cd137)
        embed.add_field(name='**Information**',
                        value=f'Unlocked Channel : `{ctx.channel}`\n'
                              f'Aus dem Lockdown genommen von : `{ctx.author}`')
        await ctx.send(embed=embed, delete_after=5)
        await asyncio.sleep(1)
        await ctx.message.delete()

        channel = self.bot.get_channel(id=872945922743619657)
        await channel.send(embed=embed)

    @commands.command(alises=['announce'])
    @commands.has_permissions(administrator=True)
    async def say(self, ctx, *, text):
        """
        Give back your text with a `@everyone` at the beginning!
        """

        role = ctx.guild.default_role
        await ctx.send(f'{role}, {text}')

def setup(bot):
    bot.add_cog(Administration(bot)
                )
