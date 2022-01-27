import json
import discord
from discord.ext import commands


class math(commands.Cog):
    """
    `You could do it by yourself but it is easier with this`
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='addition', aliases=['add', 'plus'])
    async def addition(self, ctx, first: int, second: int):
        """
        Add two specific numbers together
        - **?add [`first`] [`second`]**
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Math"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Math) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#8691)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            result = first + second
            embed = discord.Embed(title='**Math Addition**',
                                  description=f'The result from **{first}** and **{second}** is **{result}**!')
            await ctx.send(embed=embed)

    @commands.command(name='subtract', aliases=['sub', 'minus'])
    async def subtraction(self, ctx, first: int, second: int):
        """
        Subtract two specific numbers from them
        - **?minus [`first`] [`second`]**
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Math"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Math) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#8691)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            result = first - second
            embed = discord.Embed(title='**Math Subtract**',
                                  description=f'The result from **{first}** and **{second}** is **{result}**!')
            await ctx.send(embed=embed)

    @commands.command(name='multiplicate', aliases=['mal'])
    async def multiplication(self, ctx, first: int, second: int):
        """
        Multiply two number with each other
        - **?multiplicate [`first`] [`second`]**
        """
        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Math"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Math) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#8691)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            result = first * second
            embed = discord.Embed(title='**Math Multiplicate**',
                                  description=f'The result from **{first}** and **{second}** is **{result}**!')
            await ctx.send(embed=embed)

    @commands.command(name='divide', aliases=['geteilt'])
    async def dividation(self, ctx, first: int, second: int):
        """
        Divide two numbers
        - **?divide [`first`] [`second`]**
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Math"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Math) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#8691)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            result = first / second
            embed = discord.Embed(title='**Math Divide**',
                                  description=f'The result from **{first}** and **{second}** is **{result}**!')
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(math(bot))
