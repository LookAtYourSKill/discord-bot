import asyncio
import discord
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
                                  description=f'Nach **{ctx.command}** fehlt ein Argument (**Name** oder Ähnliches)!',
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

        if isinstance(error, discord.Forbidden):
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',  # (MissingPermission)
                                  description=f'`Etwas ist schief gelaufen!`',
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
                                  description=f'`{ctx.command}` hat gerade noch **ein Cooldown von {round(error.retry_after)} Sekunde**!Versuche es später erneut!')
            await ctx.send(embed=embed, delete_after=5)
            await asyncio.sleep(1)
            await ctx.message.delete()

        if isinstance(error, commands.NoPrivateMessage):
            try:
                embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',  # (NoPrivateMessage)
                                      description=f'Der Command: **{ctx.command}** kann nicht in Privatmessanges benutzt werden!')
                await ctx.author.send(embed=embed, delete_after=5)
                await asyncio.sleep(1)
                await ctx.message.delete()
            except discord.HTTPException:
                pass

        if isinstance(error, commands.DisabledCommand):
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',  # (DisableCommand)
                                  description=f'**{ctx.command}** wurde deaktiviert!')
            await ctx.send(embed=embed, delete_after=5)
            await asyncio.sleep(1)
            await ctx.message.delete()

        if isinstance(error, commands.ExtensionNotFound):
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',  # (ExtensionNotFound)
                                  description=f'`Diese Extension` wurde **nicht gefunden**!')
            await ctx.send(embed=embed, delete_after=5)
            await asyncio.sleep(1)
            await ctx.message.delete()

        if isinstance(error, commands.ExtensionAlreadyLoaded):
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',  # (ExtensionAlreadyLoaded)
                                  description=f'`Diese Extension` ist bereits **Aktiviert**!')
            await ctx.send(embed=embed, delete_after=5)
            await asyncio.sleep(1)
            await ctx.message.delete()

        if isinstance(error, commands.ExtensionNotLoaded):
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',  # (ExtensionNotLoaded)
                                  description=f'`Diese Extension` ist bereits **Deaktiviert**!')
            await ctx.send(embed=embed, delete_after=5)
            await asyncio.sleep(1)
            await ctx.message.delete()

        if isinstance(error, discord.Forbidden):
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',  # (Discord Forbidden)
                                  description=f'Etwas ist schiefgelaufen! Versuche es **im einem Textchannel** o.Ä. erneut! ')
            await ctx.send(embed=embed, delete_after=5)
            await asyncio.sleep(1)
            await ctx.message.delete()

        else:
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                  description='**Der Error, wurde nicht gefunden!** Vielleicht kannst du damit etwas anfangen')
            embed.add_field(name='__ERROR__',
                            value=f'`{error}`',
                            inline=False)
            await ctx.send(embed=embed, delete_after=5)
            print("Error not caught in chat")
            await ctx.message.delete()
            print(error)

        # else:
        #    print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        #    traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


def setup(bot):
    bot.add_cog(CommandErrorHandler(bot)
                )
