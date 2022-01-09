import discord
from discord.ext import commands


class Help(commands.Cog):
    """
    Sends this help message
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, *content):
        """
                Shows this help
                """

        prefix = '?'
        version = 1

        owner = 493370963807830016
        owner_name = 'LookAtYourSkill#6822'

        if not content:
            embed = discord.Embed(title='Commands and Modules', color=discord.Color.blue(),
                                  description=f'Use `{prefix}help <module>` to gain more information about that module and \n'
                                              f'`{prefix}help <command>` to gain more information about that command')

            embed.add_field(name='Moderation',
                            value='`ban`, `softban`, `unban`, `unbanall`, `tempban`, `banned`, `mute`, `unmute`, `tempmute`, `kick`, `dc`, `clear`, `slowmode`, `nuke`, `block`, `unblock`',
                            inline=False)
            embed.add_field(name='Blacklist',
                            value='`blacklistadd`, `blacklistremove`, `blacklistshow`, `blacklistclear`',
                            inline=False)
            embed.add_field(name=f'Administration',
                            value=f'`setstatus`, `lock`, `release`, `say`, `gawrole`, `muterole`, `rules`',
                            inline=False)
            embed.add_field(name='Utilities',
                            value='`invite`, `invites`, `botinvite`, `embed`, `repeat`, `senddm`, `password`, `spotify`, `add`, `minus`, `multiplicate`, `divide`',
                            inline=False)
            embed.add_field(name='Channel',
                            value='`deletechannel`, `createchannel`, `tempchannel`',
                            inline=False)
            embed.add_field(name='Roles',
                            value='`giverole`, `removerole`, `create_role`, `delete_role`, `getroles`, `removeroles`',
                            inline=False)
            embed.add_field(name='Fun',
                            value='`8ball`, `slots`, `dice`, `rps`, `num_game`, `simp`, `sus`',
                            inline=False)
            embed.add_field(name='Info',
                            value='`info`, `members`, `server`, `joined`, `bot`, `avatar`',
                            inline=False)
            embed.add_field(name='Systems',
                            value='`verify`, `setup`, `toggle`, `new`, `close`, `addaccess`, `delaccess`, `addpingedrole`, `delpingedrole`, `addadminrole`, `deladminrole`')
            embed.add_field(name='Timers',
                            value='`reminder`, `giveaway`',
                            inline=False)
            await ctx.send(embed=embed)

        elif str(content) == 'Moderation' or str(content) == 'moderation':
            embed = discord.Embed(
                description=f'Verwende `{prefix}help <command>` to gain more information about the command',
                color=discord.Color.blurple())
            embed.add_field(name='ban <member> [reason]',
                            value='Ban a member from your server',
                            inline=False)
            embed.add_field(name='softban <member> [reason]',
                            value='Kick a member from your server and delete all of its messages',
                            inline=False)
            embed.add_field(name='unban <id>',
                            value='Unban a member from your server',
                            inline=False)
            embed.add_field(name='unbanall',
                            value='Unban every banned member on your server',
                            inline=False)
            embed.add_field(name='tempban <member> <time> [reason]',
                            value='Ban a member for a specific time from your server',
                            inline=False)
            embed.add_field(name='banned',
                            value='List all banned members',
                            inline=False)
            embed.add_field(name='mute <member>',
                            value='Give a member a specific role, so the user cant write in any textchannel\'s and join in any voicechannel\'s',
                            inline=False)
            embed.add_field(name='unmute <member>',
                            value='Remove a specific role from a member, so the user can write again in any textchannel\'s and join in any voicechannel\'s',
                            inline=False)
            embed.add_field(name='tempmute <member> <time> [reason]',
                            value='Give a member a specific role, so the user cant write in any textchannel\'s and join in any voicechannel\'s for a specific time',
                            inline=False)
            embed.add_field(name='kick <member>',
                            value='Kick a user from your server',
                            inline=False)
            embed.add_field(name='dc <member>',
                            value='Disconnect a user from a voicechannel',
                            inline=False)
            embed.add_field(name='clear <amount>',
                            value='Clears a specific amount of messages',
                            inline=False)
            embed.add_field(name='slowmode <seconds>',
                            value='Activate / Disable a slowmode in a textchannel',
                            inline=False)
            embed.add_field(name='nuke <channel>',
                            value='Delete and Clone a channel on your server',
                            inline=False)
            embed.add_field(name='block <member>',
                            value='Block a user from writing in a textchannel',
                            inline=False)
            embed.add_field(name='unblock <member>',
                            value='Unblock a user from writing in a textchannel',
                            inline=False)
            embed.set_footer(text='[] optional | <> required')
            await ctx.send(embed=embed)

        elif len(content) > 1:
            embed = discord.Embed(title="That's too much.",
                                  description="Please request only one module/command at once ",
                                  color=discord.Color.orange())
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
