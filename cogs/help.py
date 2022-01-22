import discord
from discord.ext import commands


class Help(commands.Cog):
    """
    Sends this help message
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, content=None):
        """
        Shows this help
        """

        prefix = '?'

        if not content:
            embed = discord.Embed(title='Commands and Modules', color=discord.Color.blue(),
                                  description=f'Use `{prefix}help <module>` to gain more information about that module and \n'
                                              f'`{prefix}help <command>` to gain more information about that command')

            embed.add_field(name='Moderation',
                            value='`ban`, `softban`, `warn`, `unwarn`, `warns`, `unban`, `unbanall`, `tempban`, `banned`, `mute`, `unmute`, `tempmute`, `kick`, `dc`, `clear`, `slowmode`, `nuke`, `block`, `unblock`',
                            inline=False)
            embed.add_field(name='Blacklist',
                            value='`blacklistadd`, `blacklistremove`, `blacklistshow`, `blacklistclear`',
                            inline=False)
            embed.add_field(name=f'Administration',
                            value=f'`setstatus`, `lock`, `release`, `say`, `gawrole`, `muterole`, `rules`',
                            inline=False)
            embed.add_field(name='Utilities',
                            value='`invite`, `invites`, `botinvite`, `embed`, `repeat`, `senddm`, `password`, `translate`, `add`, `minus`, `multiplicate`, `divide`',
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
                            value='`verify`, `setup`, `toggle`',
                            inline=False)
            embed.add_field(name='Ticket',
                            value='`new`, `close`, `addaccess`, `delaccess`, `addpingedrole`, `delpingedrole`, `addadminrole`, `deladminrole`',
                            inline=False)
            embed.add_field(name='Timers',
                            value='`reminder`, `giveaway`, `poll`',
                            inline=False)
            await ctx.send(embed=embed)

        elif str(content) == 'Moderation' or str(content) == 'moderation':
            embed = discord.Embed(
                description=f'Use `{prefix}help <command>` to gain more information about the command',
                color=discord.Color.blurple())
            embed.add_field(name='ban <member> [reason]',
                            value='Ban a member from your server',
                            inline=False)
            embed.add_field(name='softban <member> [reason]',
                            value='Kick a member from your server and delete all of its messages',
                            inline=False)
            embed.add_field(name='warn <member>',
                            value='Warn a member on your Server',
                            inline=False)
            embed.add_field(name='unwarn <id>',
                            value='Unwarn a member on your Server',
                            inline=False)
            embed.add_field(name='warns <id>',
                            value='Checks the warns from the member for your Server',
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

        elif str(content) == 'Blacklist' or str(content) == 'blacklist':
            embed = discord.Embed(
                description=f'Use `{prefix}help <command>` to gain more information about the command',
                color=discord.Color.blurple())
            embed.add_field(name='blacklistadd <word>',
                            value='Add a word to the Blacklist',
                            inline=False)
            embed.add_field(name='blacklistremove <word>',
                            value='Remove a word from the blacklist',
                            inline=False)
            embed.add_field(name='blacklistshow',
                            value='Display the whole blacklist',
                            inline=False)
            embed.add_field(name='blacklistclear',
                            value='Clears the blacklist',
                            inline=False)
            embed.set_footer(text='[] optional | <> required')
            await ctx.send(embed=embed)

        elif str(content) == 'Administration' or str(content) == 'administration':
            embed = discord.Embed(
                description=f'Use `{prefix}help <command>` to gain more information about the command',
                color=discord.Color.blurple())
            embed.add_field(name='setstatus <text>',
                            value='Change the status from the bot',
                            inline=False)
            embed.add_field(name='lock <channel>',
                            value='Lock a channel, so nobody can write in it',
                            inline=False)
            embed.add_field(name='unlock <channel>',
                            value='Unlock a locked channel',
                            inline=False)
            embed.add_field(name='say <text>',
                            value='Gives your text back, with an @everyone at the beginning',
                            inline=False)
            embed.add_field(name='gawrole',
                            value='Create a Giveaway Role, for the giveaway command',
                            inline=False)
            embed.add_field(name='muterole',
                            value='Create a mute Role, required for the mute command',
                            inline=False)
            embed.add_field(name='rules',
                            value='Print a text with rules in a embed!',
                            inline=False)
            embed.set_footer(text='[] optional | <> required')
            await ctx.send(embed=embed)

        elif str(content) == 'Utilities' or str(content) == 'utilities':
            embed = discord.Embed(
                description=f'Use `{prefix}help <command>` to gain more information about the command',
                color=discord.Color.blurple())
            embed.add_field(name='invite',
                            value='Create an invite',
                            inline=False)
            embed.add_field(name='invites <member>',
                            value='Check the invites from a user',
                            inline=False)
            embed.add_field(name='unlock <channel>',
                            value='Unlock a locked channel',
                            inline=False)
            embed.add_field(name='botinvite',
                            value='Gives you two versions of a bots invite link',
                            inline=False)
            embed.add_field(name='embed <text>',
                            value='Create an embed with a specified text',
                            inline=False)
            embed.add_field(name='repeat <text>',
                            value='Repeat what you wrote',
                            inline=False)
            embed.add_field(name='senddm <member> <text>',
                            value='Send a dm to a member from your server',
                            inline=False)
            embed.add_field(name='password',
                            value='Create a random generated password in your dms',
                            inline=False)
            embed.add_field(name='translator <language> <text/word>',
                            value='Translate a text/word you want in any language!',
                            inline=False)
            embed.add_field(name='add <number 1> <number 2>',
                            value='Add two numbers together',
                            inline=False)
            embed.add_field(name='minus <number 1> <number 2>',
                            value='Subtract two numbers with each other',
                            inline=False)
            embed.add_field(name='multiplicate <number 1> <number 2>',
                            value='Multiplicate two numbers with each other',
                            inline=False)
            embed.add_field(name='divide <number 1> <number 2>',
                            value='Divide two numbers trough each other',
                            inline=False)
            embed.set_footer(text='[] optional | <> required')
            await ctx.send(embed=embed)

        elif str(content) == 'Channel' or str(content) == 'channel':
            embed = discord.Embed(
                description=f'Use `{prefix}help <command>` to gain more information about the command',
                color=discord.Color.blurple())
            embed.add_field(name='deletechannel <channel>',
                            value='Delete a text channel',
                            inline=False)
            embed.add_field(name='createchannel <channel_name>',
                            value='Create a text channel with a specific name',
                            inline=False)
            embed.add_field(name='tempchannel <channel_name> <time>',
                            value='Create a text channel with a specific name and time',
                            inline=False)
            embed.set_footer(text='[] optional | <> required')
            await ctx.send(embed=embed)

        elif str(content) == 'Roles' or str(content) == 'roles':
            embed = discord.Embed(
                description=f'Use `{prefix}help <command>` to gain more information about the command',
                color=discord.Color.blurple())
            embed.add_field(name='giverole <member> <role_name>',
                            value='Give an user a role',
                            inline=False)
            embed.add_field(name='removerole <member> <role_name>',
                            value='Remove a role from a user',
                            inline=False)
            embed.add_field(name='create_role <role_name>',
                            value='Create a simple role',
                            inline=False)
            embed.add_field(name='delete_role <role_name>',
                            value='Delete a role on your Server',
                            inline=False)
            embed.add_field(name='getroles [member]',
                            value='Get all roles from a user',
                            inline=False)
            embed.add_field(name='removeroles <member>',
                            value='Remove all roles from a user',
                            inline=False)
            embed.set_footer(text='[] optional | <> required')
            await ctx.send(embed=embed)

        elif str(content) == 'Fun' or str(content) == 'fun':
            embed = discord.Embed(
                description=f'Use `{prefix}help <command>` to gain more information about the command',
                color=discord.Color.blurple())
            embed.add_field(name='8ball <question>',
                            value='Ask the bot a question and he will answer randomly',
                            inline=False)
            embed.add_field(name='slots',
                            value='Play slots',
                            inline=False)
            embed.add_field(name='dice',
                            value='Let a dice roll',
                            inline=False)
            embed.add_field(name='rps <rock, paper or scissors>',
                            value='Play rock paper scissors against the bot',
                            inline=False)
            embed.add_field(name='num_game <number 1-10>',
                            value='Just guess',
                            inline=False)
            embed.add_field(name='simp',
                            value='Random simp rate',
                            inline=False)
            embed.add_field(name='sus',
                            value='Random sus rate',
                            inline=False)
            embed.set_footer(text='[] optional | <> required')
            await ctx.send(embed=embed)

        elif str(content) == 'Info' or str(content) == 'info':
            embed = discord.Embed(
                description=f'Use `{prefix}help <command>` to gain more information about the command',
                color=discord.Color.blurple())
            embed.add_field(name='8ball <question>',
                            value='Ask the bot a question and he will answer randomly',
                            inline=False)
            embed.add_field(name='info [member]',
                            value='Get information about a user from your server',
                            inline=False)
            embed.add_field(name='members',
                            value='Check how many users are in your server',
                            inline=False)
            embed.add_field(name='server',
                            value='Give out information about the server',
                            inline=False)
            embed.add_field(name='joined [member]',
                            value='It\'s your place when you joined',
                            inline=False)
            embed.add_field(name='bot',
                            value='Information about the bot',
                            inline=False)
            embed.add_field(name='avatar [member]',
                            value='Avatar from a user',
                            inline=False)
            embed.set_footer(text='[] optional | <> required')
            await ctx.send(embed=embed)

        elif str(content) == 'Systems' or str(content) == 'systems':
            embed = discord.Embed(
                description=f'Use `{prefix}help <command>` to gain more information about the command',
                color=discord.Color.blurple())
            embed.add_field(name='verify',
                            value='Verify system, which you can use only in a specific channel',
                            inline=False)
            embed.add_field(name='setup',
                            value='Setup system, you can use to set up the bot for your server',
                            inline=False)
            embed.add_field(name='Ticket system',
                            value='-----------------',
                            inline=False)
            embed.add_field(name='new',
                            value='Create a new ticket',
                            inline=False)
            embed.add_field(name='close',
                            value='Close the ticket you type `close` in',
                            inline=False)
            embed.add_field(name='addaccess <role_id>',
                            value='Add access to a role who can "spectate" the ticket (like Supporter role...)',
                            inline=False)
            embed.add_field(name='delaccess <role_id>',
                            value='Remove access from a role',
                            inline=False)
            embed.add_field(name='addpingedrole <role_id>',
                            value='Add a role, that should get pinged when a new ticket get opened',
                            inline=False)
            embed.add_field(name='delpingedrole <role_id>',
                            value='Remove the ping role',
                            inline=False)
            embed.add_field(name='addadminrole <role_id>',
                            value='Add admin-level perms for a role for commands like `?addpingedrole` and `?addaccess`',
                            inline=False)
            embed.add_field(name='deladminrole <role_id>',
                            value='Remove admin-level perms from a role for commands like `?addpingedrole` and `?addaccess`',
                            inline=False)
            embed.set_footer(text='[] optional | <> required')
            await ctx.send(embed=embed)

        elif str(content) == 'Ticket' or str(content) == 'ticket':
            embed = discord.Embed(
                description=f'Use `{prefix}help <command>` to gain more information about the command',
                color=discord.Color.blurple())
            embed.add_field(name='new',
                            value='Create a new ticket',
                            inline=False)
            embed.add_field(name='close',
                            value='Close the ticket you type `close` in',
                            inline=False)
            embed.add_field(name='addaccess <role_id>',
                            value='Add access to a role who can "spectate" the ticket (like Supporter role...)',
                            inline=False)
            embed.add_field(name='delaccess <role_id>',
                            value='Remove access from a role',
                            inline=False)
            embed.add_field(name='addpingedrole <role_id>',
                            value='Add a role, that should get pinged when a new ticket get opened',
                            inline=False)
            embed.add_field(name='delpingedrole <role_id>',
                            value='Remove the ping role',
                            inline=False)
            embed.add_field(name='addadminrole <role_id>',
                            value='Add admin-level perms for a role for commands like `?addpingedrole` and `?addaccess`',
                            inline=False)
            embed.add_field(name='deladminrole <role_id>',
                            value='Remove admin-level perms from a role for commands like `?addpingedrole` and `?addaccess`',
                            inline=False)
            embed.set_footer(text='[] optional | <> required')
            await ctx.send(embed=embed)

        elif str(content) == 'Timers' or str(content) == 'timers':
            embed = discord.Embed(
                description=f'Use `{prefix}help <command>` to gain more information about the command',
                color=discord.Color.blurple())
            embed.add_field(name='reminder <time> [reason]',
                            value='Create a reminder for you',
                            inline=False)
            embed.add_field(name='giveaway <time> <prize>',
                            value='Create a giveaway with reaction stuff',
                            inline=False)
            embed.add_field(name='poll <question>',
                            value='Create a poll with reaction stuff and a question you can decide',
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
