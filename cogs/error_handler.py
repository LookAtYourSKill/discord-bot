import asyncio
from distutils import extension
import discord
import traceback
import sys
from discord.ext import commands

class CommandErrorHandler(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """The event triggered when an error is raised while invoking a command.
        Parameters
        ------------
        ctx: commands.Context
            The context used for command invocation.
        error: commands.CommandError
            The Exception raised.
        """
        if hasattr(ctx.command, 'on_error'):
            return

        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return

        ignored = (commands.CommandNotFound,)
        error = getattr(error, 'original', error)

        if isinstance(error, ignored):
            return

        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',  # (MissingRequiredArgument)
                                  description=f'Nach **{ctx.command}** fehlt ein Argument!',
                                  color=0x4cd137)
            await ctx.send(embed=embed, delete_after=5)
            await asyncio.sleep(1)
            await ctx.message.delete()

        if isinstance(error, commands.MemberNotFound):
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',  # (MemberNotFound)
                                  description=f'Der ``User konnte nicht gefunden werden``. Bitte versuche es erneut!',
                                  color=0x4cd137)
            await ctx.send(embed=embed, delete_after=5)
            await asyncio.sleep(1)
            await ctx.message.delete()

        if isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',  # (BotMissingPermission)
                                  description=f'Um diesen Befehl auszuführen, fehlen ``mir die Berechtigungen``!',
                                  color=0x4cd137)
            await ctx.send(embed=embed, delete_after=5)
            await asyncio.sleep(1)
            await ctx.message.delete()

        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',  # (MissingPermission)
                                  description=f'Um diesen Befehl auszuführen, fehlen ``dir die Berechtigungen``!',
                                  color=0x4cd137)
            await ctx.send(embed=embed, delete_after=5)
            await asyncio.sleep(1)
            await ctx.message.delete()

        if isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',  # (CommandNotFound)
                                  description=f'**Unknown Command**',
                                  color=0x4cd137)
            await ctx.send(embed=embed, delete_after=5)
            await asyncio.sleep(1)
            await ctx.message.delete()

        if isinstance(error, commands.MissingRole):
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',  # (MissingRequiredRole)
                                  description=f'Dir fehlt `eine bestimmte Rolle` um diesen Befehl ausführen zu können!')
            await ctx.send(embed=embed, delete_after=5)
            await asyncio.sleep(1)
            await ctx.message.delete()

        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',  # (CommandOnCooldown)
                                  description=f'{ctx.command} hat gerade noch ein Cooldown {round(error.retry_after)}! Versuche es später erneut!')
            await ctx.send(embed=embed, delete_after=5)
            await asyncio.sleep(1)
            await ctx.message.delete()

        if isinstance(error, commands.NoPrivateMessage):
            try:
                embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',  # (NoPrivateMessage)
                                      description=f'Der Command: **{ctx.command}** kann nicht in Privatmessages benutzt werden!')
                await ctx.author.send(embed=embed)
            except discord.HTTPException:
                pass

        if isinstance(error, commands.DisabledCommand):
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',  # (DisableCommand)
                                  description=f'**{ctx.command}** wurde deaktiviert!')
            await ctx.send(embed=embed)

        if isinstance(error, commands.ExtensionAlreadyLoaded):
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',  # (ExtensionAlreadyLoaded)
                                  description=f'`{extension}` ist bereits **Aktiviert**!')
            await ctx.send(embed=embed)

        if isinstance(error, commands.ExtensionNotFound):
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',  # (ExtensionNotFound)
                                  description=f'`{extension}` wurde **nicht gefunden**!')
            await ctx.send(embed=embed)

        if isinstance(error, commands.ExtensionNotLoaded):
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',  # (ExtensionAlreadyLoaded)
                                  description=f'`{extension}` ist bereits **Deaktiviert**!')
            await ctx.send(embed=embed)

        #if isinstance(error, commands.ExtensionError):
        #    embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',  # (ExtensionAlreadyLoaded)
        #                          description=f'Es gab ein Fehler mit der Extension `({extension})`! **Bitte versuche es erneut**')
        #    await ctx.send(embed=embed)

        else:
            print("Error not caught in chat")
            print(error)

        #else:
        #    print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        #    traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))
