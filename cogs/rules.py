import discord
from discord.ext import commands


class rules(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='rules')
    @commands.has_permissions(manage_channels=True)
    async def _rules(self, ctx):
        embed = discord.Embed(title='',
                              description='```py\n'
                                          'REGELWERK 📜\n'
                                          '\n'
                                          'Die Regeln gelten für dein ganzes Erscheinen, also Chatnachrichten, Name, Avatar, Spieleanzeige oder anderes.\n'
                                          '\n'
                                          '§1 Grundregel\n'
                                          '» Seid gegenüber jeder Person respektvoll. Jede Art von beleidigenden, sexistischen, radikalen, verachtenden, ethisch inkorrekten, NSFW, potentiell gefährlichen und durch das Gesetz verboten Aussagen oder Dateien sind verboten.\n'
                                          '\n'
                                          '§2 Werbung\n'
                                          '» Jegliche Form von Werbung ist strengstens untersagt.\n'
                                          '» Discord-Invites werden ausnahmslos gebannt.\n'
                                          '\n'
                                          '§3 Name und Avatar\n'
                                          '» Es darf niemand kopiert werden. Name und Avatar sollten möglichst einzigartig sein.\n'
                                          '\n'
                                          '§4 Verhalten in den Channeln\n'
                                          '» Spam und Capslock vermeiden. Channel-Thema beachten.\n'
                                          '» Keine Stimmverzerrer oder andere laute/störende Geräusche.\n'
                                          '\n'
                                          '§5 Datenschutz\n'
                                          '» Keine Aufnahmen oder ähnliches ohne Zustimmung aller zu hörenden/sehenden Personen.\n'
                                          '» Keine fremden Daten veröffentlichen.\n'
                                          '» Private Missverständnisse privat klären\n'
                                          '\n'
                                          '§6 Verkäufe und Geschäfte\n'
                                          '» Verkäufe und Geschäfte sind hier verboten. (Einen Fortnite-Account zu verkaufen ist gegen die Epic Games Richtlinien).\n'
                                          '\n'
                                          '§7 Sonstiges\n'
                                          '» Das Serverteam muss sich gegenüber den Usern nicht rechtfertigen.\n'
                                          '» Jeder Regelbruch wird je nach Vergehen bestraft.\n'
                                          '» Der User ist für seinen Account verantwortlich.\n'
                                          '\n'
                                          'Du stimmst beim Betreten des Servers automatisch den obenstehenden Regeln zu.\n'
                                          '\n'
                                          'Unwissenheit schützt  nicht vor Strafe```')
        message = await ctx.send(embed=embed)
        await message.add_reaction('<:open:869959941321011260>')
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(rules(bot))
