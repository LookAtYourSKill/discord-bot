import discord
from discord.ext import commands


class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def poll(self, ctx, *, poll_question, ):
        embed = discord.Embed(title=f'🙋 New Poll 🙋',
                              description=f'The question of the poll is `{poll_question}`\n'
                                          f'**For yes vote with** :thumbsup: **if your answer should be no vote with** :thumbsdown:',
                              color=discord.Color.blurple())
        embed.set_footer(text=f'Poll from {ctx.author}')
        msg = await ctx.send('||@everyone||', embed=embed)

        await msg.add_reaction('👍')
        await msg.add_reaction('👎')


def setup(bot):
    bot.add_cog(Poll(bot))
