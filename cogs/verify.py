import json

import discord
from discord.ext import commands

with open('./config.json', 'r') as config_file:
    config = json.load(config_file)

class Verify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if 'verify' in message.content:
            await message.author.add_roles(message.author.guild.roles, config["verified_role"])
            embed = discord.Embed(title='Verified Successfully!')
            await message.send(embed=embed)

def setup(bot):
    bot.add_cog(Verify(bot))
