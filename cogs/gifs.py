import json
import discord
import random
from discord.ext import commands


class Gif(commands.Cog):

    """
    `They are gifs`
    """

    with open('utils/json/gifs.json') as gifs:
        gifData = json.load(gifs)

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hug')
    async def hug(self, ctx, member: discord.Member):
        """
        They are gifs
        """

        if member == ctx.author:
            embed = discord.Embed(title=f'<:close:864599591692009513> **ERROR**',
                                  description='Du kannst dich leider **nicht selbst umarmen!**')
            await ctx.send(embed=embed)
        else:
            gifs = self.gifData['hug']
            gif = random.choice(gifs)

            embed = discord.Embed(title=' ',
                                  description=f'{ctx.author.mention} just hugged {member.mention}!')
            embed.set_image(url=gif)
            await ctx.send(embed=embed)

    @commands.command(name='laugh')
    async def laugh(self, ctx):
        """
        They are gifs
        """

        gifs = self.gifData['laugh']
        gif = random.choice(gifs)

        embed = discord.Embed(title=' ',
                              description=f'{ctx.author.mention} lacht!')
        embed.set_image(url=gif)
        await ctx.send(embed=embed)

    @commands.command(name='punch')
    async def punch(self, ctx, member: discord.Member):
        """
        They are gifs
        """

        if member == ctx.author:
            embed = discord.Embed(title=f'<:close:864599591692009513> **ERROR**',
                                  description='Du kannst dich leider **nicht selbst schlagen!**')
            await ctx.send(embed=embed)
        else:
            gifs = self.gifData['punch']
            gif = random.choice(gifs)

            embed = discord.Embed(title=' ',
                                  description=f'{ctx.author.mention} just punched {member.mention}!')
            embed.set_image(url=gif)
            await ctx.send(embed=embed)

    @commands.command(name='cry')
    async def cry(self, ctx):
        """
        They are gifs
        """

        gifs = self.gifData['cry']
        gif = random.choice(gifs)

        embed = discord.Embed(title=' ',
                              description=f'{ctx.author.mention} weint!')
        embed.set_image(url=gif)
        await ctx.send(embed=embed)

    @commands.command(name='kiss')
    async def kiss(self, ctx, member: discord.Member):
        """
        They are gifs
        """

        if member == ctx.author:
            embed = discord.Embed(title=f'<:close:864599591692009513> **ERROR**',
                                  description='Du kannst dich leider **nicht selbst küssen!**')
            await ctx.send(embed=embed)
        else:
            gifs = self.gifData['kiss']
            gif = random.choice(gifs)

            embed = discord.Embed(title=' ',
                                  description=f'{ctx.author.mention} just kissed {member.mention}!')
            embed.set_image(url=gif)
            await ctx.send(embed=embed)

    @commands.command(name='cat')
    async def cat(self, ctx):
        """
        They are gifs
        """

        gifs = self.gifData['cat']
        gif = random.choice(gifs)

        embed = discord.Embed(title=' ',
                              description=' ')
        embed.set_image(url=gif)
        await ctx.send(embed=embed)

    @commands.command(name='rage')
    async def rage(self, ctx):
        """
        They are gifs
        """

        gifs = self.gifData['rage']
        gif = random.choice(gifs)

        embed = discord.Embed(title=' ',
                              description=f'{ctx.author.mention} ist richtig sauer!')
        embed.set_image(url=gif)
        await ctx.send(embed=embed)

    @commands.command(name='highfive')
    async def highfive(self, ctx, member: discord.Member):
        """
        They are gifs
        """

        if member == ctx.author:
            embed = discord.Embed(title=f'<:close:864599591692009513> **ERROR**',
                                  description='Du kannst dich leider **nicht selbst ein Highfive geben!**')
            await ctx.send(embed=embed)
        else:
            gifs = self.gifData['highfive']
            gif = random.choice(gifs)

            embed = discord.Embed(title=' ',
                                  description=f'{ctx.author.mention} just highfived with {member.mention}!')
            embed.set_image(url=gif)
            await ctx.send(embed=embed)

    @commands.command(name='handshake')
    async def handshake(self, ctx, member: discord.Member):
        """
        They are gifs
        """

        if member == ctx.author:
            embed = discord.Embed(title=f'<:close:864599591692009513> **ERROR**',
                                  description='Du kannst dich leider **nicht selbst die Hand geben!**')
            await ctx.send(embed=embed)
        else:
            gifs = self.gifData['handshake']
            gif = random.choice(gifs)

            embed = discord.Embed(title=' ',
                                  description=f'{ctx.author.mention} just handshaked with {member.mention}!')
            embed.set_image(url=gif)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Gif(bot)
                )