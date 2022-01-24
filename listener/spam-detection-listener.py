import json
import discord
from discord.ext import commands


class spamDetection(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        with open('utils/json/on_guild.json', 'r') as f:
            guild_data = json.load(f)

        if message.author.bot:
            return
        counter = 0
        with open("utils/json/spam-detection.json", "r+") as file:
            for lines in file:
                if lines.strip("\n") == str(message.author.id):
                    counter += 1

            file.writelines(f"{str(message.author.id)}\n")
            if counter > 100:
                await message.guild.kick(message.author, reason="Spam Detection")
                channel = message.guild.get_channel(guild_data[str(message.author.guild.id)]['moderation_log_channel'])
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
