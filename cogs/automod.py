import asyncio

import discord
from discord.ext import commands


class Automod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    with open('C:/Users/simon/PycharmProjects/pythonProject/Discord Bot/utils/json_files/spam-detection.json', 'r+') as file:
        file.truncate(0)

    @commands.Cog.listener()
    async def on_message(self, message):
        counter = 0
        with open("C:/Users/simon/PycharmProjects/pythonProject/Discord Bot/utils/json_files/spam-detection.json", "r+") as file:
            for lines in file:
                if lines.strip("\n") == str(message.author.id):
                    counter += 1

            file.writelines(f"{str(message.author.id)}\n")
            if counter > 5:
                await message.guild.kick(message.author, reason="spam")
                channel =

def setup(bot):
    bot.add_cog(Automod(bot))
