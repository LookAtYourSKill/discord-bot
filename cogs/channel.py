import asyncio

import discord
from discord.ext import commands

class Channel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def delete_channel(self, ctx, channel: discord.TextChannel):

        if channel is not None:
            await channel.delete()
            await ctx.send(f"Der Channel ``{channel.name}`` wurde **Erfolgreich gelöscht!**", delete_after=5)
            await ctx.message.delete()

        elif not channel:
            channel = ctx.channel
            await ctx.channel.delete()
            await ctx.send(f"Der Channel ``{channel.name}`` wurde **Erfolgreich gelöscht!**", delete_after=5)
            await ctx.message.delete()

        else:
            await ctx.send(f'No channel named, "{channel}", was found', delete_after=5)
            await ctx.message.delete()

    @commands.command()
    async def create_channel(self, ctx, channel_name):
        guild = ctx.message.guild

        if not channel_name:
            await ctx.send('Du hast **keinen Channel Namen angegeben!**', delete_after=5)
            await ctx.message.delete()

        if channel_name is not None:
            channel = await guild.create_text_channel(f'{channel_name}')
            await ctx.send(f'Der Channel {channel.mention} wurde **Erfolgreich erstellt!**', delete_after=5)
            await ctx.message.delete()

        else:
            await ctx.send(f'Irgendetwas ist schiefgelaufen!', delete_after=5)
            await ctx.message.delete()

    @commands.command()
    @commands.cooldown(rate=5, per=1)
    async def temp_channel(self, ctx, channel_name, time):
        if not channel_name:
            await ctx.send('Du hast keine Channel Name angegeben!')

        if not time:
            await ctx.send('Du hast keine Zeit angegeben!')

        guild = ctx.message.guild
        time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400, "w": 604800}
        tempchanneltime = int(time[:-1]) * time_convert[time[-1]]

        await ctx.message.delete()
        channel = await guild.create_text_channel(f'{channel_name}')
        await ctx.send(f'Temp Channel `{channel_name}` **Erfolgreich erstellt!**', delete_after=5)
        await asyncio.sleep(tempchanneltime)
        await channel.delete()
        await ctx.send(f'Temp Channel `{channel_name}` **Erfolgreich gelöscht!**', delete_after=5)

def setup(bot):
    bot.add_cog(Channel(bot))
