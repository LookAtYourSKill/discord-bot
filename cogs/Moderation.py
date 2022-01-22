import asyncio
import datetime
import json
import discord
from discord.ext import commands

with open("./etc/config.json", "r") as f_org:
    config = json.load(f_org)


class moderation(commands.Cog):
    """
    `Moderation commands all you can need`
    """

    def __init__(self, bot):
        self.channel = None
        self.message = None
        self.bot = bot

    @commands.command(name='warn')
    async def warn(self, ctx, member: discord.Member, *, reason=None):
        """
        Warn a user in your server. At 3 Warns the user will get banned!
        """
        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Moderation"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Moderation) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            with open('utils/json/warns.json', 'r+') as f:
                data = json.load(f)

            if str(member.id) not in data[str(ctx.guild.id)]["warns"]:
                data[str(ctx.guild.id)]["warns"][str(member.id)] = {}
                data[str(ctx.guild.id)]["warns"][str(member.id)]["Name"] = str(member)
                data[str(ctx.guild.id)]["warns"][str(member.id)]["Punished By"] = str(ctx.author.id)
                data[str(ctx.guild.id)]["warns"][str(member.id)]["Anzahl der Warns"] = 1
                with open('utils/json/warns.json', 'w') as f:
                    json.dump(data, f, indent=4)

                embed = discord.Embed(title='> Warn System', color=discord.Color.red())
                embed.add_field(
                    name=f'Erste Verwarnung von {member}',
                    value=f':police_car: {member} hat seine **erste Verwarnung**, wegen dem Grund `{reason}` erhalten! :police_car:',
                    inline=False)
                embed.set_footer(text=f'von {ctx.author} auf {ctx.guild.name}')
                await ctx.send(embed=embed)

                channel = self.bot.get_channel(id=config['moderation_log_channel'])
                await channel.send(embed=embed)

            elif data[str(ctx.guild.id)]["warns"][str(member.id)]["Anzahl der Warns"] == 1:
                data[str(ctx.guild.id)]["warns"][str(member.id)]["Anzahl der Warns"] += 1
                with open('utils/json/warns.json', 'w') as f:
                    json.dump(data, f, indent=4)

                embed = discord.Embed(title='> Warn System', color=discord.Color.red())
                embed.add_field(
                    name=f'Zweite Verwarnung von {member}',
                    value=f':police_car: {member} hat seine **zweite Verwarnung**, wegen dem Grund `{reason}` erhalten! :police_car:',
                    inline=False)
                embed.set_footer(text=f'von {ctx.author} auf {ctx.guild.name}')
                await ctx.send(embed=embed)

                channel = self.bot.get_channel(id=config['moderation_log_channel'])
                await channel.send(embed=embed)

            elif data[str(ctx.guild.id)]["warns"][str(member.id)]["Anzahl der Warns"] == 2:
                data[str(ctx.guild.id)]["warns"][str(member.id)]["Anzahl der Warns"] += 1
                with open('utils/json/warns.json', 'w') as f:
                    json.dump(data, f, indent=4)

                embed = discord.Embed(title='> Warn System', color=discord.Color.red())
                embed.add_field(
                    name=f'Dritte Verwarnung von {member}',
                    value=f':police_car: {member} hat seine **dritte Verwarnung und wird somit gebannt**, wegen dem Grund `{reason}`! :police_car:',
                    inline=False)
                embed.set_footer(text=f'von {ctx.author} auf {ctx.guild.name}')
                await ctx.send(embed=embed)

                channel = self.bot.get_channel(id=config['moderation_log_channel'])
                await channel.send(embed=embed)

                await member.ban(reason=reason)

    @commands.command(name='unwarn')
    async def unwarn(self, ctx, *, member: int):
        """
        Here you can unwarn the user you warned before with the warn command
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Moderation"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Moderation) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            member = self.bot.get_user(member)
            with open('utils/json/warns.json', 'r+') as f:
                data = json.load(f)

            if data[str(ctx.guild.id)]["warns"][str(member.id)]["Anzahl der Warns"] == 1:
                data[str(ctx.guild.id)]["warns"][str(member.id)]["Anzahl der Warns"] -= 1
                data[str(ctx.guild.id)]["warns"].pop(str(member.id))
                with open('utils/json/warns.json', 'w') as f:
                    json.dump(data, f, indent=4)

                embed = discord.Embed(title='> Warn System', color=discord.Color.green())
                embed.add_field(name='Keine Verwarnung mehr!',
                                value=f':police_car: {member} hat nun **keine Verwarnung** mehr! :police_car:',
                                inline=False)
                embed.set_footer(text=f'von {ctx.author}')
                await ctx.send(embed=embed)

                channel = self.bot.get_channel(id=config['moderation_log_channel'])
                await channel.send(embed=embed)

            elif data[str(ctx.guild.id)]["warns"][str(member.id)]["Anzahl der Warns"] == 2:
                data[str(ctx.guild.id)]["warns"][str(member.id)]["Anzahl der Warns"] -= 1
                with open('utils/json/warns.json', 'w') as f:
                    json.dump(data, f, indent=4)

                embed = discord.Embed(title='> Warn System', color=discord.Color.orange())
                embed.add_field(name='Eine Verwarnung noch!',
                                value=f':police_car: {member} hat nun noch **eine Verwarnung**! :police_car:',
                                inline=False)
                embed.set_footer(text=f'von {ctx.author}')
                await ctx.send(embed=embed)

                channel = self.bot.get_channel(id=config['moderation_log_channel'])
                await channel.send(embed=embed)

            elif data[str(ctx.guild.id)]["warns"][str(member.id)]["Anzahl der Warns"] == 3:
                try:
                    user = await self.bot.get_user(member.id)
                    if str(member) == str(user):
                        await ctx.guild.unban(user)
                        embed = discord.Embed(title='> Warn System', color=discord.Color.red())
                        embed.add_field(name='Zwei Verwarnung noch!',
                                        value=f':police_car: {member} hat nun noch **zwei Verwarnung** und **wurde entbannt**! :police_car:',
                                        inline=False)
                        embed.set_footer(text=f'von {ctx.author}')
                        await ctx.send(embed=embed)

                        channel = self.bot.get_channel(id=config['moderation_log_channel'])
                        await channel.send(embed=embed)
                        return
                    else:
                        ban_error = discord.Embed(title='__BAN ERROR__',
                                                  description='Der User konnte nicht Entbannt werden!',
                                                  color=discord.Color.green())
                        await ctx.send(embed=ban_error)
                    data[str(ctx.guild.id)]["warns"][str(member.id)]["Anzahl der Warns"] -= 1
                    with open('utils/json/warns.json', 'w') as f:
                        json.dump(data, f, indent=4)

                except discord.Forbidden:
                    unban_error = discord.Embed(title='__ERROR__',
                                                description='Ein Fehler ist aufgetreten!',
                                                color=discord.Color.red())
                    await ctx.send(embed=unban_error)

    @commands.command(name='warns', aliases=['warnings'])
    async def warns(self, ctx, *, member: int):

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Moderation"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Moderation) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            member = self.bot.get_user(member)
            with open('utils/json/warns.json', 'r+') as f:
                data = json.load(f)

            if str(member.id) in data[str(ctx.guild.id)]["warns"]:
                if data[str(ctx.guild.id)]["warns"][str(member.id)]["Anzahl der Warns"] == 1:
                    embed = discord.Embed(title='> Warn System',
                                          description=f':police_car: Der User `{data[str(ctx.guild.id)]["warns"][str(member.id)]["Name"]}` hat **einen Warn!** :police_car:',
                                          color=discord.Color.green())
                    await ctx.send(embed=embed)
                elif data[str(ctx.guild.id)]["warns"][str(member.id)]["Anzahl der Warns"] == 2:
                    embed = discord.Embed(title='> Warn System',
                                          description=f':police_car: Der User `{data[str(ctx.guild.id)]["warns"][str(member.id)]["Name"]}` hat **zwei Warns!** :police_car:',
                                          color=discord.Color.orange())
                    await ctx.send(embed=embed)
                elif data[str(ctx.guild.id)]["warns"][str(member.id)]["Anzahl der Warns"] == 3:
                    embed = discord.Embed(title='> Warn System',
                                          description=f':police_car: Der User `{data[str(ctx.guild.id)]["warns"][str(member.id)]["Name"]}` hat **drei Warns** und **ist bereits gebannt**! :police_car:',
                                          color=discord.Color.red())
                    await ctx.send(embed=embed)
            else:
                embed = discord.Embed(description=f'Der User hat hat entweder keine Warns oder wurde nicht gefunden!')
                await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason):
        """
        Ban a user from your server
        - **?ban [`member`] [`reason`]**
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Moderation"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Moderation) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
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

    @commands.command(name='unban', aliases=['idunban'])
    async def unban(self, ctx, id: int):
        """
        Unban a user from your server but with the id
        - **?unban [`id`]**
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Moderation"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Moderation) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
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
        - **?unbanall**
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Moderation"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Moderation) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
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
        - **?tempban [`member`] [`time`] [`reason`]**

        ``Times:
        "s": second/s
        "m": minute/s
        "h": hour/s
        "d": day/s
        "w": week/s``
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Moderation"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Moderation) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            with open('utils/json/temp_times.json', 'r') as f:
                data = json.load(f)

            punished_time = datetime.datetime.utcnow()

            if time is None:
                embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                      description='Du musst `eine Zeit` angeben!')
                return await ctx.send(embed=embed)

            time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400, "w": 604800}
            tempbantime = int(time[:-1]) * time_convert[time[-1]]

            guild = ctx.guild
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

            data[str(ctx.guild.id)]["tempbans"][str(member.id)] = {}
            data[str(ctx.guild.id)]["tempbans"][str(member.id)]["Name"] = str(member)
            data[str(ctx.guild.id)]["tempbans"][str(member.id)]["Punished By"] = str(ctx.author.id)
            data[str(ctx.guild.id)]["tempbans"][str(member.id)]["Punished At"] = punished_time.strftime(
                "%m/%d/%Y, %H:%M:%S")
            # %m=month, %d=day, %Y=year, %H:=hour:,%M:=minute:, %S=second
            data[str(ctx.guild.id)]["tempbans"][str(member.id)]["Time"] = str(time)
            with open('utils/json/temp_times.json', 'w') as f:
                json.dump(data, f, indent=4)

            await guild.ban(user=member, reason=reason)
            await ctx.send(embed=embed, delete_after=5)
            await ctx.message.delete()  # Delete user's message
            await asyncio.sleep(tempbantime)
            await member.unban()

            data[str(ctx.guild.id)]["tempbans"][str(member.id)] = {}
            data[str(ctx.guild.id)]["tempbans"][str(member.id)]["Name"] = str(member)
            data[str(ctx.guild.id)]["tempbans"][str(member.id)]["Punished By"] = None
            data[str(ctx.guild.id)]["tempbans"][str(member.id)]["Punished At"] = None
            data[str(ctx.guild.id)]["tempbans"][str(member.id)]["Time"] = None
            with open('utils/json/temp_times.json', 'w') as f:
                json.dump(data, f, indent=4)

            channel = self.bot.get_channel(id=config["moderation_log_channel"])
            await channel.send(embed=embed)

    @commands.command(name='banned')
    @commands.has_permissions(ban_members=True)
    async def bannedUserList(self, ctx):
        """
        Display all banned users in chat
        - **?banned**
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Moderation"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Moderation) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
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
                                    value=f'`{i}`',
                                    inline=False)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        """
        Give a user a role, with what the user cant wirte in channels
        - **mute [`member`] [`reason`]**
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Moderation"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Moderation) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
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
        - **?unmute [`member`]**
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Moderation"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Moderation) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
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
    async def tempmute(self, ctx, member: discord.Member, time=None, *, reason='Nicht Angegeben'):
        """
        Mute a user for a specific time
        - **?tempmute [`member`] [`time`] [`reason`]**

        ``Times:
        "s": second/s
        "m": minute/s
        "h": hour/s
        "d": day/s
        "w": week/s``
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Moderation"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Moderation) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            with open('utils/json/temp_times.json', 'r') as f:
                data = json.load(f)

            punished_time = datetime.datetime.utcnow()

            if time is None:
                embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                      description='Du musst `eine Zeit` angeben!')
                return await ctx.send(embed=embed)

            time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400, "w": 604800}
            tempmutetime = int(time[:-1]) * time_convert[time[-1]]
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

            # members_roles = member.roles

            # for i in range(len(members_roles) - 1):
            #    await member.remove_roles(members_roles[i + 1])

            await member.add_roles(mutedRole)
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

            embed = discord.Embed(
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

            data[str(ctx.guild.id)]["tempmutes"][str(member.id)] = {}
            data[str(ctx.guild.id)]["tempmutes"][str(member.id)]["Name"] = str(member)
            data[str(ctx.guild.id)]["tempmutes"][str(member.id)]["Punished By"] = str(ctx.author.id)
            data[str(ctx.guild.id)]["tempmutes"][str(member.id)]["Punished At"] = punished_time.strftime(
                "%m/%d/%Y, %H:%M:%S")
            # %m=month, %d=day, %Y=year, %H:=hour:,%M:=minute:, %S=second
            data[str(ctx.guild.id)]["tempmutes"][str(member.id)]["Time"] = str(time)
            with open('utils/json/temp_times.json', 'w') as f:
                json.dump(data, f, indent=4)

            await asyncio.sleep(tempmutetime)
            await member.remove_roles(mutedRole)

            data[str(ctx.guild.id)]["tempmutes"][str(member.id)] = {}
            data[str(ctx.guild.id)]["tempmutes"][str(member.id)]["Name"] = str(member)
            data[str(ctx.guild.id)]["tempmutes"][str(member.id)]["Punished By"] = None
            data[str(ctx.guild.id)]["tempmutes"][str(member.id)]["Punished At"] = None
            data[str(ctx.guild.id)]["tempmutes"][str(member.id)]["Time"] = None
            with open('utils/json/temp_times.json', 'w') as f:
                json.dump(data, f, indent=4)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """
        Kick a user from your server
        - **?kick [`member`] [`reason`]**
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Moderation"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Moderation) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            if member == ctx.author:
                embed = discord.Embed(description=f'{member.mention}, du kannst dich selbst **nicht kicken**!',
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
        - **?dc [`member`]**
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Moderation"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Moderation) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
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
        - **?clear [`amount`]**
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Moderation"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Moderation) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
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
        - **?nuke [`channel`]**
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Moderation"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Moderation) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
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
        - **?sm [`seconds`]**
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Moderation"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Moderation) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
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
        - **?softban [`member`] [`reason`]**
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Moderation"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Moderation) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
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
        - **?block [`user`]**
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Moderation"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Moderation) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
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
        - **?unblock [`user`]**
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Moderation"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Moderation) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            if not user:
                return await ctx.send("Du musst einen User angeben!")
            embed = discord.Embed(description=f'Der User `{user}` wurde in dem Channel `{ctx.channel}` entblockt!')
            await ctx.send(embed=embed, delete_after=5)
            await ctx.message.delete()
            await ctx.channel.set_permissions(target=user, send_messages=True)


def setup(bot):
    bot.add_cog(moderation(bot))
