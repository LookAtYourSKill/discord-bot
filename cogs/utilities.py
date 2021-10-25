import asyncio
import os
import string
import time
import random
import discord
from discord.ext import commands
from discord.ext.commands import bot

bot = commands.Bot(intense=discord.Intents.all(), command_prefix='?')


class Utilities(commands.Cog):
    """
    `A few commands may useless my not`
    """

    def __init__(self):
        self.bot = bot

    @commands.command(name='invite', help='?invite')
    async def invite(self, ctx):
        """
        Create an invite
        """

        invite = await ctx.channel.create_invite(reason="Automated Invite")
        embed = discord.Embed(title=' ',
                              description=f'{ctx.author.mention} Invite Link zum Server **{ctx.guild.name}**\n'
                                          f'[Invite]({invite})',
                              color=0x4cd137)
        await ctx.send(embed=embed)

    @commands.command(name='botinvite', help='?botinvite')
    @commands.has_permissions(administrator=True)
    async def botinvite(self, ctx):
        """
        Get two invites, with which you can invite the bot
        """

        embed = discord.Embed(title=' ',
                              description=f'{ctx.author.mention} hier sind zwei Invite Links zum Bot \n'
                                          f'[Botinvite (Custom Rechte)](https://discord.com/oauth2/authorize?client_id=790965419670241281&scope=bot&permissions=261993005047)\n'
                                          f'[Botinvite (Administrator Rechte)](https://discord.com/oauth2/authorize?client_id=790965419670241281&scope=bot&permissions=8)',
                              color=0x4cd137)
        await ctx.send(embed=embed)

    @commands.command(name='embed')
    async def embed(self, ctx, *, text: str):
        """
        Create an embed with your text
        """

        embed = discord.Embed(title='',
                              description=text)
        await ctx.send(embed=embed)

    @commands.command(name='repeat', aliases=['mimic', 'copy', 'echo'])
    async def _do_repeat(self, ctx, *, inp: str):
        """
        Repeats your input
        """

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
        """

        member = member if member else ctx.author
        invites_raw = [invite for invite in (await ctx.guild.invites()) if invite.inviter.id == member.id]
        invites: int = 0
        for invite in invites_raw:
            invites += invite.uses
        embed = discord.Embed(title='Invites',
                              color=0xff00c8)
        embed.add_field(name=f'Invites from {member}',
                        value=f"You've invited **{invites}** members to the server!")
        embed.set_footer(text=f'Requested by {ctx.author.name}',
                         icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        # await ctx.send(f"Member {member.mention} has {invites} invites")

    @commands.command(name='senddm')
    async def senddm(self, ctx, member: discord.Member = None, *, text=None):
        """
        Send a user a direct message with the text you want
        """

        embed = discord.Embed(title='You got MAIL!', color=0xff00c8)
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
        """

        length = 20
        chars = string.ascii_letters + string.digits + '!@#$%^&*()'
        random.seed = (os.urandom(1024))

        await ctx.message.author.send('Dein Passwort wurde erstellt!', delete_after=5)
        await asyncio.sleep(1)
        await ctx.message.delete()
        await ctx.message.author.send(''.join(random.choice(chars) for i in range(length)), delete_after=10)

    @commands.command(name='reminder')
    async def reminder(self, ctx, zeit=None, *, reason='Nicht angegeben'):
        """
        Creates a reminder for a time you want
        """

        time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400, "w": 604800}
        remindertime = int(zeit[:-1]) * time_convert[zeit[-1]]
        if zeit is None:
            await ctx.send('Du musst eine Zeit angeben!')
        elif reason is None:
            embed = discord.Embed(title='Error',
                                  description='You did\'nt mentioned a reason.\n'
                                              'By standard it was set to \'nicht angegeben\'!')
        else:
            embed = discord.Embed(title='Reminder',
                                  description=f'You\'ll be reminded in `{zeit}` because of `{reason}`')
            await ctx.send(embed=embed)

            await asyncio.sleep(remindertime)
            await ctx.send(f'{ctx.author.mention} i should remind you now, ``reason = {reason}``')


def setup(bot):
    bot.add_cog(Utilities()
                )
