import json

import discord
from discord.ext import commands


class on_guild(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open('C:/Users/simon/PycharmProjects/Discord Bot/Discord Bot/utils/json/on_guild.json', 'r+') as f:
            data = json.load(f)

        new_server = {
            "servername": str(guild.name),
            "warns": {

            }
        }
        data[str(guild.id)] = new_server
        with open('C:/Users/simon/PycharmProjects/Discord Bot/Discord Bot/utils/json/on_guild.json', 'w') as f:
            json.dump(data, f, indent=4)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open('C:/Users/simon/PycharmProjects/Discord Bot/Discord Bot/utils/json/on_guild.json', 'r') as f:
            data = json.load(f)

        old_server = {
            "servername": str(guild.name),
            "warns": {

            }
        }
        data[str(guild.id)] = old_server
        with open('C:/Users/simon/PycharmProjects/Discord Bot/Discord Bot/utils/json/on_guild.json', 'w') as f:
            json.dump(data, f, indent=4)


def setup(bot):
    bot.add_cog(on_guild(bot))
