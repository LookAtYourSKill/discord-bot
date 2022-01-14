import datetime
import json
import discord
from discord.ext import commands

with open('./etc/config.json', 'r') as config_file:
    config = json.load(config_file)


class onMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_edit(self, old, new):
        if old.author.bot:
            return
        channel = self.bot.get_channel(id=config['message_log_channel'])
        embed = discord.Embed(title="",
                              description=f"{old.author.mention} has edited a message in {old.channel.mention} \n[Jump to the Message]({new.jump_url})",
                              color=discord.Color.random(),
                              timestamp=datetime.datetime.utcnow())
        embed.add_field(name="Old Message",
                        value=f'{old.content}',
                        inline=False)
        embed.add_field(name="New Message",
                        value=f'{new.content}',
                        inline=False)
        embed.set_author(name='Message Edited', icon_url=old.author.avatar_url)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        message_attachments = message.attachments

        if message.author.bot:
            return

        elif len(message_attachments) > 0:
            for attachment in message_attachments:
                if attachment.filename.endswith('.png') or attachment.filename.endswith(
                        '.jpg') or attachment.filename.endswith('.jpeg'):
                    channel = self.bot.get_channel(id=config['message_log_channel'])
                    embed = discord.Embed(
                        description=f'A picture from {message.author.mention} was deleted in {message.channel.mention} ',
                        color=discord.Color.random(),
                        timestamp=datetime.datetime.utcnow())
                    embed.add_field(name="Picture",
                                    value=f'It was a picture...',
                                    inline=False)
                    embed.set_author(name='Picture Deleted', icon_url=message.author.avatar_url)
                    await channel.send(embed=embed)

        else:
            channel = self.bot.get_channel(id=config['message_log_channel'])
            embed = discord.Embed(
                description=f'A message from {message.author.mention} was deleted in {message.channel.mention} ',
                color=discord.Color.random(),
                timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Message",
                            value=f'{message.content}',
                            inline=False)
            embed.set_author(name='Message Deleted', icon_url=message.author.avatar_url)
            await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(onMessage(bot))
