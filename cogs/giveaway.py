import asyncio
import random
import discord
from discord.ext import commands


class Giveaway(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['gawrole', 'creategaw'])
    @commands.has_permissions(manage_channels=True)
    async def createGAWRole(self, ctx):
        guild = ctx.guild
        giveawayrole = await guild.create_role(name="Giveaway", color=discord.Color.green())
        embed = discord.Embed(title='<:open:869959941321011260>',
                              description=f'Die Rolle `**{giveawayrole}** wurde erfolgreich erstellt!`')
        await ctx.send(embed=embed)

    @commands.command(aliases=['giveaway'])
    @commands.has_role('Giveaway')
    async def create(self, ctx, time=None, *, prize=None):
        if time is None:
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                  description='Du musst `eine Zeit` angeben!')
            return await ctx.send(embed=embed)
        elif prize is None:
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                  description='Du musst `ein Preis` angeben!')
            return await ctx.send(embed=embed)
        embed = discord.Embed(title=f"🎉{prize}🎉", description=f"{ctx.author.mention} is giving away 🎉**{prize}**🎉")
        time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400, "w": 604800}
        giveawaytime = int(time[0]) * time_convert[time[-1]]
        embed.set_footer(text=f"Giveaway ends in {time}")
        gaw_msg = await ctx.send(embed=embed)

        await gaw_msg.add_reaction("🎉")
        await asyncio.sleep(giveawaytime)

        new_gaw_msg = await ctx.channel.fetch_message(gaw_msg.id)

        users = await new_gaw_msg.reactions[0].users().flatten()

        users.pop(users.index(self.bot.user))

        winner = random.choice(users)
        await ctx.send(f"YAAY 🎉{winner.mention} has won **{prize}**🎉")

def setup(bot):
    bot.add_cog(Giveaway(bot))
