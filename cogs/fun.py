import asyncio
import random
import discord
from discord.ext import commands


class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='8ball', aliases=['8Ball'])
    async def ball(self, ctx, question=None):
        if question is None:
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                  description='Bitte gebe `eine Frage` ein!')
        answers = ['Ja', 'Nein', 'Vielleicht']
        embed = discord.Embed(title='**8Ball**',
                              description=f'Deine Frage:'
                                          f'\n `{question}`'
                                          f'\n'
                                          f'Antwort: **{random.choice(answers)}**')
        await ctx.send(embed=embed)
        #FIX DAS MAN DIE KOMPLETTE FRAGE SIEHT (muss noch gemacht werden)

    @commands.command()
    @commands.cooldown(rate=2, per=1, type=commands.BucketType.member)
    async def slots(self, ctx):
        emojis = ["🍎", '🍉', '🍇', '🍓', '🍒']

        grabbed = ''
        for slot in emojis:
            grabbed += random.choice(emojis)

        winembed = discord.Embed(title='**Slots**',
                                 description=f'🎉Du hast in **Slots gewonnen**🎉')

        loseembed = discord.Embed(title='**Slots**',
                                  description='🥲Du hast leider nicht gewonnen🥲')

        if len(grabbed) == 1:
            await ctx.send(embed=winembed)
        else:
            await ctx.send(embed=loseembed)
        #FIX DAS MAN DAS WAS GEDREHT WURDE SIEHT ALSO DIE EMOJIS (muss noch gemacht werden)

    @commands.command(name='rolling', aliases=['roll'])
    async def würfel(self, ctx):
        num = random.randint(1, 6)
        embed = discord.Embed(title='',
                              description='Würfel rollt...')
        await ctx.send(embed=embed, delete_after=1)

        await asyncio.sleep(1)

        embed = discord.Embed(title='',
                              description=f'Der Würfel ist auf **der Nummer {num}** gelandet!')
        await ctx.send(embed=embed)

    @commands.command()
    async def rps(self, ctx, name=None):
        rps = ['Stein', 'Papier', 'Schere']
        if name is None:
            name = name.lower()
        if name is None or name not in rps:
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                  description='**Benutze bitte:** `stein`, `schere` oder `papier`!')
            await ctx.send(embed=embed)

        bot_move = random.choice(rps)
        embed = discord.Embed(title='',
                              description=f'Der Bot hat `{bot_move} gewählt`!')
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
                                      description=f'{ctx.author.mention} Ja  oke dikka `gewonnen`')
                await ctx.send(embed=embed)

        elif name == "Papier":
            if bot_move == "Schere":
                embed = discord.Embed(title='',
                                      description=f'{ctx.author.mention} Du hast einfach verloren')
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title='',
                                      description=f'{ctx.author.mention} Ja  oke dikka gewonnen')
                await ctx.send(embed=embed)

        elif name == "Schere":
            if bot_move == "Stein":
                embed = discord.Embed(title='',
                                      description=f'{ctx.author.mention} Du hast einfach verloren')
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title='',
                                      description=f'{ctx.author.mention} Ja  oke dikka gewonnen')
                await ctx.send(embed=embed)

        else:
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                  description='Unbekannter Fehler ist aufgetreten!')
            await ctx.send(embed=embed)
            #FIX WENN ES EIN FEHLER GIBT STOPPT ALLES! (Muss noch gemacht werden)


def setup(bot):
    bot.add_cog(fun(bot))
