import datetime
import json
import random
import discord
from discord.ext import commands


class onMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    ###################################################AUTOMOD##############################################################
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
                channel = message.guild.get_channel(872945922743619657)
                embed = discord.Embed(title='',
                                      description='',
                                      color=discord.Color.random())
                embed.add_field(name='**Spam Detection Kick**',
                                value=f'Kicked User : `{message.author.name}#{message.author.discriminator}`\n'
                                      f'User ID : `{message.author.id}`\n'
                                      f'Gekickt von : `Ich seh dich#0264`')
                await channel.send(embed=embed)

        ##################################################BLACKLIST CHECK#######################################################

        with open("C:/Users/simon/PycharmProjects/Discord Bot/Discord Bot/utils/json/blacklist.json", 'r') as f:
            data = json.load(f)
        for bad_word in data["blacklist"]:
            # print(bad_word)
            if bad_word in message.content.lower():
                # print(message.content.lower())
                await message.delete()
                embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                      description='Deine Message `wurde gelöscht`, da du ein Wort `aus der Blacklist darin hattest!`\n**Bitte unterlasse dies!**')
                await message.channel.send(embed=embed, delete_after=5)

        ##################################################ANTI BAD FILE#########################################################

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

        ##################################################LINK PROTECTION#######################################################
        invLink = ['https://discord, https://discord.gg/']  # , 'http://, https://']

        for synonym in invLink:
            if synonym in message.content.lower():
                await message.delete()
                embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                      description='Hier sind **keine Links erlaubt**!')
                await message.channel.send(embed=embed, delete_after=5)

        ##################################################ONPING################################################################

        if message.content.startswith('<@!790965419670241281>'):
            embed = discord.Embed(title="Ping",
                                  description=f"Mein Prefix: **?**\n"
                                              f"Mit **?help** kannst du `dir alle Commands anschauen!`",
                                  color=0xff00c8)
            await message.author.send(embed=embed)
            await message.delete()

    @commands.Cog.listener()
    async def on_message_edit(self, old, new):
        if old.author.bot:
            return
        channel = self.bot.get_channel(872945922743619657)
        embed = discord.Embed(title="Message Edited",
                              description=f"{old.author.mention} has edited a message in {old.channel.mention} \n[Jump to the Message]({new.jump_url})",
                              color=discord.Color.random(),
                              timestamp=datetime.datetime.utcnow())
        embed.add_field(name="Old Message",
                        value=f'{old.content}',
                        # f'{(f"Embed oder Nachricht: {old.content}" if old.author.bot else f"{old.content}")}',
                        inline=False)
        embed.add_field(name="New Message",
                        value=f'{new.content}',
                        # f'{(f"Embed oder Nachricht: {new.content}" if new.author.bot else f"{new.content}")}',
                        inline=False)
        # embed.add_field(name="Channel", value=f'{old.channel.mention}', inline=False)
        # embed.add_field(name="Author", value=f'{old.author.mention}', inline=False)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot:
            return
        channel = self.bot.get_channel(872945922743619657)
        embed = discord.Embed(title="Message Deleted",
                              description=f'A message from {message.author.mention} was deleted in {message.channel.mention} ',
                              color=discord.Color.random(),
                              timestamp=datetime.datetime.utcnow())
        embed.add_field(name="Message",
                        value=f'{message.content}',
                        # f'{(f"Embed oder Nachricht: {message.content}" if message.author.bot else f"{message.content}")}',
                        inline=False)
        # embed.add_field(name="Author", value=f'{message.author.mention}', inline=False)
        # embed.add_field(name="Channel", value=f'{message.channel.mention}', inline=False)
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(onMessage(bot))
