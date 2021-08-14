import asyncio
import json
import discord
from discord.ext import commands


class Automod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='bladd', aliases=['blacklistadd'])
    async def blacklist_add(self, ctx, text):
        with open("C:/Users/simon/PycharmProjects/pythonProject/Discord Bot/utils/json_files/blacklist.json", "r") as f:
            data = json.load(f)
            if text not in f:
                data.append(text)
            else:
                embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                      description=f'`Das Wort ({text})` ist **bereits in der Blacklist!**')
                await ctx.send(embed=embed)
        with open("C:/Users/simon/PycharmProjects/pythonProject/Discord Bot/utils/json_files/blacklist.json", "w") as file:
            json.dump(data, file, indent=4)
            embed = discord.Embed(title='',
                                  description='')
            embed.add_field(name='<:open:869959941321011260> **Blacklist Add**',
                            value=f'Hinzugefügtes Wort:\n'
                                  f'`{text}`',
                            inline=False)
            await ctx.send(embed=embed)

    @commands.command(name='blrm', aliases=['blacklistremove'])
    async def blacklist_remove(self, ctx, text):
        with open("C:/Users/simon/PycharmProjects/pythonProject/Discord Bot/utils/json_files/blacklist.json", "r") as f:
            data = json.load(f)
            if text in f:
                data.remove(text)
            else:
                embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                      description=f'`Das Wort ({text})` ist **nicht in der Blacklist!**')
                await ctx.send(embed=embed)
        with open("C:/Users/simon/PycharmProjects/pythonProject/Discord Bot/utils/json_files/blacklist.json", "w") as file:
            json.dump(data, file, indent=4)
            embed = discord.Embed(title='',
                                  description='')
            embed.add_field(name='<:open:869959941321011260> **Blacklist Remove**',
                            value=f'**Entferntes Wort:**\n'
                                  f'`{text}`',
                            inline=False)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Automod(bot))
