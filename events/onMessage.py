import datetime
import json
import random
import discord
from discord.ext import commands


class onMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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
