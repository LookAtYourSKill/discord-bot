import asyncio
import json

import discord
from discord.ext import commands


class onMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

#################################################AUTOMOD################################################################
    @commands.Cog.listener()
    async def on_message(self, message):
        counter = 0
        with open("./utils/json_files/spam-detection.json",
                  "r+") as file:
            for lines in file:
                if lines.strip("\n") == str(message.author.id):
                    counter += 1

            file.writelines(f"{str(message.author.id)}\n")
            if counter > 10:
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

        #with open("./utils/json_files/blacklist.json", 'r') as file:
        #    json.load(file)
        #    blacklist = '.utils/json_files/blacklist.json'
        #message_content = message.content.strip().lower()
        #for bad_word in blacklist:
        #    if bad_word in message_content:
        #        await message.send(f"{message.author.mention}, your message has been deleted.")
        #        await message.delete()

        message_attachments = message.attachments
        if len(message_attachments) > 0:
            for attachment in message_attachments:
                if attachment.filename.endswith(".dll"):
                    await message.delete()
                    embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                          description='Hier sind keine Datein, mit dem **Dateinamen Ende \'dll\' erlaubt**')
                    await message.channel.send(embed=embed, delete_after=5)
                elif attachment.filename.endswith('.exe'):
                    await message.delete()
                    embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                          description='Hier sind keine Datein, mit dem **Dateinamen Ende \'exe\' erlaubt**')
                    await message.channel.send(embed=embed, delete_after=5)
                elif attachment.filename.endswith('.bat'):
                    await message.delete()
                    embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                          description='Hier sind keine Datein, mit dem **Dateinamen Ende \'bat\' erlaubt**')
                    await message.channel.send(embed=embed, delete_after=5)
                else:
                    break
##################################################ONPING################################################################
        if message.content.startswith('<@!790965419670241281>'):
            embed = discord.Embed(title="Ping",
                                  description=f"Mein Prefix: **?**\n"
                                              f"Mit **?help** kannst du `dir alle Commands anschauen!`",
                                  color=0xff00c8)
            await message.author.send(embed=embed)


def setup(bot):
    bot.add_cog(onMessage(bot))
