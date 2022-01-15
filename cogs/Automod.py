import asyncio
import json
import discord
from discord.ext import commands


class automod(commands.Cog):
    """
    `Automod which make you life easier`
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='blacklist_add', aliases=['blacklistadd', 'bladd'])
    @commands.has_permissions(manage_messages=True)
    async def blacklist_add(self, ctx, text):
        """
        Add a word to the blacklist!
        - **?bladd [`word`]**
        """

        with open("utils/json/blacklist.json", "r") as f:
            data = json.load(f)
            if text in data["blacklist"]:
                embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                      description=f'`Das Wort ({text})` ist **bereits in der Blacklist!**',
                                      color=discord.Color.red())
                await ctx.send(embed=embed, delete_after=5)
                await ctx.message.delete()
                return
            else:
                data["blacklist"].append(text)
        with open("utils/json/blacklist.json", "w") as file:
            json.dump(data, file, indent=4)
            embed = discord.Embed(color=discord.Color.green())
            embed.add_field(name='<:open:869959941321011260> **Blacklist Add**',
                            value=f'Hinzugefügtes Wort:\n'
                                  f'`{text}`',
                            inline=False)
            await ctx.send(embed=embed, delete_after=5)
            await ctx.message.delete()

    @commands.command(name='blacklist_remove', aliases=['blacklistremove', 'blrm'])
    @commands.has_permissions(manage_messages=True)
    async def blacklist_remove(self, ctx, text):
        """
        Remove a word to the blacklist!
        - **?blrm [`word`]**
        """

        with open("utils/json/blacklist.json", "r") as f:
            data = json.load(f)
            if text not in data["blacklist"]:
                embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                      description=f'`Das Wort ({text})` ist **nicht in der Blacklist!**',
                                      color=discord.Color.red())
                await ctx.send(embed=embed, delete_after=5)
                await ctx.message.delete()
                return
            else:
                data["blacklist"].remove(text)
        with open("utils/json/blacklist.json", "w") as file:
            json.dump(data, file, indent=4)
            embed = discord.Embed(color=discord.Color.green())
            embed.add_field(name='<:open:869959941321011260> **Blacklist Remove**',
                            value=f'**Entferntes Wort:**\n'
                                  f'`{text}`',
                            inline=False)
            await ctx.send(embed=embed, delete_after=5)
            await ctx.message.delete()

    @commands.command(name='blacklist_show', aliases=['blacklistshow', 'blshow'])
    @commands.has_permissions(manage_messages=True)
    async def blacklist_show(self, ctx):
        """
        Display the whole blacklist!
        - **?blshow**
        """

        with open('utils/json/blacklist.json', 'r') as f:
            data = json.load(f)

            if not data["blacklist"]:
                embed = discord.Embed(color=discord.Color.red())
                embed.add_field(name='<:close:864599591692009513> **ERROR**',
                                value='`Die Blacklist ist leer!`',
                                inline=False)
                await ctx.send(embed=embed, delete_after=5)
                await ctx.message.delete()
            else:
                embed = discord.Embed(color=discord.Color.green())
                embed.add_field(name='**Blacklist Words**',
                                value=f'`{data["blacklist"]}`',
                                inline=False)
                await ctx.send(embed=embed, delete_after=5)
                await ctx.author.send(embed=embed)
                await ctx.message.delete()

    @commands.command(name='blacklist_clear', aliases=['blacklistclear', 'blclear'])
    @commands.has_permissions(manage_messages=True)
    async def blacklist_clear(self, ctx):
        """
        Remove all words out of the blacklist!
        - **?blclear**
        """

        with open('utils/json/blacklist.json', 'r') as f:
            data = json.load(f)
            if not data["blacklist"]:
                embed = discord.Embed(color=discord.Color.red())
                embed.add_field(name='<:close:864599591692009513> **ERROR**',
                                value='`Die Blacklist ist bereits leer!`',
                                inline=False)
                await ctx.send(embed=embed, delete_after=5)
                await ctx.message.delete()
            else:
                data["blacklist"].remove(data)
                with open("utils/json/blacklist.json", "r+") as file:
                    json.dump(file, data, indent=4)
                embed = discord.Embed(color=discord.Color.green())
                embed.add_field(name='<:open:869959941321011260> **Deleted All Blacklisted Words**',
                                value=f'Deleted Words: `{data}`',
                                inline=False)
                await ctx.send(embed=embed, delete_after=5)
                await ctx.message.delete()

    @commands.command(name='channel_blacklist_add', aliases=['channelblacklistadd', 'chbladd'])
    @commands.has_permissions(manage_channels=True)
    async def channel_blacklist_add(self, ctx, id: int):
        with open("utils/json/channel_blacklist.json", "r") as f:
            data = json.load(f)
            if id in data["channel_blacklist"]:
                embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                      description=f'`Das Wort ({id})` ist **bereits in der Blacklist!**',
                                      color=discord.Color.red())
                await ctx.send(embed=embed, delete_after=5)
                await ctx.message.delete()
                return
            else:
                data["channel_blacklist"].append(id)
        with open("utils/json/channel_blacklist.json", "w") as file:
            json.dump(data, file, indent=4)
            embed = discord.Embed(color=discord.Color.green())
            embed.add_field(name='<:open:869959941321011260> **Channel Blacklist Add**',
                            value=f'Hinzugefügter Channel:\n'
                                  f'`{id}`',
                            inline=False)
            await ctx.send(embed=embed, delete_after=5)
            await ctx.message.delete()

    @commands.command(name='channel_blacklist_remove', aliases=['channelblacklistremove', 'chblrm'])
    @commands.has_permissions(manage_channels=True)
    async def channel_blacklist_remove(self, ctx, id: int):
        with open("utils/json/channel_blacklist.json", "r") as f:
            data = json.load(f)
            if id not in data["channel_blacklist"]:
                embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                      description=f'`Der Channel` `({id})` ist **nicht in der Channel Blacklist!**',
                                      color=discord.Color.red())
                await ctx.send(embed=embed, delete_after=5)
                await ctx.message.delete()
                return
            else:
                data["channel_blacklist"].remove(id)
        with open("utils/json/channel_blacklist.json", "w") as file:
            json.dump(data, file, indent=4)
            embed = discord.Embed(color=discord.Color.green())
            embed.add_field(name='<:open:869959941321011260> **Channel Blacklist Remove**',
                            value=f'**Entfernte Channel-ID:**\n'
                                  f'`{id}`',
                            inline=False)
            await ctx.send(embed=embed, delete_after=5)
            await ctx.message.delete()

    @commands.command(name='channel_blacklist_show', aliases=['channelblacklistshow', 'chblshow'])
    @commands.has_permissions(manage_channels=True)
    async def channel_blacklist_show(self, ctx):
        with open('utils/json/channel_blacklist.json', 'r') as f:
            data = json.load(f)

            if not data["channel_blacklist"]:
                embed = discord.Embed(color=discord.Color.red())
                embed.add_field(name='<:close:864599591692009513> **ERROR**',
                                value='`Die Channel Blacklist ist leer!`',
                                inline=False)
                await ctx.send(embed=embed, delete_after=5)
                await ctx.message.delete()
            else:
                embed = discord.Embed(color=discord.Color.green())
                embed.add_field(name='Channel Blacklist',
                                value=f'`{data["channel_blacklist"]}`',
                                inline=False)
                await ctx.send(embed=embed, delete_after=5)
                await ctx.author.send(embed=embed)
                await ctx.message.delete()

    @commands.command(name='channel_blacklist_clear', aliases=['channelblacklistclear', 'chblclear'])
    @commands.has_permissions(manage_channels=True)
    async def channel_blacklist_clear(self, ctx):

        with open('utils/json/channel_blacklist.json', 'r') as f:
            data = json.load(f)

            if not data["channel_blacklist"]:
                embed = discord.Embed(color=discord.Color.red())
                embed.add_field(name='<:close:864599591692009513> **ERROR**',
                                value='`Die Channel Backlist ist bereits leer!`',
                                inline=False)
                await ctx.send(embed=embed, delete_after=5)
                await ctx.message.delete()
            else:
                print(data["channel_blacklist"])
                data["channel_blacklist"].remove(data)
                with open("utils/json/channel_blacklist.json", "r+") as file:
                    json.dump(file, data, indent=4)
                embed = discord.Embed(color=discord.Color.green())
                embed.add_field(name='<:open:869959941321011260> **Deleted All Blacklisted Words**',
                                value=f'Deleted Words: `{data}`',
                                inline=False)
                await ctx.send(embed=embed, delete_after=5)
                await ctx.message.delete()


def setup(bot):
    bot.add_cog(automod(bot))
