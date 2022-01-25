import json
import discord
from discord.ext import commands


class server_setup(commands.Cog):
    """
    `A Server setup commands, to make the bot ready for your server!`
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setup(self, ctx):
        embed = discord.Embed(description=f'Hinweis für die Setup Commands!', color=discord.Color.blurple())
        embed.add_field(name=f'setup_welcome_channel <channel_id>',
                        value=f'Damit kannst du ein Channel einstellen, in den alle neu joinenden User reingeschrieben werden!',
                        inline=False)
        embed.add_field(name=f'setup_leave_channel <channel_id>',
                        value=f'Damit kannst du ein Channel einstellen, in den alle verlassenden User reingeschrieben werden!',
                        inline=False)
        embed.add_field(name=f'setup_verify_channel <channel_id>',
                        value=f'Damit kannst du ein Channel einstellen, in den alle neu joinenden User den `?verify` Command reinschreiben können!',
                        inline=False)
        embed.add_field(name=f'setup_message_log_channel <channel_id>',
                        value=f'Damit kannst du ein Channel einstellen, in den alle editierten und gelöschten Nachrichten reingeschrieben werden!',
                        inline=False)
        embed.add_field(name=f'setup_moderation_log_channel <channel_id>',
                        value=f'Damit kannst du ein Channel einstellen, in den alle Moderatoren Aktionen reingeschrieben werden!',
                        inline=False)
        embed.add_field(name=f'setup_bot_role <role_id>',
                        value=f'Damit kannst du eine Rolle einstellen, die jeder neu joinende Bot erhält!!',
                        inline=False)
        embed.add_field(name=f'setup_verified_role <role_id>',
                        value=f'Damit kannst du eine Rolle einstellen, die jeder User nach dem `?verify` Command erhält!',
                        inline=False)
        embed.set_footer(text='[] optional | <> required')
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setup_welcome_channel(self, ctx, channel_id):
        """
        The setup commands
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Setup"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Setup) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            with open('utils/json/on_guild.json', 'r') as f:
                guild_data = json.load(f)

            if not guild_data[str(ctx.guild.id)]["welcome_channel"]:
                guild_data[str(ctx.guild.id)]["welcome_channel"] = int(channel_id)
                with open('utils/json/on_guild.json', 'w') as f:
                    json.dump(guild_data, f, indent=4)
                embed = discord.Embed(description=f'Der `Welcome Channel` wurde auf <#{channel_id}> gesetzt!',
                                      color=discord.Color.green())
                await ctx.send(embed=embed)

            elif guild_data[str(ctx.guild.id)]["welcome_channel"]:
                member = ctx.author
                embed = discord.Embed(
                    description=f'Der `Welcome Channel` ist bereits konfiguriert! Momentan ist dieser <#{guild_data[str(ctx.guild.id)]["welcome_channel"]}>')
                embed.add_field(name='Möchtest du ihn ändern?',
                                value='Falls **Ja** dann gebe **Ja** ein!\n'
                                      'Falls **Nein** dann gebe **Nein** ein!')
                embed.set_footer(text='Um den Command zu beenden schreibe einfach exit!')
                await ctx.send(embed=embed)
                while True:
                    message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                    if 'Ja' in message.content or 'ja' in message.content:
                        guild_data[str(ctx.guild.id)]["welcome_channel"] = int(channel_id)
                        with open('utils/json/on_guild.json', 'w') as f:
                            json.dump(guild_data, f, indent=4)
                        embed = discord.Embed(
                            description=f'Du hast **Ja** gewählt! Der `Welcome Channel` wurde nun **zu** <#{guild_data[str(ctx.guild.id)]["welcome_channel"]}> **geändert**!')
                        await ctx.send(embed=embed)
                    elif 'Nein' in message.content or 'nein' in message.content:
                        embed = discord.Embed(
                            description=f'Du hast **Nein** gewählt! Der `Welcome Channel` **wurde nicht geändert** und ist immer noch bei <#{guild_data[str(ctx.guild.id)]["welcome_channel"]}>!')
                        await ctx.send(embed=embed)
                    else:
                        return

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setup_leave_channel(self, ctx, channel_id):
        """
        The setup commands
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Setup"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Setup) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            with open('utils/json/on_guild.json', 'r') as f:
                guild_data = json.load(f)

            if not guild_data[str(ctx.guild.id)]["leave_channel"]:
                guild_data[str(ctx.guild.id)]["leave_channel"] = int(channel_id)
                with open('utils/json/on_guild.json', 'w') as f:
                    json.dump(guild_data, f, indent=4)
                embed = discord.Embed(description=f'Der `Leave Channel` wurde auf <#{channel_id}> gesetzt!',
                                      color=discord.Color.green())
                await ctx.send(embed=embed)

            elif guild_data[str(ctx.guild.id)]["leave_channel"]:
                member = ctx.author
                embed = discord.Embed(
                    description=f'Der `Leave Channel` ist bereits konfiguriert! Momentan ist dieser <#{guild_data[str(ctx.guild.id)]["leave_channel"]}>')
                embed.add_field(name='Möchtest du ihn ändern?',
                                value='Falls **Ja** dann gebe **Ja** ein!\n'
                                      'Falls **Nein** dann gebe **Nein** ein!')
                embed.set_footer(text='Um den Command zu beenden schreibe einfach exit!')
                await ctx.send(embed=embed)
                while True:
                    message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                    if 'Ja' in message.content or 'ja' in message.content:
                        guild_data[str(ctx.guild.id)]["leave_channel"] = int(channel_id)
                        with open('utils/json/on_guild.json', 'w') as f:
                            json.dump(guild_data, f, indent=4)
                        embed = discord.Embed(
                            description=f'Du hast **Ja** gewählt! Der `Leave Channel` wurde nun **zu** <#{guild_data[str(ctx.guild.id)]["leave_channel"]}> **geändert**!')
                        await ctx.send(embed=embed)
                    elif 'Nein' in message.content or 'nein' in message.content:
                        embed = discord.Embed(
                            description=f'Du hast **Nein** gewählt! Der `Leave Channel` **wurde nicht geändert** und ist immer noch bei <#{guild_data[str(ctx.guild.id)]["leave_channel"]}>!')
                        await ctx.send(embed=embed)
                    else:
                        return

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setup_verify_channel(self, ctx, channel_id):
        """
        The setup commands
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Setup"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Setup) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            with open('utils/json/on_guild.json', 'r') as f:
                guild_data = json.load(f)

            if not guild_data[str(ctx.guild.id)]["verify_channel"]:
                guild_data[str(ctx.guild.id)]["verify_channel"] = int(channel_id)
                with open('utils/json/on_guild.json', 'w') as f:
                    json.dump(guild_data, f, indent=4)
                embed = discord.Embed(description=f'Der `Verify Channel` wurde auf <#{channel_id}> **gesetzt**!',
                                      color=discord.Color.green())
                await ctx.send(embed=embed)

            elif guild_data[str(ctx.guild.id)]["verify_channel"]:
                member = ctx.author
                embed = discord.Embed(
                    description=f'Der `Verify Channel` ist bereits konfiguriert! Momentan ist dieser <#{guild_data[str(ctx.guild.id)]["verify_channel"]}>')
                embed.add_field(name='Möchtest du ihn ändern?',
                                value='Falls **Ja** dann gebe **Ja** ein!\n'
                                      'Falls **Nein** dann gebe **Nein** ein!')
                embed.set_footer(text='Um den Command zu beenden schreibe einfach exit!')
                await ctx.send(embed=embed)
                while True:
                    message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                    if 'Ja' in message.content or 'ja' in message.content:
                        guild_data[str(ctx.guild.id)]["verify_channel"] = int(channel_id)
                        with open('utils/json/on_guild.json', 'w') as f:
                            json.dump(guild_data, f, indent=4)
                        embed = discord.Embed(
                            description=f'Du hast **Ja** gewählt! Der `Verify Channel` wurde nun **zu** <#{channel_id}> **geändert**!')
                        await ctx.send(embed=embed)
                    elif 'Nein' in message.content or 'nein' in message.content:
                        embed = discord.Embed(
                            description=f'Du hast **Nein** gewählt! Der `Verify Channel` **wurde nicht geändert** und ist immer noch bei <#{guild_data[str(ctx.guild.id)]["verify_channel"]}>!')
                        await ctx.send(embed=embed)
                    else:
                        return

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setup_moderation_log_channel(self, ctx, channel_id):
        """
        The setup commands
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Setup"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Setup) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            with open('utils/json/on_guild.json', 'r') as f:
                guild_data = json.load(f)

            if not guild_data[str(ctx.guild.id)]["moderation_log_channel"]:
                guild_data[str(ctx.guild.id)]["moderation_log_channel"] = int(channel_id)
                with open('utils/json/on_guild.json', 'w') as f:
                    json.dump(guild_data, f, indent=4)
                embed = discord.Embed(description=f'Der `Moderation Log Channel` wurde auf <#{channel_id}> gesetzt!',
                                      color=discord.Color.green())
                await ctx.send(embed=embed)

            elif guild_data[str(ctx.guild.id)]["moderation_log_channel"]:
                member = ctx.author
                embed = discord.Embed(
                    description=f'Der `Moderation Log Channel` ist bereits konfiguriert! Momentan ist dieser <#{guild_data[str(ctx.guild.id)]["moderation_log_channel"]}>')
                embed.add_field(name='Möchtest du ihn ändern?',
                                value='Falls **Ja** dann gebe **Ja** ein!\n'
                                      'Falls **Nein** dann gebe **Nein** ein!')
                embed.set_footer(text='Um den Command zu beenden schreibe einfach exit!')
                await ctx.send(embed=embed)
                while True:
                    message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                    if 'Ja' in message.content or 'ja' in message.content:
                        guild_data[str(ctx.guild.id)]["moderation_log_channel"] = int(channel_id)
                        with open('utils/json/on_guild.json', 'w') as f:
                            json.dump(guild_data, f, indent=4)
                        embed = discord.Embed(
                            description=f'Du hast **Ja** gewählt! Der `Moderation Log Channel` wurde nun **zu** <#{channel_id}> **geändert**!')
                        await ctx.send(embed=embed)
                    elif 'Nein' in message.content or 'nein' in message.content:
                        embed = discord.Embed(
                            description=f'Du hast **Nein** gewählt! Der `Moderation Log Channel` **wurde nicht geändert** und ist immer noch bei <#{guild_data[str(ctx.guild.id)]["moderation_log_channel"]}>!')
                        await ctx.send(embed=embed)
                    else:
                        return

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setup_message_log_channel(self, ctx, channel_id):
        """
        The setup commands
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Setup"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Setup) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            with open('utils/json/on_guild.json', 'r') as f:
                guild_data = json.load(f)

            if not guild_data[str(ctx.guild.id)]["message_log_channel"]:
                guild_data[str(ctx.guild.id)]["message_log_channel"] = int(channel_id)
                with open('utils/json/on_guild.json', 'w') as f:
                    json.dump(guild_data, f, indent=4)
                embed = discord.Embed(description=f'Der `Message Log Channel` wurde auf <#{channel_id}> gesetzt!',
                                      color=discord.Color.green())
                await ctx.send(embed=embed)

            elif guild_data[str(ctx.guild.id)]["message_log_channel"]:
                member = ctx.author
                embed = discord.Embed(
                    description=f'Der `Message Log Channel` ist bereits konfiguriert! Momentan ist dieser <#{guild_data[str(ctx.guild.id)]["message_log_channel"]}>')
                embed.add_field(name='Möchtest du ihn ändern?',
                                value='Falls **Ja** dann gebe **Ja** ein!\n'
                                      'Falls **Nein** dann gebe **Nein** ein!')
                embed.set_footer(text='Um den Command zu beenden schreibe einfach exit!')
                await ctx.send(embed=embed)
                while True:
                    message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                    if 'Ja' in message.content or 'ja' in message.content:
                        guild_data[str(ctx.guild.id)]["message_log_channel"] = int(channel_id)
                        with open('utils/json/on_guild.json', 'w') as f:
                            json.dump(guild_data, f, indent=4)
                        embed = discord.Embed(
                            description=f'Du hast **Ja** gewählt! Der `Message Log Channel` wurde nun **zu** <#{channel_id}> **geändert**!')
                        await ctx.send(embed=embed)
                    elif 'Nein' in message.content or 'nein' in message.content:
                        embed = discord.Embed(
                            description=f'Du hast **Nein** gewählt! Der `Message Log Channel` **wurde nicht geändert** und ist immer noch bei <#{guild_data[str(ctx.guild.id)]["message_log_channel"]}>!')
                        await ctx.send(embed=embed)
                    else:
                        return

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setup_bot_role(self, ctx, role_id):
        """
        The setup commands
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Setup"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Setup) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            with open('utils/json/on_guild.json', 'r') as f:
                guild_data = json.load(f)

            if not guild_data[str(ctx.guild.id)]["bot_role"]:
                guild_data[str(ctx.guild.id)]["bot_role"] = int(role_id)
                with open('utils/json/on_guild.json', 'w') as f:
                    json.dump(guild_data, f, indent=4)
                embed = discord.Embed(description=f'Die `Bot Rolle` wurde auf <@&{role_id}> gesetzt!',
                                      color=discord.Color.green())
                await ctx.send(embed=embed)

            elif guild_data[str(ctx.guild.id)]["bot_role"]:
                member = ctx.author
                embed = discord.Embed(
                    description=f'Die `Bot Rolle` ist bereits konfiguriert! Momentan ist dieser <@&{guild_data[str(ctx.guild.id)]["bot_role"]}>')
                embed.add_field(name='Möchtest du ihn ändern?',
                                value='Falls **Ja** dann gebe **Ja** ein!\n'
                                      'Falls **Nein** dann gebe **Nein** ein!')
                embed.set_footer(text='Um den Command zu beenden schreibe einfach exit!')
                await ctx.send(embed=embed)
                while True:
                    message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                    if 'Ja' in message.content or 'ja' in message.content:
                        guild_data[str(ctx.guild.id)]["bot_role"] = int(role_id)
                        with open('utils/json/on_guild.json', 'w') as f:
                            json.dump(guild_data, f, indent=4)
                        embed = discord.Embed(
                            description=f'Du hast **Ja** gewählt! Die `Bot Rolle` wurde nun **zu** <@&{role_id}> **geändert**!')
                        await ctx.send(embed=embed)
                    elif 'Nein' in message.content or 'nein' in message.content:
                        embed = discord.Embed(
                            description=f'Du hast **Nein** gewählt! Die `Bot Rolle` **wurde nicht geändert** und ist immer noch bei <@&{guild_data[str(ctx.guild.id)]["bot_role"]}>!')
                        await ctx.send(embed=embed)
                    else:
                        return

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setup_verified_role(self, ctx, role_id):
        """
        The setup commands
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Setup"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Setup) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            with open('utils/json/on_guild.json', 'r') as f:
                guild_data = json.load(f)

            if not guild_data[str(ctx.guild.id)]["verified_role"]:
                guild_data[str(ctx.guild.id)]["verified_role"] = int(role_id)
                with open('utils/json/on_guild.json', 'w') as f:
                    json.dump(guild_data, f, indent=4)
                embed = discord.Embed(description=f'Die `Verified Rolle` wurde auf <@&{role_id}> gesetzt!',
                                      color=discord.Color.green())
                await ctx.send(embed=embed)

            elif guild_data[str(ctx.guild.id)]["verified_role"]:
                member = ctx.author
                embed = discord.Embed(
                    description=f'Die `Verified Rolle` ist bereits konfiguriert! Momentan ist dieser <@&{guild_data[str(ctx.guild.id)]["verified_role"]}>')
                embed.add_field(name='Möchtest du ihn ändern?',
                                value='Falls **Ja** dann gebe **Ja** ein!\n'
                                      'Falls **Nein** dann gebe **Nein** ein!')
                embed.set_footer(text='Um den Command zu beenden schreibe einfach exit!')
                await ctx.send(embed=embed)
                while True:
                    message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                    if 'Ja' in message.content or 'ja' in message.content:
                        guild_data[str(ctx.guild.id)]["verified_role"] = int(role_id)
                        with open('utils/json/on_guild.json', 'w') as f:
                            json.dump(guild_data, f, indent=4)
                        embed = discord.Embed(
                            description=f'Du hast **Ja** gewählt! Die `Verified Rolle` wurde nun **zu** <@&{role_id}> **geändert**!')
                        await ctx.send(embed=embed)
                    elif 'Nein' in message.content or 'nein' in message.content:
                        embed = discord.Embed(
                            description=f'Du hast **Nein** gewählt! Die `Verified Rolle` **wurde nicht geändert** und ist immer noch bei <@&{guild_data[str(ctx.guild.id)]["verified_role"]}>!')
                        await ctx.send(embed=embed)
                    else:
                        return


def setup(bot):
    bot.add_cog(server_setup(bot))
