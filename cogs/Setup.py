import json
import discord
from discord.ext import commands


class server_setup(commands.Cog):
    """
    `A Server setup commands, to make the bot ready for your server!`
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setup(self, ctx):
        """
        The setup commands
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Setup"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Setup) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            pass

def setup(bot):
    bot.add_cog(server_setup(bot))
