import asyncio
import random
import discord
from discord.ext import commands


class Timers(commands.Cog):
    """
    `A giveaway command`
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='create', aliases=['giveaway'])
    @commands.has_role('Giveaway')
    async def create(self, ctx, time=None, *, prize=None):
        """
        Creating a giveaway with a specific prize and time
        - **?create [`time`] [`prize`]**
        """

        if time is None:
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                  description='Du musst `eine Zeit` angeben!')
            return await ctx.send(embed=embed)

        elif prize is None:
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                  description='Du musst `ein Preis` angeben!')
            return await ctx.send(embed=embed)

        embed = discord.Embed(title=f"A Giveaway with a big prize appeared!",
                              description=f"{ctx.author.mention} is giving away 🎉**{prize}**🎉\n"
                                          f"**React** with 🎉 within `{time}` to participate at the Giveaway")

        time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400, "w": 604800}
        giveawaytime = int(time[:-1]) * time_convert[time[-1]]

        embed.set_footer(text=f"Giveaway ends in {time}")

        gaw_msg = await ctx.send(f'||@everyone||', embed=embed)

        await gaw_msg.add_reaction("🎉")
        await asyncio.sleep(giveawaytime)

        new_gaw_msg = await ctx.channel.fetch_message(gaw_msg.id)

        users = await new_gaw_msg.reactions[0].users().flatten()

        users.pop(users.index(self.bot.user))

        winner = random.choice(users)

        winner_embed = discord.Embed(title=f'{winner.name}',
                                     description=f'**You\'ve :tada: won {prize} :tada: **\n'
                                                 f'`Please contact the server team, to claim you prize` :thumbsup:',
                                     colour=discord.Color.greyple())
        await ctx.send(f'{winner.mention}', embed=winner_embed)

        winner_private_embed = discord.Embed(title=f'You\'ve :tada: won at the Giveaway :tada: on {ctx.guild.name}',
                                             description=f'**:tada: You\'ve won {prize} :tada:**\n'
                                                         f'`Please contact there a member from the server team to claim your prize` :thumbsup:')
        await winner.send(embed=winner_private_embed)

    @commands.command(name='reminder')
    async def reminder(self, ctx, zeit=None, *, reason='not set'):
        """
        Creates a reminder for a time you want
        - **?reminder [`time`] [`reason`]**
        """

        time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400, "w": 604800}
        remindertime = int(zeit[:-1]) * time_convert[zeit[-1]]

        if zeit is None:
            await ctx.send('Du musst eine Zeit angeben!')

        elif reason is None:
            embed = discord.Embed(title='Error',
                                  description='You did\'nt mentioned a reason.\n'
                                              'By standard it was set to \'not set\'!',
                                  color=discord.Color.red())
            await ctx.send(embed=embed)

            embed = discord.Embed(title='Reminder',
                                  description=f'You\'ll be reminded in `{zeit}` because of `not set`')
            await ctx.send(embed=embed)

            await asyncio.sleep(remindertime)
            await ctx.send(f'{ctx.author.mention} i should remind you now, ``reason = not set``')

        else:

            embed = discord.Embed(title='Reminder',
                                  description=f'You\'ll be reminded in `{zeit}` because of `{reason}`')
            await ctx.send(embed=embed)

            await asyncio.sleep(remindertime)
            await ctx.send(f'{ctx.author.mention} i should remind you now, ``reason = {reason}``')


def setup(bot):
    bot.add_cog(Timers(bot))
