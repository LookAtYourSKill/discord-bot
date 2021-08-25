import discord
from discord.ext import commands


class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def addition(self, ctx, first: int, second: int):
        result = first + second
        await ctx.send(f'You wanted me to add **{first}** and **{second}**.\n'
                       f'The Result is **{result}**')

    @commands.command()
    async def substraction(self, ctx, first: int, second: int, third: int):
        result = first - second - third
        await ctx.send(f'You wanted me to subtract **{first}** and **{second}** and **{third}**.\n'
                       f'The Result is **{result}**')


def setup(bot):
    bot.add_cog(Math(bot))
