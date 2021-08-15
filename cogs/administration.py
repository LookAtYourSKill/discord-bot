import asyncio

import discord
from discord.ext import commands


class Administration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="setstatus")
    @commands.is_owner()
    @commands.cooldown(rate=30, per=1)
    async def setstatus(self, ctx: commands.Context, *, text: str):
        await self.bot.change_presence(activity=discord.Game(name=text))
        embed = discord.Embed(title='<:open:869959941321011260> Erfolgreich',
                              description=f'Successfully changed bot status to **{text}**')
        await ctx.send(embed=embed, delete_after=5)
        await asyncio.sleep(1)
        await ctx.message.delete()

    @commands.command(name='load', aliases=['activate'])
    @commands.has_permissions(administrator=True)
    async def load(self, ctx, extension):
        self.bot.load_extension(f'cogs.{extension}')
        embed = discord.Embed(title='<:open:869959941321011260> Successfully',
                              description=f'**Loaded** Extension `{extension}`')
        await ctx.send(embed=embed, delete_after=5)
        await asyncio.sleep(1)
        await ctx.message.delete()

    @commands.command(name='unload', aliases=['deactivate'])
    @commands.has_permissions(administrator=True)
    async def unload(self, ctx, extension):
        self.bot.unload_extension(f'cogs.{extension}')
        embed = discord.Embed(title='<:open:869959941321011260> Successfully',
                              description=f'**Unloaded** Extension `{extension}`')
        await ctx.send(embed=embed, delete_after=5)
        await asyncio.sleep(1)
        await ctx.message.delete()

    @commands.command(name='reload', aliases=['rl'])
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx, extension):
        self.bot.unload_extension(f'cogs.{extension}')
        self.bot.load_extension(f'cogs.{extension}')
        embed = discord.Embed(title='<:open:869959941321011260> Successfully',
                              description=f'**Reloaded** Extension `{extension}`')
        await ctx.send(embed=embed, delete_after=5)
        await asyncio.sleep(1)
        await ctx.message.delete()

    @commands.command(name='lock')
    @commands.has_permissions(administrator=True)
    async def lockdown(self, ctx):
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

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unlock(self, ctx):
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

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def say(self, ctx, *, text):
        role = ctx.guild.default_role
        await ctx.send(f'{role} {text}')

def setup(bot):
    bot.add_cog(Administration(bot)
                )
