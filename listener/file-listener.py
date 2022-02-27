import disnake as discord
from disnake.ext import commands


class fileBlocker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        message_attachments = message.attachments
        if len(message_attachments) > 0:
            for attachment in message_attachments:
                if attachment.filename.endswith(".dll"):
                    await message.delete()
                    embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                          description='Hier sind keine Datein, mit dem **Dateinamen Ende \'dll\' erlaubt**')
                    await message.channel.send(embed=embed, delete_after=5)
                elif attachment.filename.endswith('.exe'):
                    await message.delete()
                    embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                          description='Hier sind keine Datein, mit dem **Dateinamen Ende \'exe\' erlaubt**')
                    await message.channel.send(embed=embed, delete_after=5)
                elif attachment.filename.endswith('.bat'):
                    await message.delete()
                    embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                          description='Hier sind keine Datein, mit dem **Dateinamen Ende \'bat\' erlaubt**')
                    await message.channel.send(embed=embed, delete_after=5)
                else:
                    break


def setup(bot):
    bot.add_cog(fileBlocker(bot))
