import asyncio
import json
import discord
from discord.ext import commands

with open("./config.json", "r") as f:
    config = json.load(f)


class moderation(commands.Cog):
    """
    `Moderation commands all you can need`
    """

    def __init__(self, bot):
        self.channel = None
        self.message = None
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason):
        """
        Ban a user from your server
        """

        if member == ctx.author:
            embed = discord.Embed(title='',
                                  description=f'{member.mention}, du kannst dich **nicht selbst bannen**!',
                                  color=0x4cd137, )
            await ctx.send(embed=embed, delete_after=5)
            await asyncio.sleep(1)
            await ctx.message.delete()
        else:
            await member.ban(reason=reason, delete_message_days=1)
            embed = discord.Embed(title=f'',
                                  description=f'Der User **{member.mention}** wurde wegen `{reason}` gebannt!',
                                  color=0x4cd137)
            embed.add_field(name='**Information**',
                            value=f'Gebannter User : `{member}`\n'
                                  f'User ID : `{member.id}`\n'
                                  f'Reason : `{reason}`\n'
                                  f'Gebannt von : `{ctx.author}`',
                            inline=False)
            await member.send(embed=embed)
            await ctx.send(embed=embed, delete_after=5)
            await ctx.message.delete()

    # @commands.command()
    # @commands.has_permissions(ban_members=True)
    # async def unban(self, ctx, *, member):
    #    """
    #    Unban a user from your server
    #    """

    #    banned_users = await ctx.guild.bans()
    #    member_name, member_discriminator = member.split('#')

    #    for ban_entry in banned_users:
    #        user = ban_entry.user

    #    if (user.name, user.discriminator) == (member_name, member_discriminator):
    #        await ctx.guild.unban(user)
    #        embed = discord.Embed(title=f'',
    #                              description=f'Der User {user.mention} wurde entbannt!',
    #                              color=0x4cd137)
    #        embed.add_field(name='**Information**',
    #                        value=f'Entbannter User : `{user}`\n'
    #                              f'User ID : `{user.id}`\n'
    #                              f'Entbannt von : `{ctx.author}`')
    #        await ctx.send(embed=embed, delete_after=5)
    #        await ctx.message.delete()
    #        return
    #    else:
    #        embed = discord.Embed(title=f'<:close:864599591692009513> **ERROR**',
    #                              description='`Du kannst niemanden entbannen, der nichtmal gebannt ist!`')
    #        await ctx.send(embed=embed, delete_after=5)
    #        await asyncio.sleep(1)
    #        await ctx.message.delete()

    @commands.command(name='unban', aliases=['idunban'])
    async def unban(self, ctx, id: int):
        """
        Unban a user from your server but with the id
        """

        user = await self.bot.fetch_user(id)
        await ctx.guild.unban(user)
        embed = discord.Embed(title=f'',
                              description=f'Der User {user.mention} wurde entbannt!',
                              color=0x4cd137)
        embed.add_field(name='**Information**',
                        value=f'Entbannter User : `{user}`\n'
                              f'User ID : `{user.id}`\n'
                              f'Entbannt von : `{ctx.author}`')
        await ctx.send(embed=embed, delete_after=5)
        await ctx.message.delete()

    @commands.command(name='unbanall', aliases=['uball'])
    @commands.has_permissions(ban_members=True)
    async def mass_unban(self, ctx):
        """
        Unban everybody banned on your server
        """

        ban_list = await ctx.guild.bans()
        for users in ban_list:
            try:
                await ctx.guild.unban(user=users.user)
            except discord.Forbidden:
                pass
        embed = discord.Embed(title='',
                              description='`Unbanned all banned Users`',
                              color=0x4cd137)
        embed.add_field(name='**Information**',
                        value=f'Users to unban : `{len(ban_list)}`\n'
                              f'Entbannt von : `{ctx.author}`')
        await ctx.send(embed=embed, delete_after=5)
        await ctx.message.delete()

        channel = self.bot.get_channel(id=config['moderation_log_channel'])
        await channel.send(embed=embed)

    @commands.command(aliases=['tban'])
    @commands.has_permissions(ban_members=True)
    async def tempban(self, ctx, member: discord.Member, time=None, *, reason='Nicht Angegeben'):
        """
        Ban a user for a specific time
        Times:

        "s": second/s
        "m": minute/s
        "h": hour/s
        "d": day/s
        "w": week/s
        """

        if time is None:
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                  description='Du musst `eine Zeit` angeben!')
            return await ctx.send(embed=embed)
        if reason is None:
            reason = 'Nicht angegeben'
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                  description='Die `Reason` is nicht angegeben!\n'
                                              f'Sie wurde **automatisch auf {reason} gesetzt!**')
            return await ctx.send(embed=embed)
        time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400, "w": 604800}
        tempbantime = int(time[:-1]) * time_convert[time[-1]]
        guild = ctx.guild
        await guild.ban(reason=reason)
        embed = discord.Embed(title=f'',
                              description=f'Der User **{member.name}** wurde für `{time}` wegen `{reason}` gebannt!',
                              color=0x4cd137)
        embed.add_field(name='**Information**',
                        value=f'Gebannter User : `{member}`\n'
                              f'User ID : `{member.id}`\n'
                              f'Reason : `{reason}`\n'
                              f'Time : `{time}`\n'
                              f'Gebannt von : `{ctx.author}`',
                        inline=False)
        await member.send(embed=embed)
        await ctx.send(embed=embed, delete_after=5)
        await ctx.message.delete()  # Delete user's message
        await asyncio.sleep(tempbantime)
        await member.unban()

        channel = self.bot.get_channel(id=config["moderation_log_channel"])
        await channel.send(embed=embed)

    @commands.command(name='banned')
    @commands.has_permissions(ban_members=True)
    async def bannedUserList(self, ctx):
        """
        Display all banned users in chat
        """

        bannedUser = await ctx.guild.bans()
        if not bannedUser:
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                  description='`Auf diesem Server ist niemand gebannt!`',
                                  color=0x4cd137)
            await ctx.send(embed=embed, delete_after=5)
            await ctx.message.delete()
        else:
            embed = discord.Embed(title='Banned User Check')
            for i in bannedUser:
                embed.add_field(name='User',
                                value=f'{i}',
                                inline=False)
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        """
        Give a user a role, with what the user cant wirte in channels
        """

        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")
        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")
            for channel in guild.channels:
                await channel.set_permissions(mutedRole,
                                              speak=False,
                                              send_messages=False,
                                              read_message_history=False,
                                              read_messages=False
                                              )

        members_roles = member.roles

        for i in range(len(members_roles) - 1):
            await member.remove_roles(members_roles[i + 1])

        await member.add_roles(mutedRole, reason=reason)
        embed = discord.Embed(title=f'',
                              description=f'Der User **{member.name}** wurde wegen `{reason}` gemuted!',
                              color=0x4cd137)
        embed.add_field(name='**Information**',
                        value=f'Muted User : `{member}`\n'
                              f'User ID : `{member.id}`\n'
                              f'Reason : `{reason}`\n'
                              f'Muted von : `{ctx.author}`',
                        inline=False)
        await ctx.send(embed=embed, delete_after=5)
        await ctx.message.delete()

        channel = self.bot.get_channel(id=config['moderation_log_channel'])
        await channel.send(embed=embed)

        embed = discord.Embed(title=f'',
                              description=f'Du wurdest auf dem Server **{ctx.guild.name}** wegen `{reason}` gemuted!',
                              color=0x4cd137)
        embed.add_field(name='**Information**',
                        value=f'Muted User : `{member}`\n'
                              f'User ID : `{member.id}`\n'
                              f'Reason : `{reason}`\n'
                              f'Muted von : `{ctx.author}`',
                        inline=False)
        await member.send(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, member: discord.Member):
        """
        Remove the mute role from the user
        """

        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(mutedRole)
        embed = discord.Embed(title=f'',
                              description=f'Der User **{member.name}** wurde unmuted!',
                              color=0x4cd137)
        embed.add_field(name='**Information**',
                        value=f'Unmuted User : `{member}`\n'
                              f'User ID : `{member.id}`\n'
                              f'Unmuted von : `{ctx.author}`',
                        inline=False)
        await ctx.send(embed=embed, delete_after=5)
        await ctx.message.delete()

        channel = self.bot.get_channel(id=config['moderation_log_channel'])
        await channel.send(embed=embed)

        embed = discord.Embed(title=f'',
                              description=f'Du wurdest auf dem Server **{ctx.guild.name}** unmuted!',
                              color=0x4cd137)
        embed.add_field(name='**Information**',
                        value=f'Unmuted User : `{member}`\n'
                              f'User ID : `{member.id}`\n'
                              f'Unmuted von : `{ctx.author}`',
                        inline=False)
        await member.send(embed=embed)

    @commands.command(aliases=['tmute'])
    @commands.has_permissions(kick_members=True)
    async def tempmute(self, ctx, member: discord.Member, time=None, *, reason=None):
        """
        Mute a user for a specific time
        Times:

        "s": second/s
        "m": minute/s
        "h": hour/s
        "d": day/s
        "w": week/s
        """

        if time is None:
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                  description='Du musst `eine Zeit` angeben!')
            return await ctx.send(embed=embed)

        time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400, "w": 604800}
        tempmutetime = int(time[:-1]) * time_convert[time[-1]]
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if reason is None:
            reason = 'Nicht Angegeben'
            embed = discord.Embed(description='Du hast kein Grund angegeben!\n'
                                              f'Er wurde **automatisch auf {reason} gesetzt!**')
            await ctx.author.send(embed=embed)

            members_roles = member.roles

            for i in range(len(members_roles) - 1):
                await member.remove_roles(members_roles[i + 1])

            await member.add_roles(mutedRole, reason=reason)

            embed = discord.Embed(title=f'',
                                  description=f'Der User **{member.name}** wurde für `{time}` wegen `{reason}` gemuted!',
                                  color=0x4cd137)
            embed.add_field(name='**Information**',
                            value=f'Tempmuted User : `{member}`\n'
                                  f'User ID : `{member.id}`\n'
                                  f'Reason : `{reason}`\n'
                                  f'Time : `{time}`\n'
                                  f'Tempmuted von : `{ctx.author}`',
                            inline=False)
            await ctx.send(embed=embed, delete_after=5)
            await ctx.message.delete()

            channel = self.bot.get_channel(id=config['moderation_log_channel'])
            await channel.send(embed=embed)

            embed = discord.Embed(title=f'',
                                  description=f'Du wurdest auf dem Server **{ctx.guild.name}** für `{time}` wegen `{reason}` gemuted!',
                                  color=0x4cd137)
            embed.add_field(name='**Information**',
                            value=f'Tempmuted User : `{member}`\n'
                                  f'User ID : `{member.id}`\n'
                                  f'Reason : `{reason}`\n'
                                  f'Time : `{time}`\n'
                                  f'Tempmuted von : `{ctx.author}`',
                            inline=False)
            await member.send(embed=embed)

            await asyncio.sleep(tempmutetime)
            await member.remove_roles(mutedRole)
            return

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")
            for channel in guild.channels:
                await channel.set_permissions(mutedRole,
                                              speak=False,
                                              send_messages=False,
                                              read_message_history=False,
                                              read_messages=False
                                              )

        members_roles = member.roles

        for i in range(len(members_roles) - 1):
            await member.remove_roles(members_roles[i + 1])

        await member.add_roles(mutedRole, reason=reason)
        embed = discord.Embed(title=f'',
                              description=f'Der User **{member.name}** wurde für `{time}` wegen `{reason}` gemuted!',
                              color=0x4cd137)
        embed.add_field(name='**Information**',
                        value=f'Tempmuted User : `{member}`\n'
                              f'User ID : `{member.id}`\n'
                              f'Reason : `{reason}`\n'
                              f'Time : `{time}`\n'
                              f'Tempmuted von : `{ctx.author}`',
                        inline=False)
        await ctx.send(embed=embed, delete_after=5)
        await ctx.message.delete()

        channel = self.bot.get_channel(id=config['moderation_log_channel'])
        await channel.send(embed=embed)

        embed = discord.Embed(title=f'',
                              description=f'Du wurdest auf dem Server **{ctx.guild.name}** für `{time}` wegen `{reason}` gemuted!',
                              color=0x4cd137)
        embed.add_field(name='**Information**',
                        value=f'Tempmuted User : `{member}`\n'
                              f'User ID : `{member.id}`\n'
                              f'Reason : `{reason}`\n'
                              f'Time : `{time}`\n'
                              f'Tempmuted von : `{ctx.author}`',
                        inline=False)
        await member.send(embed=embed)
        await asyncio.sleep(tempmutetime)
        await member.remove_roles(mutedRole)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """
        Kick a user from your server
        """

        if member == ctx.author:
            embed = discord.Embed(title=' ',
                                  description=f'{member.mention}, du kannst dich selbst **nicht kicken**!',
                                  color=0x4cd137)
            await ctx.send(embed=embed, delete_after=5)
            await asyncio.sleep(1)
            await ctx.message.delete()
            return

        else:
            await member.kick(reason=reason)
            embed = discord.Embed(title=f'',
                                  description=f'Der User **{member.name}** wurde wegen `{reason}` gekickt!',
                                  color=0x4cd137)
            embed.add_field(name='**Information**',
                            value=f'Kicked User : `{member}`\n'
                                  f'User ID : `{member.id}`\n'
                                  f'Reason : `{reason}`\n'
                                  f'Gekickt von : `{ctx.author}`',
                            inline=False)
            await ctx.send(embed=embed, delete_after=5)
            await ctx.message.delete()

    @commands.command(name='dc', aliases=['vckick', 'vc'])
    @commands.has_permissions(kick_members=True)
    async def vc_kick(self, ctx, member: discord.Member):
        """
        Disconnect a user from the vc, if he is in one
        """

        await member.edit(voice_channel=None)
        embed = discord.Embed(title='',
                              description=f'**{member}** wurde `aus dem Voice Channel gekickt!`',
                              color=0xff00c8)
        embed.add_field(name='**Information**',
                        value=f'Disconnected User : `{member}`\n'
                              f'User ID : `{member.id}`\n'
                              f'Disconnected von : `{ctx.author}`',
                        inline=False)
        await ctx.send(embed=embed, delete_after=5)
        await asyncio.sleep(1)
        await ctx.message.delete()

        channel = self.bot.get_channel(id=config['moderation_log_channel'])
        await channel.send(embed=embed)

    @commands.command(name='clear', aliases=['purge'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        """
        Clear an amount of messages
        """

        await asyncio.sleep(1)
        await ctx.message.delete()
        await ctx.channel.purge(limit=amount)
        channel = ctx.channel
        embed = discord.Embed(title=f'',
                              description=f'Es wurden `{amount} Nachrichten` gelöscht',
                              color=0x4cd137)
        embed.add_field(name='**Information**',
                        value=f'Nachrichten gelöscht : `{amount}`\n'
                              f'Channel Name : `{channel.name}`\n'
                              f'Channel ID : `{channel.id}`\n'
                              f'Nachrichten gelöscht von : `{ctx.author}`',
                        inline=False)
        await ctx.send(embed=embed, delete_after=5)

        channel = self.bot.get_channel(id=config['moderation_log_channel'])
        await channel.send(embed=embed)

    @commands.command(name='nuke')
    @commands.has_permissions(manage_channels=True)
    async def nuke(self, ctx, channel: discord.TextChannel = None):
        """
        If in a channel is too much spam, you nuke the channel. It will be cloned automatically
        """

        if not channel:
            nuke_channel = ctx.channel
            new_channel = await nuke_channel.clone(reason="Has been Nuked!")
            await nuke_channel.delete()
            embed = discord.Embed(title='<:open:869959941321011260> **Successful**',
                                  description='This Channel **has been Nuked!**',
                                  color=discord.Color.random())
            embed.add_field(name='**Information**',
                            value=f'Channel Name : `{channel.name}`\n'
                                  f'Channel ID : `{channel.id}`\n'
                                  f'Channel Nuked von : `{ctx.author}`',
                            inline=False)
            await new_channel.send(embed=embed, delete_after=5)

            channel = self.bot.get_channel(id=config['moderation_log_channel'])
            await channel.send(embed=embed)

        nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

        if nuke_channel is not None:
            new_channel = await nuke_channel.clone(reason="Has been Nuked!")
            await nuke_channel.delete()
            embed = discord.Embed(title='<:open:869959941321011260> **Successful**',
                                  description='This Channel **has been Nuked!**',
                                  color=discord.Color.random())
            embed.add_field(name='**Information**',
                            value=f'Channel Name : `{channel.name}`\n'
                                  f'Channel ID : `{channel.id}`\n'
                                  f'Channel Nuked von : `{ctx.author}`',
                            inline=False)
            await new_channel.send(embed=embed, delete_after=5)

            channel = self.bot.get_channel(id=config['moderation_log_channel'])
            await channel.send(embed=embed)

        else:
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                  description=f'**No channel** named **{channel.name} was found!**')
            await ctx.send(embed=embed)

    @commands.command(name='slowmode', aliases=['sm'])
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self, ctx, sec: int = None):
        """
        Add or remove a slowmode from a channel
        """

        if sec == 0:
            channel = ctx.channel
            await channel.edit(slowmode_delay=0)
            embed = discord.Embed(title='',
                                  description='Der Channel hat nun `kein Slowmode mehr`!',
                                  color=0x4cd137)
            embed.add_field(name='**Information**',
                            value=f'Channel Name : `{channel.name}`\n'
                                  f'Channel ID : `{channel.id}`\n'
                                  f'Sekunden : `{sec} Sekunden`\n'
                                  f'Slowmode deaktiviert von : `{ctx.author}`',
                            inline=False)
            await ctx.send(embed=embed, delete_after=5)

            channel = self.bot.get_channel(id=config['moderation_log_channel'])
            await channel.send(embed=embed)

        else:
            channel = ctx.channel
            await channel.edit(slowmode_delay=sec)
            embed = discord.Embed(title=f'',
                                  description=f'Der Channel **{channel.name}** hat einen Slowmode von `{sec} Sekunden`!',
                                  color=0x4cd137)
            embed.add_field(name='**Information**',
                            value=f'Channel Name : `{channel.name}`\n'
                                  f'Channel ID : `{channel.id}`\n'
                                  f'Sekunden : `{sec} Sekunden`\n'
                                  f'Slowmode aktiviert von : `{ctx.author}`',
                            inline=False)
            await asyncio.sleep(1)
            await ctx.message.delete()
            await ctx.send(embed=embed, delete_after=5)

            channel = self.bot.get_channel(id=config['moderation_log_channel'])
            await channel.send(embed=embed)

    @commands.command(name='softban')
    @commands.has_permissions(ban_members=True)
    async def softban(self, ctx, member: discord.Member, *, reason=None):
        """
        The softban is for people, which send Scam/Fishing or invite links. When you softban them they'll get kicked and the messages deleted
        """

        invite = await ctx.channel.create_invite(max_uses=1)
        if not member:
            await ctx.send('Du musst einen User angeben!')
        else:
            embed = discord.Embed(description=f'Der User `{member}` wurde wegen `{reason}` gekickt!')
            await ctx.send(embed=embed, delete_after=5)
            await ctx.message.delete()

            member_embed = discord.Embed(
                description=f'Du wurdest von dem Server `{ctx.guild.name}` wegen `{reason}` gekickt!\n'
                            f'\n'
                            f'**Was ist überhaupt dieser Softban?**\n'
                            f'-> Du wurdest gekickt(gebannt und direkt wieder entbannt), damit all deine Nachrichten gelöscht werden.\n'
                            f'\n'
                            f'Hier ist ein Invite zum Server: [Invite]({invite}).')
            await member.send(embed=member_embed)

            await member.ban(reason=reason, delete_message_days=1)
            await member.unban()

    @commands.command(name='block')
    @commands.has_permissions(manage_channels=True)
    async def block(self, ctx, user: discord.Member = None):
        """
        Block a user from chatting in the channel you use the command in
        """

        if not user:
            return await ctx.send("Du musst einen User angeben!")
        embed = discord.Embed(description=f'Der User `{user}` wurde in dem Channel `{ctx.channel}` geblockt!')
        await ctx.send(embed=embed, delete_after=5)
        await ctx.message.delete()
        await ctx.channel.set_permissions(target=user, send_messages=False)

    @commands.command(name='unblock')
    @commands.has_permissions(manage_channels=True)
    async def unblock(self, ctx, user: discord.Member = None):
        """
        Unblock the user you blocked before in the channel you wrote the block command
        """

        if not user:
            return await ctx.send("Du musst einen User angeben!")
        embed = discord.Embed(description=f'Der User `{user}` wurde in dem Channel `{ctx.channel}` entblockt!')
        await ctx.send(embed=embed, delete_after=5)
        await ctx.message.delete()
        await ctx.channel.set_permissions(target=user, send_messages=True)


def setup(bot):
    bot.add_cog(moderation(bot))