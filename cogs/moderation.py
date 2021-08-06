import asyncio
import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.channel = None
        self.message = None
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if member == ctx.author:
            embed = discord.Embed(title='',
                                  description=f'{member.mention}, du kannst dich **nicht selbst bannen**!',
                                  color=0x4cd137, )
            await ctx.send(embed=embed, delete_after=5)
            await asyncio.sleep(1)
            await ctx.message.delete()
        else:
            await member.ban(reason=reason)
            embed = discord.Embed(title=f'',
                                  description=f'Der User **{member.mention}** wurde wegen `{reason}` gebannt!',
                                  color=0x4cd137)
            embed.add_field(name='**Information**',
                            value=f'Gebannter User : `{member.mention}`\n'
                                  f'User ID : `{member.id}`\n'
                                  f'Reason : `{reason}`\n'
                                  f'Gebannt von : `{ctx.author}`',
                            inline=False)
            await ctx.send(embed=embed, delete_after=5)
            await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            embed = discord.Embed(title=f'',
                                  description=f'Der User {user.mention} wurde entbannt!',
                                  color=0x4cd137)
            await ctx.send(embed=embed, delete_after=5)
            await ctx.message.delete()
            return
        else:
            embed = discord.Embed(title=f'<:close:864599591692009513> **ERROR**',
                                  description='`Du kannst niemanden entbannen, der nichtmal gebannt ist!`')
            await ctx.send(embed=embed, delete_after=5)
            await asyncio.sleep(1)
            await ctx.message.delete()

    @commands.command(aliases=['tban'])
    @commands.has_permissions(ban_members=True)
    async def tempban(self, ctx, member: discord.Member, time=None, reason=None):
        if time is None:
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                  description='Du musst `eine Zeit` angeben!')
            return await ctx.send(embed=embed)
        if reason is None:
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                  description='Die `Reason` is nicht angegeben!')
            return await ctx.send(embed=embed)
        time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400, "w": 604800, "m": 2629743, "y": 31556926}
        tempbantime = int(time[0]) * time_convert[time[-1]]
        guild = ctx.guild
        await member.ban(reason=reason)
        embed = discord.Embed(title=f'',
                              description=f'Der User **{member.name}** wurde für `{time}` wegen `{reason}` gebannt!',
                              color=0x4cd137)
        embed.add_field(name='**Information**',
                        value=f'Gebannter User : `{member}`\n'
                              f'User ID : `{member.id}`\n'
                              f'Reason : `{reason}`\n'
                              f'Time : {time}\n'
                              f'Gebannt von : `{ctx.author}`',
                        inline=False)
        await ctx.send(embed=embed, delete_after=5)
        await ctx.message.delete()  # Delete user's message
        await asyncio.sleep(tempbantime)
        await member.unban()

    @commands.command(aliases=['banned'])
    @commands.has_permissions(ban_members=True)
    async def bannedUserList(self, ctx):
        empty = []
        bannedUser = await ctx.guild.bans()
        if bannedUser == empty:
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                  description='`Die Banlist ist leer`!',
                                  color=0x4cd137)
            await ctx.send(embed=embed, delete_after=5)
            await ctx.message.delete()
        else:
            for i in bannedUser:
                embed = discord.Embed(title='**Banned people**',
                                      description=i,
                                      color=0x4cd137)
                await ctx.send(embed=embed, delete_after=5)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
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
        embed = discord.Embed(title=f'',
                              description=f'Du wurdest auf dem Server **{ctx.guild.name}** wegen `{reason}` gemuted!',
                              color=0x4cd137)
        await member.send(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(mutedRole)
        embed = discord.Embed(title=f'',
                              description=f'Der User **{member.name}** wurde unmuted!',
                              color=0x4cd137)
        await ctx.send(embed=embed, delete_after=5)
        await ctx.message.delete()
        embed = discord.Embed(title=f'',
                              description=f'Du wurdest auf dem Server **{ctx.guild.name}** unmuted!',
                              color=0x4cd137)
        await member.send(embed=embed)

    @commands.command()
    async def setMute(self, ctx):
        role = discord.utils.get(ctx.guild.roles, name="muted")
        guild = ctx.guild
        if role not in guild.roles:
            perms = discord.Permissions(send_messages=False, speak=False, read_messages=True, read_message_history=True)
            await guild.create_role(name="muted", permissions=perms)

    @commands.command(aliases=['tmute'])
    @commands.has_permissions(kick_members=True)
    async def tempmute(self, ctx, member: discord.Member, time=None, reason=None):
        if time is None:
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                  description='Du musst `eine Zeit` angeben!')
            return await ctx.send(embed=embed)
        if reason is None:
            embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                  description='Die `Reason` is nicht angegeben!')
            return await ctx.send(embed=embed)

        time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400, "w": 604800, "m": 2629743, "y": 31556926}
        tempmutetime = int(time[0]) * time_convert[time[-1]]
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
        await member.add_roles(mutedRole, reason=reason)
        embed = discord.Embed(title=f'',
                              description=f'Der User **{member.name}** wurde für `{time}` wegen `{reason}` gemuted!',
                              color=0x4cd137)
        embed.add_field(name='**Information**',
                        value=f'Tempmuted User : `{member}`\n'
                              f'User ID : `{member.id}`\n'
                              f'Reason : `{reason}`\n'
                              f'Time : {time}\n'
                              f'Tempmuted von : `{ctx.author}`',
                        inline=False)
        await ctx.send(embed=embed, delete_after=5)
        await ctx.message.delete()

        embed = discord.Embed(title=f'',
                              description=f'Du wurdest auf dem Server **{ctx.guild.name}** für `{time}` wegen `{reason}` gemuted!',
                              color=0x4cd137)
        embed.add_field(name='**Information**',
                        value=f'Tempmuted User : `{member}`\n'
                              f'User ID : `{member.id}`\n'
                              f'Reason : `{reason}`\n'
                              f'Time : {time}\n'
                              f'Tempmuted von : `{ctx.author}`',
                        inline=False)
        await member.send(embed=embed)
        await asyncio.sleep(tempmutetime)
        await member.remove_roles(mutedRole)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
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
            await ctx.message.delete()
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

    @commands.command(aliases=['purge'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, channel,  ctx, amount=5):
        await asyncio.sleep(1)
        await ctx.message.delete()
        await ctx.channel.purge(limit=amount)
        embed = discord.Embed(title=f'',
                              description=f'Es wurden `{amount} Nachrichten` gelöscht',
                              color=0x4cd137)
        embed.add_field(name='**Information**',
                        value=f'Nachrichten gelöscht : `{amount}`\n'
                              f'Channel Name : `{channel.name}`\n'
                              f'Channel ID : `{channel.id}`'
                              f'Nachrichten gelöscht von : `{ctx.author}`',
                        inline=False)
        await ctx.send(embed=embed, delete_after=5)

    @commands.command(aliases=['sm'])
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self, ctx, sec: int = None, channel: discord.TextChannel = None):
        if sec == 0:
            embed = discord.Embed(title='',
                                  description='Der Channel hat nun `kein Slowmode mehr`!',
                                  color=0x4cd137)
            await ctx.send(embed=embed, delete_after=5)
        if not sec:
            sec = 0
        if not channel:
            channel = ctx.channel
        await channel.edit(slowmode_delay=sec)
        await asyncio.sleep(1)
        await ctx.message.delete()
        embed = discord.Embed(title=f'',
                              description=f'Der Channel **{channel.name}** hat einen Slowmode von `{sec} Sekunden`!',
                              color=0x4cd137)
        embed.add_field(name='**Information**',
                        value=f'Channel Name : `{channel.name}`\n'
                              f'Channel ID : `{channel.id}`\n'
                              f'Sekunden : `{sec} Sekunden`\n'
                              f'Slowmode aktiviert von : `{ctx.author}`',
                        inline=False)
        await ctx.send(embed=embed, delete_after=5)


def setup(bot):
    bot.add_cog(Moderation(bot)
                )
