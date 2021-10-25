import asyncio

import discord
from discord.ext import commands


class createRoles(commands.Cog):
    """
    `All roles you need for the bot`
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='gawrole', aliases=['createGAW'])
    @commands.has_permissions(manage_roles=True)
    async def gawrole(self, ctx):
        role = discord.utils.get(ctx.guild.roles, name='Giveaway')
        if not role:
            try:
                giveawayrole = await ctx.guild.create_role(name='Giveaway', color=discord.Color.green())
                embed = discord.Embed(title='<:open:869959941321011260> Successfully',
                                      description=f'Die Rolle **{giveawayrole}** wurde erstellt!')
                await ctx.send(embed=embed, delete_after=5)
                await asyncio.sleep(1)
                await ctx.message.delete()
            except discord.Forbidden:
                pass
        else:
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                  description=f'Die Rolle **existiert bereits**!')
            await ctx.send(embed=embed, delete_after=5)
            await asyncio.sleep(1)
            await ctx.message.delete()

    @commands.command(name='muterole', aliases=['createMute'])
    @commands.has_permissions(manage_roles=True)
    async def muterole(self, ctx):
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        if not role:
            try:
                muterole = await ctx.guild.create_role(name='Muted', color=discord.Color.darker_gray())
                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                      description=f'Die Rolle **{muterole}** wurde erstellt!')
                await ctx.send(embed=embed, delete_after=5)
                await asyncio.sleep(1)
                await ctx.message.delete()
                for channel in ctx.guild.channels:
                    await channel.set_permissions(muterole,
                                                  speak=False,
                                                  send_messages=False,
                                                  read_messages=True,
                                                  read_message_history=True,
                                                  )
            except discord.Forbidden:
                pass
        else:
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                  description=f'Die Rolle **existiert bereits**!')
            await ctx.send(embed=embed, delete_after=5)
            await asyncio.sleep(1)
            await ctx.message.delete()

    @commands.command(name='giverole')
    @commands.has_permissions(manage_roles=True)
    async def _give_role(self, ctx, user: discord.Member, role: discord.Role):
        try:
            await user.add_roles(role, reason=None)
            embed = discord.Embed(title='',
                                  description=f'Dem User **{user}** wurde die Rolle `{role} gegeben!`')
            await ctx.send(embed=embed, delete_after=5)
            await asyncio.sleep(1)
            await ctx.message.delete()
        except:
            pass

    @commands.command(name='removerole', aliases=['rmrole'])
    @commands.has_permissions(manage_roles=True)
    async def remove_role(self, ctx, user: discord.Member, role: discord.Role):
        try:
            await user.remove_roles(role, reason=None)
            embed = discord.Embed(title='',
                                  description=f'Dem User **{user}** wurde die Rolle `{role} entfernt!`')
            await ctx.send(embed=embed, delete_after=5)
            await asyncio.sleep(1)
            await ctx.message.delete()
        except discord.Forbidden:
            pass

    @commands.command(aliases=['createrole'])
    @commands.has_permissions(manage_roles=True)
    async def create_role(self, ctx, *, role_name, color: discord.Color = discord.Color.random()):
        await ctx.guild.create_role(name=role_name, color=color)
        embed = discord.Embed(title='<:open:869959941321011260> Successfully',
                              description=f'Die Rolle **{role_name}** wurde erstellt!')
        await ctx.send(embed=embed, delete_after=5)
        await asyncio.sleep(1)
        await ctx.message.delete()

    @commands.command(aliases=['delrole'])
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
    bot.add_cog(createRoles(bot))
