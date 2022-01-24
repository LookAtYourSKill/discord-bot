import json
import discord
from discord.ext import commands
from googletrans import Translator


class uebersetzer(commands.Cog):
    def __init__(self, bot):
        self.text = None
        self.bot = bot

    @commands.command(name='translate', aliases=["tl", "Translate"])
    async def translate(self, ctx, language, *, destination):
        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Translator"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Translator) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            translator = Translator()
            translation = translator.translate(destination, dest=language)
            embed = discord.Embed(title=f"🇩🇪 Translator 🇬🇧",
                                  description=f'Translation from `{destination}` is `{translation.text}`',
                                  color=0x00ff00)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(uebersetzer(bot))
