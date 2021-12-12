import datetime
import json
import discord
from discord.ext import commands

with open('./config.json', 'r') as config_file:
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
        if message.author.bot:
            return
        channel = self.bot.get_channel(id=config['message_log_channel'])
        embed = discord.Embed(title="",
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
