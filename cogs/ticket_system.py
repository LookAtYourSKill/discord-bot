import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import json
import asyncio


class ticket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def new(self, ctx, *, args=None):
        """
        Creating a new ticket
        """

        await self.bot.wait_until_ready()

        if args is None:
            message_content = "Please wait, we will be with you shortly!"

        else:
            message_content = "".join(args)

        with open("./utils/json/ticket_data.json") as f:
            data = json.load(f)

        ticket_number = int(data["ticket-counter"])
        ticket_number += 1

        ticket_channel = await ctx.guild.create_text_channel(f"ticket-{ticket_number}")
        await ticket_channel.set_permissions(ctx.guild.get_role(ctx.guild.id), send_messages=False, read_messages=False)

        for role_id in data["valid-roles"]:
            role = ctx.guild.get_role(role_id)

            await ticket_channel.set_permissions(role, send_messages=True, read_messages=True, add_reactions=True,
                                                 embed_links=True, attach_files=True, read_message_history=True,
                                                 external_emojis=True)

        await ticket_channel.set_permissions(ctx.author, send_messages=True, read_messages=True, add_reactions=True,
                                             embed_links=True, attach_files=True, read_message_history=True,
                                             external_emojis=True)

        em = discord.Embed(title=f"New ticket from {ctx.author.name}#{ctx.author.discriminator}",
                           description=f"{message_content}",
                           color=0x00a8ff)

        await ticket_channel.send(embed=em)

        pinged_msg_content = ""
        non_mentionable_roles = []

        if data["pinged-roles"]:

            for role_id in data["pinged-roles"]:
                role = ctx.guild.get_role(role_id)

                pinged_msg_content += role.mention
                pinged_msg_content += " "

                if role.mentionable:
                    pass
                else:
                    await role.edit(mentionable=True)
                    non_mentionable_roles.append(role)

            await ticket_channel.send(pinged_msg_content)

            for role in non_mentionable_roles:
                await role.edit(mentionable=False)

        data["ticket-channel-ids"].append(ticket_channel.id)

        data["ticket-counter"] = int(ticket_number)
        with open("./utils/json/ticket_data.json", 'w') as f:
            json.dump(data, f)

        created_em = discord.Embed(title="Ticket System",
                                   description=f"Your ticket has been created at {ticket_channel.mention}",
                                   color=0x00a8ff)

        await ctx.send(embed=created_em, delete_after=5)
        await ctx.message.delete()

    @commands.command()
    async def close(self, ctx):
        """
        Close the ticket, where you write it in!
        """

        with open('./utils/json/ticket_data.json') as f:
            data = json.load(f)

        if ctx.channel.id in data["ticket-channel-ids"]:

            channel_id = ctx.channel.id

            def check(message):
                return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() == "close"

            try:

                em = discord.Embed(title="Ticket System",
                                   description="Are you sure you want to close this ticket? Reply with `close` if you are sure.",
                                   color=0x00a8ff)

                await ctx.send(embed=em)
                await self.bot.wait_for('message', check=check, timeout=60)
                await ctx.channel.delete()

                index = data["ticket-channel-ids"].index(channel_id)
                del data["ticket-channel-ids"][index]

                with open('./utils/json/ticket_data.json', 'w') as f:
                    json.dump(data, f)

            except asyncio.TimeoutError:
                em = discord.Embed(title="Auroris Tickets",
                                   description="You have run out of time to close this ticket. Please run the command again.",
                                   color=0x00a8ff)
                await ctx.send(embed=em)

    @commands.command()
    async def addaccess(self, ctx, role_id=None):
        """
        Add a role to the access roles for the tickets
        """

        with open('./utils/json/ticket_data.json') as f:
            data = json.load(f)

        valid_user = False

        for role_id in data["verified-roles"]:
            try:
                if ctx.guild.get_role(role_id) in ctx.author.roles:
                    valid_user = True
            except discord.Forbidden:
                pass

        if valid_user or ctx.author.guild_permissions.administrator:
            role_id = int(role_id)

            if role_id not in data["valid-roles"]:

                try:
                    role = ctx.guild.get_role(role_id)

                    with open("./utils/json/ticket_data.json") as f:
                        data = json.load(f)

                    data["valid-roles"].append(role_id)

                    with open('./utils/json/ticket_data.json', 'w') as f:
                        json.dump(data, f)

                    em = discord.Embed(title="Ticket System",
                                       description=f"You have successfully added `{role.name}` to the list of roles with access to tickets.",
                                       color=0x00a8ff)

                    await ctx.send(embed=em)

                except discord.Forbidden:
                    em = discord.Embed(title="Ticket System",
                                       description="That isn't a valid role ID. Please try again with a valid role ID.")
                    await ctx.send(embed=em)

            else:
                em = discord.Embed(title="Ticket System",
                                   description="That role already has access to tickets!",
                                   color=0x00a8ff)
                await ctx.send(embed=em)

        else:
            em = discord.Embed(title="Ticket System",
                               description="Sorry, you don't have permission to run that command.",
                               color=0x00a8ff)
            await ctx.send(embed=em)

    @commands.command()
    async def delaccess(self, ctx, role_id=None):
        with open('./utils/json/ticket_data.json') as f:
            data = json.load(f)

        valid_user = False

        for role_id in data["verified-roles"]:
            try:
                if ctx.guild.get_role(role_id) in ctx.author.roles:
                    valid_user = True
            except discord.Forbidden:
                pass

        if valid_user or ctx.author.guild_permissions.administrator:

            try:
                role_id = int(role_id)
                role = ctx.guild.get_role(role_id)

                with open("./utils/json/ticket_data.json") as f:
                    data = json.load(f)

                valid_roles = data["valid-roles"]

                if role_id in valid_roles:
                    index = valid_roles.index(role_id)

                    del valid_roles[index]

                    data["valid-roles"] = valid_roles

                    with open('./utils/json/ticket_data.json', 'w') as f:
                        json.dump(data, f)

                    em = discord.Embed(title="Ticket System",
                                       description=f"You have successfully removed `{role.name}` from the list of roles with access to tickets.",
                                       color=0x00a8ff)

                    await ctx.send(embed=em)

                else:

                    em = discord.Embed(title="Ticket System",
                                       description="That role already doesn't have access to tickets!", color=0x00a8ff)
                    await ctx.send(embed=em)

            except discord.Forbidden:
                em = discord.Embed(title="Ticket System",
                                   description="That isn't a valid role ID. Please try again with a valid role ID.")
                await ctx.send(embed=em)

        else:
            em = discord.Embed(title="Ticket System",
                               description="Sorry, you don't have permission to run that command.",
                               color=0x00a8ff)
            await ctx.send(embed=em)

    @commands.command()
    async def addpingedrole(self, ctx, role_id=None):
        with open('./utils/json/ticket_data.json') as f:
            data = json.load(f)

        valid_user = False

        for role_id in data["verified-roles"]:
            try:
                if ctx.guild.get_role(role_id) in ctx.author.roles:
                    valid_user = True
            except discord.Forbidden:
                pass

        if valid_user or ctx.author.guild_permissions.administrator:

            role_id = int(role_id)

            if role_id not in data["pinged-roles"]:

                try:
                    role = ctx.guild.get_role(role_id)

                    with open("./utils/json/ticket_data.json") as f:
                        data = json.load(f)

                    data["pinged-roles"].append(role_id)

                    with open('./utils/json/ticket_data.json', 'w') as f:
                        json.dump(data, f)

                    em = discord.Embed(title="Ticket System",
                                       description=f"You have successfully added `{role.name}` to the list of roles that get pinged when new tickets are created!",
                                       color=0x00a8ff)

                    await ctx.send(embed=em)

                except discord.Forbidden:
                    em = discord.Embed(title="Ticket System",
                                       description="That isn't a valid role ID. Please try again with a valid role ID.")
                    await ctx.send(embed=em)

            else:
                em = discord.Embed(title="Ticket System",
                                   description="That role already receives pings when tickets are created.",
                                   color=0x00a8ff)
                await ctx.send(embed=em)

        else:
            em = discord.Embed(title="Ticket System",
                               description="Sorry, you don't have permission to run that command.",
                               color=0x00a8ff)
            await ctx.send(embed=em)

    @commands.command()
    async def delpingedrole(self, ctx, role_id=None):
        with open('./utils/json/ticket_data.json') as f:
            data = json.load(f)

        valid_user = False

        for role_id in data["verified-roles"]:
            try:
                if ctx.guild.get_role(role_id) in ctx.author.roles:
                    valid_user = True
            except discord.Forbidden:
                pass

        if valid_user or ctx.author.guild_permissions.administrator:

            try:
                role_id = int(role_id)
                role = ctx.guild.get_role(role_id)

                with open("./utils/json/ticket_data.json") as f:
                    data = json.load(f)

                pinged_roles = data["pinged-roles"]

                if role_id in pinged_roles:
                    index = pinged_roles.index(role_id)

                    del pinged_roles[index]

                    data["pinged-roles"] = pinged_roles

                    with open('./utils/json/ticket_data.json', 'w') as f:
                        json.dump(data, f)

                    em = discord.Embed(title="Ticket System",
                                       description=f"You have successfully removed `{role.name}` from the list of roles that get pinged when new tickets are created.",
                                       color=0x00a8ff)
                    await ctx.send(embed=em)

                else:
                    em = discord.Embed(title="Ticket System",
                                       description="That role already isn't getting pinged when new tickets are created!",
                                       color=0x00a8ff)
                    await ctx.send(embed=em)

            except discord.Forbidden:
                em = discord.Embed(title="Ticket System",
                                   description="That isn't a valid role ID. Please try again with a valid role ID.")
                await ctx.send(embed=em)

        else:
            em = discord.Embed(title="Ticket System",
                               description="Sorry, you don't have permission to run that command.",
                               color=0x00a8ff)
            await ctx.send(embed=em)

    @commands.command()
    @has_permissions(administrator=True)
    async def addadminrole(self, ctx, role_id=None):
        try:
            role_id = int(role_id)
            role = ctx.guild.get_role(role_id)

            with open("./utils/json/ticket_data.json") as f:
                data = json.load(f)

            data["verified-roles"].append(role_id)

            with open('./utils/json/ticket_data.json', 'w') as f:
                json.dump(data, f)

            em = discord.Embed(title="Ticket System",
                               description=f"You have successfully added `{role.name}` to the list of roles that can run admin-level commands!",
                               color=0x00a8ff)
            await ctx.send(embed=em)

        except discord.Forbidden:
            em = discord.Embed(title="Ticket System",
                               description="That isn't a valid role ID. Please try again with a valid role ID.")
            await ctx.send(embed=em)

    @commands.command()
    @has_permissions(administrator=True)
    async def deladminrole(self, ctx, role_id=None):
        try:
            role_id = int(role_id)
            role = ctx.guild.get_role(role_id)

            with open("./utils/json/ticket_data.json") as f:
                data = json.load(f)

            admin_roles = data["verified-roles"]

            if role_id in admin_roles:
                index = admin_roles.index(role_id)

                del admin_roles[index]

                data["verified-roles"] = admin_roles

                with open('./utils/json/ticket_data.json', 'w') as f:
                    json.dump(data, f)

                em = discord.Embed(title="Ticket System",
                                   description=f"You have successfully removed `{role.name}` from the list of roles that get pinged when new tickets are created.",
                                   color=0x00a8ff)

                await ctx.send(embed=em)

            else:
                em = discord.Embed(title="Ticket System",
                                   description="That role isn't getting pinged when new tickets are created!",
                                   color=0x00a8ff)
                await ctx.send(embed=em)

        except discord.Forbidden:
            em = discord.Embed(title="Ticket System",
                               description="That isn't a valid role ID. Please try again with a valid role ID.")
            await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(ticket(bot))
