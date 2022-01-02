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

        error = getattr(error, 'original', error)

        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',  # (MissingRequiredArgument)
                                  description=f'Nach **{ctx.command}** fehlt ein Argument!\n'
                                              f'`{error}`',
                                  color=discord.Color.red())

            if discord.ChannelType.private:
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embed, delete_after=5)

            await asyncio.sleep(1)

            if discord.ChannelType.private:
                return
            else:
                await ctx.message.delete()

        if isinstance(error, commands.MemberNotFound):
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',  # (MemberNotFound)
                                  description=f'Der ``User konnte nicht gefunden werden``. Bitte versuche es erneut!',
                                  color=discord.Color.red())

            if discord.ChannelType.private:
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embed, delete_after=5)

            await asyncio.sleep(1)

            if discord.ChannelType.private:
                return
            else:
                await ctx.message.delete()

        if isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',  # (BotMissingPermission)
                                  description=f'Um diesen Befehl auszuführen, fehlen ``mir die Berechtigungen``!',
                                  color=discord.Color.red())

            if discord.ChannelType.private:
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embed, delete_after=5)

            await asyncio.sleep(1)

            if discord.ChannelType.private:
                return
            else:
                await ctx.message.delete()

        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',  # (MissingPermission)
                                  description=f'Um diesen Befehl auszuführen, fehlen ``dir die Berechtigungen``!',
                                  color=discord.Color.red())

            if discord.ChannelType.private:
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embed, delete_after=5)

            await asyncio.sleep(1)

            if discord.ChannelType.private:
                return
            else:
                await ctx.message.delete()

        if isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',  # (CommandNotFound)
                                  description=f'**Unknown Command**',
                                  color=discord.Color.red())

            if discord.ChannelType.private:
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embed, delete_after=5)

            await asyncio.sleep(1)

            if discord.ChannelType.private:
                return
            else:
                await ctx.message.delete()

        if isinstance(error, commands.MissingRole):
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',  # (MissingRequiredRole)
                                  description=f'Dir fehlt `eine bestimmte Rolle` um diesen Befehl ausführen zu können!',
                                  color=discord.Color.red())
            if discord.ChannelType.private:
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embed, delete_after=5)

            await asyncio.sleep(1)

            if discord.ChannelType.private:
                return
            else:
                await ctx.message.delete()

        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',  # (CommandOnCooldown)
                                  description=f'`{ctx.command}` hat gerade noch **ein Cooldown von {round(error.retry_after)} Sekunde**!Versuche es später erneut!',
                                  color=discord.Color.red())
            if discord.ChannelType.private:
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embed, delete_after=5)

            await asyncio.sleep(1)

            if discord.ChannelType.private:
                return
            else:
                await ctx.message.delete()

        if isinstance(error, asyncio.TimeoutError):
            timeoutembed = discord.Embed(title=f'Timeout Error',
                                         description='You\'ve needed too much time. Try it again by executing the command again!',
                                         color=discord.Color.red())
            if discord.ChannelType.private:
                await ctx.send(embed=timeoutembed)
            else:
                await ctx.send(embed=timeoutembed, delete_after=5)

            await asyncio.sleep(1)

            if discord.ChannelType.private:
                return
            else:
                await ctx.message.delete()

        if isinstance(error, commands.NoPrivateMessage):
            try:
                embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',  # (NoPrivateMessage)
                                      description=f'Der Command: **{ctx.command}** kann nicht in Privatmessanges benutzt werden!',
                                      color=discord.Color.red())
                if discord.ChannelType.private:
                    await ctx.send(embed=embed)
                else:
                    await ctx.send(embed=embed, delete_after=5)

                await asyncio.sleep(1)

                if discord.ChannelType.private:
                    return
                else:
                    await ctx.message.delete()

            except discord.Forbidden:
                pass

        if isinstance(error, commands.DisabledCommand):
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',  # (DisableCommand)
                                  description=f'**{ctx.command}** wurde deaktiviert!',
                                  color=discord.Color.red())
            if discord.ChannelType.private:
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embed, delete_after=5)

            await asyncio.sleep(1)

            if discord.ChannelType.private:
                return
            else:
                await ctx.message.delete()

        if isinstance(error, commands.ExtensionNotFound):
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',  # (ExtensionNotFound)
                                  description=f'`Diese Extension` wurde **nicht gefunden**!',
                                  color=discord.Color.red())
            if discord.ChannelType.private:
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embed, delete_after=5)

            await asyncio.sleep(1)

            if discord.ChannelType.private:
                return
            else:
                await ctx.message.delete()

        if isinstance(error, commands.ExtensionAlreadyLoaded):
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',  # (ExtensionAlreadyLoaded)
                                  description=f'`Diese Extension` ist bereits **Aktiviert**!',
                                  color=discord.Color.red())
            if discord.ChannelType.private:
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embed, delete_after=5)

            await asyncio.sleep(1)

            if discord.ChannelType.private:
                return
            else:
                await ctx.message.delete()

        if isinstance(error, commands.ExtensionNotLoaded):
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',  # (ExtensionNotLoaded)
                                  description=f'`Diese Extension` ist bereits **Deaktiviert**!',
                                  color=discord.Color.red())
            if discord.ChannelType.private:
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embed, delete_after=5)

            await asyncio.sleep(1)

            if discord.ChannelType.private:
                return
            else:
                await ctx.message.delete()

        else:
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                  description='**Der Error, wurde nicht gefunden!** Vielleicht kannst du damit etwas anfangen',
                                  color=discord.Color.red())
            embed.add_field(name='__ERROR__',
                            value=f'`{error}`',
                            inline=False)
            await ctx.author.send(embed=embed)
            print("Error not caught in chat")
            print(error)


def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))
