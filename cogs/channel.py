import discord
from discord.ext import commands

class Channel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def delete_channel(self, ctx, channel: discord.TextChannel):

        if channel is not None:
            await channel.delete()
            await ctx.send(f"Der Channel ``{channel.name}`` wurde **Erfolgreich gelöscht!**")

        elif not channel:
            channel = ctx.channel
            await ctx.channel.delete()
            await ctx.send(f"Der Channel ``{channel.name}`` wurde **Erfolgreich gelöscht!**")

        else:
            await ctx.send(f'No channel named, "{channel}", was found')

    @commands.command()
    async def create_channel(self, ctx, channel_name):
        guild = ctx.message.guild

        if not channel_name:
            await ctx.send('Du hast **keinen Channel Namen angegeben!**')

        if channel_name is not None:
            channel = await guild.create_text_channel(f'{channel_name}')
            await ctx.send(f'Der Channel {channel.mention} wurde **Erfolgreich erstellt!**')

        else:
            await ctx.send(f'Irgendetwas ist schiefgelaufen!')

def setup(bot):
    bot.add_cog(Channel(bot))
