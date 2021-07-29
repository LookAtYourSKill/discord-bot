import asyncio

import discord
from discord.ext import commands
from discord.ext.commands import bot

bot = commands.Bot(intense=discord.Intents.all(), command_prefix='?')

class Utilities(commands.Cog):
    def __init__(self):
        self.bot = bot

    @commands.command(name='invite', help='?invite')
    async def invite(self, ctx):
        invite = await ctx.channel.create_invite(reason="eShrug")
        embed = discord.Embed(title=' ',
                              description=f'{ctx.author.mention} hier ist ein Invite Link zum Server: **{ctx.guild.name}**!\n`{invite}`',
                              color=0x4cd137)
        await ctx.send(embed=embed)

    @commands.command(name='botinvite', help='?botinvite')
    async def botinvite(self, ctx):
        embed = discord.Embed(title=' ',
                              description=f'{ctx.author.mention} hier ist ein Invite Link zum Bot:\n`https:// discord.com / oauth2 / authorize?client_id = 790965419670241281 & scope = bot & permissions = 4294967287`',
                              color=0x4cd137)
        await ctx.send(embed=embed)

    @commands.command(name='ping', help='?ping [@user]')
    async def ping(self, ctx):
        embed = discord.Embed(title='',
                              description=f'**Du** hast einen Ping von **{round(self.bot.latency * 1000)}ms**',
                              color=0x4cd137)
        await ctx.send(embed=embed, delete_after=5)

    @commands.command()
    async def embed(self, ctx, *, text: str):
        embed = discord.Embed(title='',
                              description=text)
        await ctx.send(embed=embed)

    @commands.command(name='repeat', aliases=['mimic', 'copy', 'echo'])
    async def do_repeat(self, ctx, *, inp: str):
        await ctx.send(inp)

    @do_repeat.error
    async def do_repeat_handler(self, ctx, error):
        """A local Error Handler for our command do_repeat.
        This will only listen for errors in do_repeat.
        The global on_command_error will still be invoked after.
        """
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'inp':
                embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                      description=f'Nach **{ctx.command}** fehlt ein Argument!',
                                      color=0x4cd137)
                await ctx.send(embed=embed, delete_after=5)
                await asyncio.sleep(1)
                await ctx.message.delete()

def setup(bot):
    bot.add_cog(Utilities())
