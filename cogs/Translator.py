import discord
from discord.ext import commands
from googletrans import Translator

class uebersetzer(commands.Cog):
    def __init__(self, bot):
        self.text = None
        self.bot = bot

    @commands.command(name='translate', aliases=["tl", "Translate"])
    async def translate(self, ctx, language, *, destination):
        translator = Translator()
        translation = translator.translate(destination, dest=language)
        embed = discord.Embed(title=f"🇩🇪 Translator 🇬🇧",
                              description=f'Translation from `{destination}` is {translation.text}',
                              color=0x00ff00)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(uebersetzer(bot))
