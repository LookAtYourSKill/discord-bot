import asyncio
import json
import os
import string
import random
import discord
from discord.ext import commands


class utilities(commands.Cog):
    """
    `A few commands may useless my not`
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='invite', help='?invite')
    async def invite(self, ctx):
        """
        Create an invite
        - **?invite**
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Utilities"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Utilities) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            invite = await ctx.channel.create_invite(reason="Automated Invite")
            embed = discord.Embed(description=f'{ctx.author.mention} Invite Link zum Server **{ctx.guild.name}**\n'
                                              f'[Invite]({invite})',
                                  color=0x4cd137)
            await ctx.send(embed=embed)

    @commands.command(name='botinvite', help='?botinvite')
    @commands.has_permissions(administrator=True)
    async def botinvite(self, ctx):
        """
        Get two invites, with which you can invite the bot
        - **?botinvite**
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Utilities"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Utilities) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description=f'{ctx.author.mention} hier sind zwei Invite Links zum Bot \n'
                                              f'[Botinvite (Custom Rechte)](https://discord.com/oauth2/authorize?client_id=790965419670241281&scope=bot&permissions=261993005047)\n'
                                              f'[Botinvite (Administrator Rechte)](https://discord.com/oauth2/authorize?client_id=790965419670241281&scope=bot&permissions=8)',
                                  color=0x4cd137)
            await ctx.send(embed=embed)

    @commands.command(name='embed')
    async def embed(self, ctx, *, text: str):
        """
        Create an embed with your text
        - **?embed [`text`]**
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Utilities"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Utilities) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description=text)
            await ctx.send(embed=embed)

    @commands.command(name='repeat', aliases=['mimic', 'copy', 'echo'])
    async def _do_repeat(self, ctx, *, inp: str):
        """
        Repeats your input
        - **?repeat [`input`]**
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Utilities"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Utilities) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            await ctx.send(inp)

    @_do_repeat.error
    async def do_repeat_handler(self, ctx, error):
        """A local Error Handler for our command do_repeat.
        This will only listen for errors in do_repeat.
        The global on_command_error will still be invoked after.
        """
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'inp':
                embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                      description=f'Nach **{ctx.command}** fehlt ein Argument!',
                                      color=0x4cd137)
                await ctx.send(embed=embed, delete_after=5)
                await asyncio.sleep(1)
                await ctx.message.delete()

    @commands.command(name='invites')
    async def user_invites(self, ctx, member: discord.Member = None):
        """
        Display all invites form a user
        - **?invites [`member`]**
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Utilities"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Utilities) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            member = member if member else ctx.author
            invites_raw = [invite for invite in (await ctx.guild.invites()) if invite.inviter.id == member.id]
            invites: int = 0
            for invite in invites_raw:
                invites += invite.uses
            embed = discord.Embed(title='Invites',
                                  color=discord.Color.blue())
            embed.add_field(name=f'Invites from {member}',
                            value=f"You've invited **{invites}** members to the server!")
            embed.set_footer(text=f'Requested by {ctx.author.name}',
                             icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

    @commands.command(name='senddm')
    async def senddm(self, ctx, member: discord.Member = None, *, text=None):
        """
        Send a user a direct message with the text you want
        - **?senddm [`member`] [`text`]**
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Utilities"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Utilities) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title='You got MAIL!', color=discord.Color.orange())
            embed.add_field(name='From:',
                            value=f"{ctx.author.mention}",
                            inline=False)
            embed.add_field(name='Message: ',
                            value=f"{text}",
                            inline=True)
            await member.send(embed=embed)

            embed = discord.Embed(title='<:open:869959941321011260> Successfully',
                                  description='**Die Nachricht** wurde `Erfolgreich gesendet`!')
            await ctx.send(embed=embed, delete_after=5)
            await asyncio.sleep(1)
            await ctx.message.delete()

    @commands.command(name='password', aliases=['pw'])
    async def password(self, ctx):
        """
        Create a safe password, which only will be visible in your Direct messages for about  10 seconds
        - **?password**
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Utilities"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Utilities) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            length = 20
            chars = string.ascii_letters + string.digits + '!@#$%^&*()'
            random.seed = (os.urandom(1024))

            await ctx.message.author.send('Dein Passwort wurde erstellt!', delete_after=5)
            await asyncio.sleep(1)
            await ctx.message.delete()
            await ctx.message.author.send(''.join(random.choice(chars) for i in range(length)), delete_after=10)


def setup(bot):
    bot.add_cog(utilities(bot))
