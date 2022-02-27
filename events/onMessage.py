import datetime
import json
import disnake as discord
from disnake.ext import commands


class onMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_edit(self, old, new):
        with open('utils/json/on_guild.json', 'r') as f:
            guild_data = json.load(f)

        if old.author.bot:
            return

        elif not guild_data[str(old.author.guild.id)]["message_log_channel"]:
            return

        else:
            channel = self.bot.get_channel(guild_data[str(old.guild.id)]['message_log_channel'])
            embed = discord.Embed(
                description=f"{old.author.mention} has edited a message in {old.channel.mention} \n[Jump to the Message]({new.jump_url})",
                color=discord.Color.red(),
                timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Old Message",
                            value=f'{old.content}',
                            inline=False)
            embed.add_field(name="New Message",
                            value=f'{new.content}',
                            inline=False)
            #embed.set_author(name='Message Edited', icon_url=old.author.avatar_url)
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        with open('utils/json/on_guild.json', 'r') as f:
            guild_data = json.load(f)

        if message.author.bot:
            return

        elif not guild_data[str(message.author.guild.id)]["message_log_channel"]:
            return

        elif message.attachments:
            for attachment in message.attachments:
                channel = self.bot.get_channel(guild_data[str(message.author.guild.id)]['message_log_channel'])
                if message.content == '':
                    message.content = 'Keine Nachricht angegeben.'

                member = message.author
                embed = discord.Embed(
                    description=f'{member.mention} hat in {message.channel.mention} dieses Bild gesendet mit der Nachricht `{message.content}` gelöscht',
                    color=discord.Color.red())
                embed.set_image(url=attachment.url)
                await channel.send(embed=embed)

        else:
            channel = self.bot.get_channel(guild_data[str(message.author.guild.id)]['message_log_channel'])

            async for message1 in message.guild.audit_logs(action=discord.AuditLogAction.message_delete, limit=1):
                user = message1.user
                embed = discord.Embed(
                    description=f'A message from {message.author.mention} was deleted in {message.channel.mention} from {user.mention}',
                    color=discord.Color.red(),
                    timestamp=datetime.datetime.utcnow())
                embed.add_field(name="Message",
                                value=f'{message.content}',
                                inline=False)
                #embed.set_author(name='Message Deleted', icon_url=message.author.avatar_url)
                await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(onMessage(bot))
