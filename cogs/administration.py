import asyncio

import discord
from discord.ext import commands


class Administration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="setstatus")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(rate=1, per=30)
    async def setstatus(self, ctx: commands.Context, *, text: str):
        await self.bot.change_presence(activity=discord.Game(name=text))
        embed = discord.Embed(title='<:open:869959941321011260> Erfolgreich',
                              description=f'Successfully changed bot status to **{text}**')
        await ctx.send(embed=embed)

    @commands.command(name='load', aliases=['activate'])
    @commands.has_permissions(administrator=True)
    async def load(self, ctx, extension):
        self.bot.load_extension(f'cogs.{extension}')
        embed = discord.Embed(title='<:open:869959941321011260> Successfully',
                              description=f'**Loaded** Extension `{extension}`')
        await ctx.send(embed=embed)

    @commands.command(name='unload', aliases=['deactivate'])
    @commands.has_permissions(administrator=True)
    async def unload(self, ctx, extension):
        self.bot.unload_extension(f'cogs.{extension}')
        embed = discord.Embed(title='<:open:869959941321011260> Successfully',
                              description=f'**Unloaded** Extension `{extension}`')
        await ctx.send(embed=embed)

    @commands.command(name='reload', aliases=['rl'])
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx, extension):
        self.bot.unload_extension(f'cogs.{extension}')
        self.bot.load_extension(f'cogs.{extension}')
        embed = discord.Embed(title='<:open:869959941321011260> Successfully',
                              description=f'**Reloaded** Extension `{extension}`')
        await ctx.send(embed=embed)

    @commands.command(aliases=['addrole'])
    @commands.has_permissions(manage_roles=True)
    async def create_role(self, ctx, *, role_name: str, color: discord.Color = discord.Color.random()):
        await ctx.guild.create_role(role_name=role_name, color=color)
        embed = discord.Embed(title='<:open:869959941321011260> Successfully',
                              description=f'Die Rolle **{role_name}** wurde erstellt!')
        await ctx.send(embed=embed)

    @commands.command(aliases=['delrole', 'rmrole'])
    @commands.has_permissions(manage_roles=True)
    async def delete_role(self, ctx, *, role_name):
        role = discord.utils.get(ctx.guild.roles, name=role_name)
        if role:
            try:
                await role.delete()
                embed = discord.Embed(title='<:open:869959941321011260> Successfully',
                                      description=f'Die Rolle **{role_name}** wurde gelöscht!')
                await ctx.send(embed=embed, delete_after=5)
                await asyncio.sleep(1)
                await ctx.message.delete()
            except discord.Forbidden:
                pass
        else:
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                  description=f'Die Rolle **existiert nicht**!')
            await ctx.send(embed=embed, delete_after=5)
            await asyncio.sleep(1)
            await ctx.message.delete()

def setup(bot):
    bot.add_cog(Administration(bot)
                )