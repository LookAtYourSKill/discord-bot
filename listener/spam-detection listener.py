import json

import discord
from discord.ext import commands

with open('./config.json', 'r') as config_file:
    config = json.load(config_file)

class spamDetection(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        counter = 0
        with open("C:/Users/simon/PycharmProjects/Discord Bot/Discord Bot/utils/json/spam-detection.json",
                  "r+") as file:
            for lines in file:
                if lines.strip("\n") == str(message.author.id):
                    counter += 1

            file.writelines(f"{str(message.author.id)}\n")
            if counter > 7:
                await message.guild.kick(message.author, reason="Spam Detection")
                channel = message.guild.get_channel(config['moderation_log_channel'])
                embed = discord.Embed(title='',
                                      description='',
                                      color=discord.Color.random())
                embed.add_field(name='**Spam Detection Kick**',
                                value=f'Kicked User : `{message.author.name}#{message.author.discriminator}`\n'
                                      f'User ID : `{message.author.id}`\n'
                                      f'Gekickt von : `Ich seh dich#0264`')
                await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(spamDetection(bot))
