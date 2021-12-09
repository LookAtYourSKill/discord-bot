import json
import random

import discord
from discord.ext import commands

with open('./config.json', 'r') as config_file:
    config = json.load(config_file)


class Verify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def verify(self, ctx):
        member = ctx.author

        def check(m):
            return m.author == ctx.author

        role = ctx.guild.get_role(int(config['verified_role']))
        embed = discord.Embed(title=f'Verification',
                              description=f'You have `1` attempt to verify. If you fail, you may be re-evaluated by executing the command again',
                              color=discord.colour.Color.purple())
        failembed = discord.Embed(title=f'Verification',
                                  description=f'You have failed the verification process! Please try again',
                                  color=discord.colour.Color.purple())
        passembed = discord.Embed(title=f'Verification',
                                  description=f'You have passed the verification process! Enjoy your stay',
                                  color=discord.colour.Color.purple())
        captcha = random.randint(1, 1)
        #print(f"roles: {ctx.guild.roles}")

        if captcha == 1:
            embed.set_image(
                url=f'https://cdn.discordapp.com/attachments/910579746205745283/917283179843452970/wickCaptcha.png')
            await ctx.send(embed=embed)
            msg = await self.bot.wait_for('message', check=check, timeout=15)
            if msg.content == 'KZEXEH':
                await ctx.send(embed=passembed)
                await member.add_roles(role)
            else:
                await ctx.send(embed=failembed)


def setup(bot):
    bot.add_cog(Verify(bot))
