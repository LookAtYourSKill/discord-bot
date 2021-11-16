import discord
from discord.ext import commands
import asyncio


class AFK(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='afk')
    async def afk(self, ctx, mins, reason=None):
        current_nick = ctx.author.nick
        await ctx.send(f"{ctx.author.mention} ist für {mins} Afk, wegen {reason}")
        await ctx.author.edit(nick=f"[AFK] {ctx.author.mention}")

        counter = 0
        while counter <= int(mins):
            counter += 1
            await asyncio.sleep(60)

            if counter == int(mins):
                await ctx.author.edit(nick=current_nick)
                await ctx.send(f"{ctx.authot.mention} ist nicht mehr Afk")
                break


def setup(bot):
    bot.add_cog(AFK(bot))
