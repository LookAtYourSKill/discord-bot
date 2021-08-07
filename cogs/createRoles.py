import asyncio

import discord
from discord.ext import commands


class createRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['createGAW'])
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

    @commands.command(aliases=['createMute'])
    @commands.has_permissions(manage_roles=True)
    async def muterole(self, ctx):
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        if not role:
            try:
                muterole = await ctx.guild.create_role(name='Muted', color=discord.Color.darker_gray())
                embed = discord.Embed(title='<:open:869959941321011260> Successfull',
                                      description=f'Die Rolle **{muterole}** wurde erstellt!')
                await ctx.send(embed=embed, delete_after=5)
                await asyncio.sleep(1)
                await ctx.message.delete()
                for channel in ctx.guild.channels():
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

def setup(bot):
    bot.add_cog(createRoles(bot))
