import json
import discord
from discord.ext import commands


class Setup(commands.Cog):
    """
    `It should be a setup command but it isn't working`
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='setup', aliases=['setup_server'])
    @commands.has_permissions(administrator=True)
    async def setup_server(self, ctx):
        with open('C:/Users/simon/PycharmProjects/Discord Bot/Discord Bot/utils/json/on_guild.json', 'r') as f:
            data = json.load(f)
        member = ctx.author
        embed = discord.Embed(title='Setup',
                              description='Dies ist der Setup Command. Hier werden dir ein paar Fragen gestellt, wie dein Server eingestellt werden soll.\n'
                                          'Wenn du Fortfahren möchtest schreibe `ja` in den Chat!')
        embed.set_footer(text='Um den Command zu beenden schreibe einfach exit!')
        await ctx.send(embed=embed)
        while True:
            message = await self.bot.wait_for('message', check=lambda message: message.author == member)
            if 'ja' in message.content or 'Ja' in message.content:
                embed = discord.Embed(title='Setup',
                                      description='Du hast `Ja` gewählt.')
                embed.add_field(name='Log Channel',
                                value='Lege nun ein Message Log Channel fest.\n'
                                      'Dort werden `gelöscht und editierte` Nachrichten reingeschickt!')
                await ctx.send(embed=embed)

            else:
                embed = discord.Embed(title='Exit',
                                      description='Du hast den Command verlassen!')
                await ctx.send(embed=embed)
                break


def setup(bot):
    bot.add_cog(Setup(bot))
