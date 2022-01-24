import json
import discord
from discord.ext import commands


class Active_Check(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def activate(self, ctx, cog=None):
        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if not cog:
            if str(ctx.guild.id) not in data:
                new_checks = {
                    "Administration": "true",
                    "Automod": "true",
                    "Channel": "true",
                    "Fun": "true",
                    "Help": "true",
                    "Info": "true",
                    "Math": "true",
                    "Moderation": "true",
                    "Music": "true",
                    "Poll": "true",
                    "Roles": "true",
                    "Rules": "true",
                    "Setup": "true",
                    "Ticket": "true",
                    "Timers": "true",
                    "Translator": "true",
                    "Utilities": "true",
                    "Verify": "true"
                }
                data[str(ctx.guild.id)] = new_checks
                with open('utils/json/active_check.json', 'w') as f:
                    json.dump(data, f, indent=4)

                embed = discord.Embed(description=f'Der Server `{ctx.guild.name}` wurde **erfolgreich registriert!**',
                                      color=discord.Color.green())
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(description=f'Der Server `{ctx.guild.name}` ist **bereits registriert!**',
                                      color=discord.Color.green())
                await ctx.send(embed=embed)

        elif data[str(ctx.guild.id)][f"{cog}"] == 'true':
            embed = discord.Embed(description=f'Das `Modul {cog}` ist **bereits aktiviert!**',
                                  color=discord.Color.green())
            await ctx.send(embed=embed)

        elif data[str(ctx.guild.id)][f"{cog}"] == 'false':
            data[str(ctx.guild.id)][f"{cog}"] = 'true'
            with open('utils/json/active_check.json', 'w') as f:
                json.dump(data, f, indent=4)

            embed = discord.Embed(description=f'Das `Modul {cog}` **war deaktiviert** und wurde **nun aktiviert!**',
                                  color=discord.Color.green())
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(
                description=f'Dein Server scheint **nicht registriert zu sein!** **Registriere dein Server** bitte erst einmal **mit dem Befehl** `?activate`',
                color=discord.Color.red())
            await ctx.send(embed=embed)

    @commands.command()
    async def deactivate(self, ctx, cog):
        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if str(ctx.guild.id) not in data:
            embed = discord.Embed(
                description=f'Dein Server scheint **nicht registriert zu sein!** **Registriere dein Server** bitte erst einmal **mit dem Befehl** `?activate`',
                color=discord.Color.red())
            await ctx.send(embed=embed)

        elif data[str(ctx.guild.id)][f"{cog}"] == 'false':
            embed = discord.Embed(description=f'Das `Modul {cog}` ist **bereits deaktiviert!**',
                                  color=discord.Color.green())
            await ctx.send(embed=embed)

        elif data[str(ctx.guild.id)][f"{cog}"] == 'true':
            data[str(ctx.guild.id)][f"{cog}"] = 'false'
            with open('utils/json/active_check.json', 'w') as f:
                json.dump(data, f, indent=4)

            embed = discord.Embed(description=f'Das `Modul {cog}` **war aktiviert** und wurde **nun deaktiviert!**',
                                  color=discord.Color.green())
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(description=f'**Unbekannter Fehler!** Versuche es in ein paar Sekunden erneut',
                                  color=discord.Color.red())
            await ctx.send(embed=embed)

    @commands.command()
    async def check(self, ctx, cog):
        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if str(ctx.guild.id) not in data:
            embed = discord.Embed(
                description=f'Dein Server scheint **nicht registriert zu sein!** **Registriere dein Server** bitte erst einmal **mit dem Befehl** `?activate`',
                color=discord.Color.red())
            await ctx.send(embed=embed)

        elif data[str(ctx.guild.id)][f"{cog}"] == 'false':
            embed = discord.Embed(description=f'Das Modul `{cog}` ist **momentan deaktiviert!**',
                                  color=discord.Color.green())
            await ctx.send(embed=embed)

        elif data[str(ctx.guild.id)][f"{cog}"] == 'true':
            embed = discord.Embed(description=f'Das Modul `{cog}` ist **momentan aktiviert!**',
                                  color=discord.Color.green())
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(description=f'**Unbekannter Fehler!** Versuche es in ein paar Sekunden erneut',
                                  color=discord.Color.red())
            await ctx.send(embed=embed)

    @commands.command()
    async def check_all(self, ctx):
        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if str(ctx.guild.id) not in data:
            embed = discord.Embed(
                description=f'Dein Server scheint **nicht registriert zu sein!** **Registriere dein Server** bitte erst einmal **mit dem Befehl** `?activate`',
                color=discord.Color.red())
            await ctx.send(embed=embed)

        elif str(ctx.guild.id) in data:
            embed = discord.Embed(description=f'{data[str(ctx.guild.id)]}',
                                  color=discord.Color.green())
            await ctx.send(embed=embed)

        else:
            return


def setup(bot):
    bot.add_cog(Active_Check(bot))
