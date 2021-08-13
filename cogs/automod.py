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
                channel = message.guild.get_channel(872945922743619657)
                embed = discord.Embed(title='',
                                      description='',
                                      color=discord.Color.random())
                embed.add_field(name='**Spam Detection Kick**',
                                value=f'Kicked User : `{message.author.name}#{message.author.discriminator}`\n'
                                      f'User ID : `{message.author.id}`\n'
                                      f'Gekickt von : `Ich seh dich#0264`')
                await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Automod(bot))
