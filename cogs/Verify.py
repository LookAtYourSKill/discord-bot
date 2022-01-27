import json
import random
import discord
from discord.ext import commands
from discord.utils import get


class verify(commands.Cog):
    """
    `A Verify Command, for a verification for your server`
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(rate=120, per=1)
    async def verify(self, ctx):
        """
        The Verification Command
        - **?verify**
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Verify"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Verify) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#8691)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            with open('utils/json/on_guild.json', 'r') as f:
                guild_data = json.load(f)

            if guild_data[str(ctx.guild.id)]["verified_role"]:
                role = get(ctx.guild.roles, id=guild_data[str(ctx.guild.id)]['verified_role'])

                if guild_data[str(ctx.guild.id)]["verify_channel"]:
                    if ctx.channel.id == guild_data[str(ctx.guild.id)]['verify_channel']:

                        if role in ctx.author.roles:
                            embed = discord.Embed(
                                description='Du hast dich **bereits Verifiziert**, oder hast zumindest die `Verified Role`!',
                                color=discord.Color.red())
                            await ctx.message.delete()
                            await ctx.send(embed=embed, delete_after=10)
                            return

                        member = ctx.author

                        def check(m):
                            return m.author == ctx.author

                        role = ctx.guild.get_role(guild_data[str(ctx.guild.id)]['verified_role'])

                        embed = discord.Embed(title=f'Verification',
                                              description=f'You have `1` attempt to verify. If you fail, you may be re-evaluated by executing the command again',
                                              color=discord.colour.Color.purple())
                        failembed = discord.Embed(title=f'Verification Failed',
                                                  description=f'You have failed the verification process! Please try again',
                                                  color=discord.colour.Color.purple())
                        passembed = discord.Embed(title=f'Verification Successful',
                                                  description=f'You have passed the verification process! Enjoy your stay\n'
                                                              f'You\'ve got the role {role.mention}',
                                                  color=discord.colour.Color.purple())
                        timeoutembed = discord.Embed(title=f'Timeout Error',
                                                     description='You\'ve needed too much time. Try it again by executing the command again!',
                                                     color=discord.Color.red())
                        captcha = random.randint(1, 4)

                        await ctx.message.delete()

                        if captcha == 1:
                            embed.set_image(
                                url=f'https://cdn.discordapp.com/attachments/921773399565553695/921773496827256852/wickCaptcha.png')
                            await ctx.send(embed=embed, delete_after=20)
                            msg = await self.bot.wait_for('message', check=check, timeout=15)
                            if msg.content == 'KZEXEH' and not msg.content == 'QVDKGB' and not msg.content == '47859' and not msg.content == 'FZQU02':
                                await ctx.send(embed=passembed, delete_after=10)
                                try:
                                    await member.add_roles(role)
                                    await msg.delete()
                                except TimeoutError:
                                    await ctx.send(embed=timeoutembed)
                            else:
                                await msg.delete()
                                await ctx.send(embed=failembed, delete_after=10)

                        elif captcha == 2:
                            embed.set_image(
                                url=f'https://cdn.discordapp.com/attachments/921773399565553695/921774173892796426/wickCaptcha1.png')
                            await ctx.send(embed=embed, delete_after=20)
                            msg = await self.bot.wait_for('message', check=check, timeout=15)
                            if msg.content == 'QVDKGB' and not msg.content == 'KZEXEH' and not msg.content == '47859' and not msg.content == 'FZQU02':
                                await ctx.send(embed=passembed, delete_after=10)
                                try:
                                    await member.add_roles(role)
                                    await msg.delete()
                                except TimeoutError:
                                    await ctx.send(embed=timeoutembed)
                            else:
                                await msg.delete()
                                await ctx.send(embed=failembed, delete_after=10)

                        elif captcha == 3:
                            embed.set_image(
                                url=f'https://cdn.discordapp.com/attachments/921773399565553695/921774173452402758/wickCaptcha2.png')
                            await ctx.send(embed=embed, delete_after=20)
                            msg = await self.bot.wait_for('message', check=check, timeout=15)
                            if msg.content == '47859' and not msg.content == 'KZEXEH' and not msg.content == 'QVDKGB' and not msg.content == 'FZQU02':
                                await ctx.send(embed=passembed, delete_after=10)
                                try:
                                    await member.add_roles(role)
                                    await msg.delete()
                                except TimeoutError:
                                    await ctx.send(embed=timeoutembed)
                            else:
                                await msg.delete()
                                await ctx.send(embed=failembed, delete_after=10)

                        elif captcha == 4:
                            embed.set_image(
                                url=f'https://cdn.discordapp.com/attachments/921773399565553695/921774417829310474/wickCaptcha3.png')
                            await ctx.send(embed=embed, delete_after=20)
                            msg = await self.bot.wait_for('message', check=check, timeout=15)
                            if msg.content == 'FZQU02' and not msg.content == 'KZEXEH' and not msg.content == 'QVDKGB' and not msg.content == '47859':
                                await ctx.send(embed=passembed, delete_after=10)
                                try:
                                    await member.add_roles(role)
                                    await msg.delete()
                                except TimeoutError:
                                    await ctx.send(embed=timeoutembed)
                            else:
                                await msg.delete()
                                await ctx.send(embed=failembed, delete_after=10)

                        else:
                            await ctx.send(embed=failembed, delete_after=5)

                    else:
                        await ctx.message.delete()
                        embed = discord.Embed(description='Wrong Channel. Please use the verify channel :smile:\n'
                                                          f'<#{guild_data[str(ctx.guild.id)]["verify_channel"]}>',
                                              color=discord.Color.red())
                        await ctx.send(embed=embed, delete_after=5)

                else:
                    embed = discord.Embed(description=f'Es wurde kein `Verify Channel` eingestellt! Bitte melde dies dem Owner des Servers oder der Befehl funktioniert nicht!',
                                          color=discord.Color.red())
                    await ctx.send(embed=embed)

            else:
                embed = discord.Embed(description=f'Es wurde keine `Verified Role` eingestellt! Bitte melde dies dem Owner des Servers oder der Befehl funktioniert nicht!',
                                      color=discord.Color.red())
                await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(verify(bot))
