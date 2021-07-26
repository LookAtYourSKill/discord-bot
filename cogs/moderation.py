import asyncio
import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.channel = None
        self.message = None
        self.bot = bot

    @commands.command(description="Mutes the specified user.")
    @commands.has_permissions(manage_messages=True)
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
                                              read_messages=False)

        await member.add_roles(mutedRole, reason=reason)
        embed = discord.Embed(title=f'',
                              description=f'Der User **{member.name}** wurde wegen `{reason}` gemuted!',
                              color=0x4cd137)
        await ctx.send(embed=embed, delete_after=5)

        await ctx.message.delete()  # Delete user's message

        embed = discord.Embed(title=f'',
                              description=f'Du wurdest auf dem Server **{ctx.guild.name}** wegen `{reason}` gemuted!',
                              color=0x4cd137)
        await member.send(embed=embed)

    @commands.command(description="Unmutes a specified user.")
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

        await member.remove_roles(mutedRole)
        embed = discord.Embed(title=f'',
                              description=f'Der User **{member.name}** wurde unmuted!',
                              color=0x4cd137)
        await ctx.send(embed=embed, delete_after=5)

        await ctx.message.delete()  # Delete user's message

        embed = discord.Embed(title=f'',
                              description=f'Du wurdest auf dem Server **{ctx.guild.name}** unmuted!',
                              color=0x4cd137)
        await member.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if ctx.message.author == member.mention:
            embed = discord.Embed(title=' ',
                                  description=f'{member.mention}, du kannst dich **nicht** selbst **bannen**!',
                                  color=0x4cd137, )
            await ctx.send(embed=embed, delete_after=5)
        else:
            await member.ban(reason=reason)
            embed = discord.Embed(title=f'',
                                  description=f'Der User **{member.mention}** wurde wegen `{reason}` gebannt!',
                                  color=0x4cd137)
            await ctx.send(embed=embed, delete_after=5)

            await ctx.message.delete()  # Delete user's message

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

            await ctx.message.delete()  # Delete user's message
            return

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if ctx.message.author == member.mention:
            embed = discord.Embed(title=' ',
                                  description=f'{member.mention}, du kannst dich selbst **nicht kicken**!',
                                  color=0x4cd137, )
            await ctx.send(embed=embed, delete_after=5)
            return

        else:
            await member.kick(reason=reason)

            await ctx.message.delete()  # Delete user's message

            embed = discord.Embed(title=f'',
                                  description=f'Der User **{member.name}** wurde wegen `{reason}` gekickt!',
                                  color=0x4cd137)
            await ctx.send(embed=embed, delete_after=5)

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

            await ctx.message.delete()  # Delete user's message

        else:
            for i in bannedUser:
                embed = discord.Embed(title='**Banned people**',
                                      description=i,
                                      color=0x4cd137)
                await ctx.send(embed=embed, delete_after=5)

    @commands.command(aliases=['purge'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5, channel: discord.TextChannel = None):
        await asyncio.sleep(1)
        await ctx.message.delete()
        await ctx.channel.purge(limit=amount)
        embed = discord.Embed(title=f'',
                              description=f'Es wurden `{amount} Nachrichten` gelöscht',
                              color=0x4cd137)
        await ctx.send(embed=embed, delete_after=5)

    @commands.command(aliases=['sm'])
    async def slowmode(self, ctx, sec: int = None, channel: discord.TextChannel = None):
        if sec == 0:
            embed = discord.Embed(title='',
                                  description='Der Channel hat nun `kein Slowmode mehr`!',
                                  color=0x4cd137)
            await ctx.send(embed = embed, delete_after=5)
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
        await ctx.send(embed=embed, delete_after=5)


def setup(bot):
    bot.add_cog(Moderation(bot))
