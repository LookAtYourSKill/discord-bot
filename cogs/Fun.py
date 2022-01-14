import asyncio
import random
import discord
from discord.ext import commands


class fun(commands.Cog):
    """
    `A lot of funny commands`
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='8ball', aliases=['8Ball'])
    async def ball(self, ctx, *, question):
        """
        Ask the bot a question!
        - **?8ball [`question`]**
        """

        if question is None:
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                  description='Bitte gebe `eine Frage` ein!')
            await ctx.send(embed=embed)

        answers = ['Ja',
                   'Nein',
                   'Vielleicht']
        embed = discord.Embed(title='**8Ball**',
                              description=f'Deine Frage:'
                                          f'\n `{question}`'
                                          f'\n'
                                          f'Antwort: **{random.choice(answers)}**')
        await ctx.send(embed=embed)

    @commands.command(aliases=['slot'])
    @commands.cooldown(rate=2, per=1)
    async def slots(self, ctx):
        """
        Play slots but without a prize
        - **?slots**
        """

        emojis = ["🍎", '🍇', '🍒', '🍉', '🍓']

        grabbed = ''
        for _emoji in range(3):
            grabbed += random.choice(emojis)

        winembed = discord.Embed(title=' ',
                                 description=f'🎉Du hast in **Slots gewonnen**🎉!\nDu hast {grabbed} gezogen!')

        loseembed = discord.Embed(title=' ',
                                  description=f'Du hast **leider nicht gewonnen**!\nDu hast {grabbed} gezogen!')

        if grabbed == '🍎🍎🍎' or grabbed == '🍇🍇🍇' or grabbed == '🍒🍒🍒' or grabbed == '🍉🍉🍉' or grabbed == '🍓🍓🍓':
            await ctx.send(embed=winembed)
        else:
            await ctx.send(embed=loseembed)

    @commands.command(name='rolling', aliases=['roll'])
    async def dice(self, ctx):
        """
        Roll a dice
        - **?dice**
        """

        num = random.randint(1, 6)
        embed = discord.Embed(title='',
                              description='Würfel rollt...')
        dice_message = await ctx.send(embed=embed)

        await asyncio.sleep(1)

        embed = discord.Embed(title='',
                              description=f'Der Würfel ist auf **der Nummer {num}** gelandet!')
        await dice_message.edit(embed=embed)

    @commands.command(name='rps', aliases=['rockpapersissors', 'scheresteinpapier'])
    async def rps(self, ctx, name=None):
        """
        Play rock, paper, scissors against the bot!
        - **rps [`Stein, Papier, Schere`]**
        """

        rps = ['rock', 'paper', 'scissors']
        if name is None or name not in rps:
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                  description='**Please use:** `rock`, `paper` or `scissors`!')
            await ctx.send(embed=embed)

        else:
            bot_move = random.choice(rps)
            embed = discord.Embed(title='',
                                  description=f'**The Bot** chose `{bot_move}`!\n'
                                              f'**You** chose `{name}`!')
            message = await ctx.send(embed=embed)
            await asyncio.sleep(5)

            if bot_move == name:
                embed = discord.Embed(title='',
                                      description=f'{ctx.author.mention} Das ist ein `unentschieden`!')
                await message.edit(embed=embed)

            elif name == "rock":
                if bot_move == "paper":
                    embed = discord.Embed(title='',
                                          description=f'{ctx.author.mention} Du hast `verloren`')
                    await message.edit(embed=embed)
                else:
                    embed = discord.Embed(title='',
                                          description=f'{ctx.author.mention} Du hast `gewonnen`')
                    await message.edit(embed=embed)

            elif name == "paper":
                if bot_move == "scissors":
                    embed = discord.Embed(title='',
                                          description=f'{ctx.author.mention} Du hast `verloren`')
                    await message.edit(embed=embed)
                else:
                    embed = discord.Embed(title='',
                                          description=f'{ctx.author.mention} Du hast `gewonnen`')
                    await message.edit(embed=embed)

            elif name == "scissors":
                if bot_move == "rock":
                    embed = discord.Embed(title='',
                                          description=f'{ctx.author.mention} Du hast `verloren`')
                    await message.edit(embed=embed)
                else:
                    embed = discord.Embed(title='',
                                          description=f'{ctx.author.mention} Du hast `gewonnen`')
                    await message.edit(embed=embed)

            else:
                embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                      description='Unbekannter Fehler ist aufgetreten!')
                await message.edit(embed=embed)

    @commands.command(name='num_game', aliases=['numgame'])
    async def num_game(self, ctx):
        """
        Guess a random number between 1 and 10
        - **?numgame**
        """

        def check(m):
            return m.author == ctx.author

        ran_number = random.randint(1, 10)
        embed = discord.Embed(title='Numgame',
                              description='Choose a number between 1-10', colour=discord.Color.orange())
        await ctx.send(embed=embed)
        while True:
            message = await self.bot.wait_for('message', check=check)
            guess = int(message.content)
            if guess > ran_number:
                embed = discord.Embed(
                    description=f'The Number **is a little bit smaller** than you thought... ``The number was {ran_number}``\n'
                                f'Wish you more luck next time :thumbsup:', colour=discord.Color.blue())
                await ctx.send(embed=embed)
            elif guess < ran_number:
                embed = discord.Embed(
                    description=f'The Number **is a little bit bigger** than you thought... ``The number was {ran_number}``\n'
                                f'Wish you more luck next time :thumbsup:', colour=discord.Color.red())
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    description=f'**The Number is exactly what you thought...** ``The number was {ran_number}`` :tada:\n'
                                f'Hopefully you have the same luck next time :thumbsup:', colour=discord.Color.green())
                await ctx.send(embed=embed)

    @commands.command(name='simp', aliases=['simprate'])
    async def simp(self, ctx):
        """
        Just a random test if you are a simp or not
        - **?simp**
        """

        ran_percent = random.randint(1, 100)
        embed = discord.Embed(title='Simp Test',
                              description=f'Simp Rate: **{ran_percent}%**',
                              color=discord.colour.Color.blurple())
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/810855960133894154/871855679768514560/pny0r8v4c0m41.png')
        await ctx.send(embed=embed)

    @commands.command(name='sus', alises=['susrate'])
    async def sus(self, ctx):
        """
        Just a simply test if you are sus or not
        - **?sus**
        """

        ran_percent = random.randint(1, 100)
        embed = discord.Embed(title='Sus Test',
                              description=f'Sus Rate: **{ran_percent}%**',
                              color=discord.colour.Color.red())
        embed.set_thumbnail(
            url='https://static.wikia.nocookie.net/0974aaa7-7e44-4887-997b-2bf06efb6297/scale-to-width/755')
        await ctx.send(embed=embed)

    @commands.command(name='alzheimer', alises=['alz'])
    async def alzheimer(self, ctx):
        """
        Just a simply test if you are sus or not
        - **?sus**
        """

        if ctx.author.id == 427408295427440652:
            embed = discord.Embed(title='Alzheimer Test',
                                  description=f'Alzheimer liegt **ganz klar** bei: **100%**',
                                  color=discord.colour.Color.red())
            await ctx.send(embed=embed)
        else:
            ran_percent = random.randint(1, 100)
            embed = discord.Embed(title='Alzheimer Test',
                                  description=f'Alzheimer liegt bei: **{ran_percent}%**',
                                  color=discord.colour.Color.red())
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(fun(bot))
