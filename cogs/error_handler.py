import asyncio
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
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                  description=f'Nach **{ctx.command}** fehlt ein Argument!',
                                  color=0x4cd137)
            await ctx.send(embed=embed, delete_after=5)
            await asyncio.sleep(1)
            await ctx.message.delete()

        if isinstance(error, commands.MemberNotFound):
            if ctx.command.qualified_name == 'tag list':
                embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                      description=f'Der ``User konnte nicht gefunden werden``. Bitte versuche es erneut!',
                                      color=0x4cd137)
                await ctx.send(embed=embed, delete_after=5)
                await asyncio.sleep(1)
                await ctx.message.delete()

            if isinstance(error, commands.BotMissingPermissions):
                embed = discord.Embed(title='<:close:864599591692009513> ERROR',
                                      description=f'Um diesen Befehl auszuführen, fehlen ``mir die Berechtigungen``!',
                                      color=0x4cd137)
                await ctx.send(embed=embed, delete_after=5)
                await asyncio.sleep(1)
                await ctx.message.delete()

            else:
                print("Error not caught")
                print(error)

        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                  description=f'Um diesen Befehl auszuführen, fehlen ``dir die Berechtigungen``!',
                                  color=0x4cd137)
            await ctx.send(embed=embed, delete_after=5)
            await asyncio.sleep(1)
            await ctx.message.delete()

        if isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                  description=f'**Unknown Command**',
                                  color=0x4cd137)
            await ctx.send(embed=embed, delete_after=5)
            await asyncio.sleep(1)
            await ctx.message.delete()

        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))
