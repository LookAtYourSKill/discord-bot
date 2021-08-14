import asyncio
import discord
from discord.ext import commands


class onMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    with open('C:/Users/simon/PycharmProjects/pythonProject/Discord Bot/utils/json_files/spam-detection.json',
              'r+') as file:
        file.truncate(0)

    with open("C:/Users/simon/PycharmProjects/pythonProject/Discord Bot/utils/json_files/blacklist.json", 'r') as file:
        bad_words = [bad_word.strip().lower() for bad_word in file.readlines()]

    @commands.Cog.listener()
    async def on_message(self, message):
        counter = 0
        with open("C:/Users/simon/PycharmProjects/pythonProject/Discord Bot/utils/json_files/spam-detection.json",
                  "r+") as file:
            for lines in file:
                if lines.strip("\n") == str(message.author.id):
                    counter += 1

            file.writelines(f"{str(message.author.id)}\n")
            if counter > 10:
                await message.guild.kick(message.author, reason="spam")
                await asyncio.sleep(10)
                file.truncate(0)
                channel = message.guild.get_channel(872945922743619657)
                embed = discord.Embed(title='',
                                      description='',
                                      color=discord.Color.random())
                embed.add_field(name='**Spam Detection Kick**',
                                value=f'Kicked User : `{message.author.name}#{message.author.discriminator}`\n'
                                      f'User ID : `{message.author.id}`\n'
                                      f'Gekickt von : `Ich seh dich#0264`')
                await channel.send(embed=embed)

        with open("C:/Users/simon/PycharmProjects/pythonProject/Discord Bot/utils/json_files/blacklist.json",
                  'r') as file:
            bad_words = [bad_word.strip().lower() for bad_word in file.readlines()]
        message_content = message.content.strip().lower()
        for bad_word in bad_words:
            if bad_word in message_content:
                await self.bot.send_message(message.channel,
                                            f"{message.author.mention}, your message has been censored.")
                await self.bot.delete_message(message)

        message_attachments = message.attachments
        if len(message_attachments) > 0:
            for attachment in message_attachments:
                if attachment.filename.endswith(".dll"):
                    await message.delete()
                    await message.channel.send("No DLL's allowed!")
                elif attachment.filename.endswith('.exe'):
                    await message.delete()
                    await message.channel.send("No EXE's allowed!")
                else:
                    break

        if message.content.startswith('<@790965419670241281>'):
            embed = discord.Embed(title="Prefix", color=0xff00c8)
            embed.add_field(name="Wowowow a Ping",
                            value=f"Mein Prefix: **?**\n"
                                  f"Mit ?help kannst du dir alle command anschauen!",
                            inline=False)
            await message.author.send(embed=embed)


def setup(bot):
    bot.add_cog(onMessage(bot))
