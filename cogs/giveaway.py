import asyncio
import random

import discord
from discord.ext import commands


class Giveaway(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def create(self, ctx, time=None, *, prize=None):
        if time == None:
            return await ctx.send("Include a time to make a giveaway!")
        elif prize == None:
            return await ctx.send("Include a prize to make a giveaway!")
        embed = discord.Embed(title=f"🎉{prize}🎉", description=f"{ctx.author.mention} is giving away 🎉**{prize}**🎉")
        time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}
        gawtime = int(time[0]) * time_convert[time[-1]]
        embed.set_footer(text=f"Giveawy ends in {time}")
        gaw_msg = await ctx.send(embed=embed)

        await gaw_msg.add_reaction("🎉")
        await asyncio.sleep(gawtime)

        new_gaw_msg = await ctx.channel.fetch_message(gaw_msg.id)

        users = await new_gaw_msg.reactions[0].users().flatten()

        users.pop(users.index(self.bot.user))

        winner = random.choice(users)
        await ctx.send(f"YAAY 🎉{winner.mention} has won **{prize}**🎉")

def setup(bot):
    bot.add_cog(Giveaway(bot))
