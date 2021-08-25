import discord
from discord.ext import commands


class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='addition', aliases=['add', 'plus'])
    async def addition(self, ctx, first: int, second: int):
        result = first + second
        embed = discord.Embed(title='**Math Addition**',
                              description=f'The result from **{first}** and **{second}** is **{result}**!')
        await ctx.send(embed=embed)

    @commands.command(name='subtract', aliases=['sub', 'minus'])
    async def subtraction(self, ctx, first: int, second: int):
        result = first - second
        embed = discord.Embed(title='**Math Subtract**',
                              description=f'The result from **{first}** and **{second}** is **{result}**!')
        await ctx.send(embed=embed)

    @commands.command(name='multiplicate', aliases=['mal'])
    async def multiplication(self, ctx, first: int, second: int):
        result = first * second
        embed = discord.Embed(title='**Math Multiplicate**',
                              description=f'The result from **{first}** and **{second}** is **{result}**!')
        await ctx.send(embed=embed)

    @commands.command(name='divide', aliases=['geteilt'])
    async def dividation(self, ctx, first: int, second: int):
        result = first / second
        embed = discord.Embed(title='**Math Divide**',
                              description=f'The result from **{first}** and **{second}** is **{result}**!')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Math(bot))
