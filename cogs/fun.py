import asyncio
import random
import discord
from discord.ext import commands


class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='8ball', aliases=['8Ball'])
    async def ball(self, ctx, *, question):
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
    async def würfel(self, ctx):
        num = random.randint(1, 6)
        embed = discord.Embed(title='',
                              description='Würfel rollt...')
        würfel_message = await ctx.send(embed=embed)

        await asyncio.sleep(1)

        embed = discord.Embed(title='',
                              description=f'Der Würfel ist auf **der Nummer {num}** gelandet!')
        await würfel_message.edit(embed=embed)

    @commands.command(aliases=['rockpapersissors', 'scheresteinpapier'])
    async def rps(self, ctx, name=None):
        rps = ['Stein', 'Papier', 'Schere']
        if name is None or name not in rps:
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                  description='**Benutze bitte:** `Stein`, `Schere` oder `Papier`!')
            await ctx.send(embed=embed)

        else:
            bot_move = random.choice(rps)
            embed = discord.Embed(title='',
                                  description=f'**Der Bot** hat `{bot_move} gewählt`!\n'
                                              f'**Du** hast `{name} gewählt`!')
            await ctx.send(embed=embed)

            if bot_move == name:
                embed = discord.Embed(title='',
                                      description=f'{ctx.author.mention} Das ist ein `unentschieden`!')
                await ctx.send(embed=embed)

            elif name == "Stein":
                if bot_move == "Papier":
                    embed = discord.Embed(title='',
                                          description=f'{ctx.author.mention} Du hast einfach `verloren`')
                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(title='',
                                          description=f'{ctx.author.mention} Ja oke dikka `gewonnen`')
                    await ctx.send(embed=embed)

            elif name == "Papier":
                if bot_move == "Schere":
                    embed = discord.Embed(title='',
                                          description=f'{ctx.author.mention} Du hast einfach verloren')
                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(title='',
                                          description=f'{ctx.author.mention} Ja oke dikka gewonnen')
                    await ctx.send(embed=embed)

            elif name == "Schere":
                if bot_move == "Stein":
                    embed = discord.Embed(title='',
                                          description=f'{ctx.author.mention} Du hast einfach verloren')
                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(title='',
                                          description=f'{ctx.author.mention} Ja oke gewonnen')
                    await ctx.send(embed=embed)

            else:
                embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                      description='Unbekannter Fehler ist aufgetreten!')
                await ctx.send(embed=embed)

    @commands.command()
    async def num_game(self, ctx):
        ran_number = random.randint(1, 10)
        member = ctx.author
        embed = discord.Embed(title='Numgame',
                              description='Choose a number between 1-10')
        await ctx.send(embed=embed)
        while True:
            message = await self.bot.wait_for('int', check=lambda message: message.author == member)
            if int(ran_number) in message.content:
                await ctx.send(f'You guessed it! It was {ran_number}')
            else:
                await ctx.send('Nope')

    @commands.command()
    async def simp(self, ctx):
        ran_percent = random.randint(1, 100)
        embed = discord.Embed(title='Simp Test',
                              description=f'Simp Rate: **{ran_percent}%**',
                              color=discord.colour.Color.blurple())
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/810855960133894154/871855679768514560/pny0r8v4c0m41.png')
        await ctx.send(embed=embed)

    @commands.command()
    async def sus(self, ctx):
        ran_percent = random.randint(1, 100)
        embed = discord.Embed(title='Sus Test',
                              description=f'Sus Rate: **{ran_percent}%**',
                              color=discord.colour.Color.red())
        embed.set_thumbnail(url='https://static.wikia.nocookie.net/0974aaa7-7e44-4887-997b-2bf06efb6297/scale-to-width/755')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(fun(bot)
                )
