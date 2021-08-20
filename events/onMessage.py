import json
import discord
from discord.ext import commands


def remove_afk(self, afk):
    if '[AFK]' in afk.split():
        return ' '.join(afk.split()[1:])
    else:
        return afk


class onMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

###################################################AUTOMOD##############################################################
    @commands.Cog.listener()
    async def on_message(self, message):
        counter = 0
        with open("C:/Users/simon/PycharmProjects/pythonProject/Discord Bot/utils/json/spam-detection.json",
                  "r+") as file:
            for lines in file:
                if lines.strip("\n") == str(message.author.id):
                    counter += 1

            file.writelines(f"{str(message.author.id)}\n")
            if counter > 10:
                await message.guild.kick(message.author, reason="spam")
                channel = message.guild.get_channel(872945922743619657)
                embed = discord.Embed(title='',
                                      description='',
                                      color=discord.Color.random())
                embed.add_field(name='**Spam Detection Kick**',
                                value=f'Kicked User : `{message.author.name}#{message.author.discriminator}`\n'
                                      f'User ID : `{message.author.id}`\n'
                                      f'Gekickt von : `Ich seh dich#0264`')
                await channel.send(embed=embed)

        # with open("./utils/json/blacklist.json", 'r') as file:
        #    json.load(file)
        #    blacklist = '.utils/json/blacklist.json'
        # message_content = message.content.strip().lower()
        # for bad_word in blacklist:
        #    if bad_word in message_content:
        #        await message.send(f"{message.author.mention}, your message has been deleted.")
        #        await message.delete()

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
##################################################ONPING################################################################
        if message.content.startswith('<@!790965419670241281>'):
            embed = discord.Embed(title="Ping",
                                  description=f"Mein Prefix: **?**\n"
                                              f"Mit **?help** kannst du `dir alle Commands anschauen!`",
                                  color=0xff00c8)
            await message.author.send(embed=embed)
            await message.delete()
##################################################AFKS##################################################################
        # if message.author.id in data.keys():
        #    data.pop(message.author.id)
        #    try:
        #        await message.author.edit(nick=remove_afk(message.author.display_name))
        #    except:
        #        pass
        #    await message.channel.send(f'Welcome back {message.author.name}, I removed you AFK')

        # for id, reason in data.items():
        #    member = message.guild.members, id = id
        #    if (message.reference and member == (await message.channel.fetch_message(
        #            message.reference.message_id)).author) or member.id in message.raw_mentions:
        #        await message.reply(f"{member.name} is AFK: {reason}")

##################################################ADMINISTRATION PART###################################################
        if message.content.startswith('help reload'):
            embed = discord.Embed(title='Help for Reload',
                                  description='Reload every Extension...')
            embed.add_field(name='Usage:',
                            value='?reload',
                            inline=False)
            await message.channel.send(embed=embed)

        if message.content.startswith('help unload'):
            embed = discord.Embed(title='Help for Unload',
                                  description='Unload the extension you want to...')
            embed.add_field(name='Usage:',
                            value='?unload <`extension`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help load'):
            embed = discord.Embed(title='Help for load',
                                  description='Load the extension you want to...')
            embed.add_field(name='Usage:',
                            value='?load <`extension`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help lock'):
            embed = discord.Embed(title='Help for lock',
                                  description='Lock the channel where you send the command...')
            embed.add_field(name='Usage:',
                            value='?lock',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help unlock'):
            embed = discord.Embed(title='Help for unlock',
                                  description='unlock the channel where you send the command...')
            embed.add_field(name='Usage:',
                            value='?unlock',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help say'):
            embed = discord.Embed(title='Help for say',
                                  description='Gives your message back, with an @everyone...')
            embed.add_field(name='Usage:',
                            value='?say <`message`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

##################################################MODERATION PART#######################################################

        if message.content.startswith('help ban'):
            embed = discord.Embed(title='Help for ban',
                                  description='Ban the member you mention or the id...')
            embed.add_field(name='Usage:',
                            value='?ban <`id or mention`> [`reason`]',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help unban'):
            embed = discord.Embed(title='Help for unban',
                                  description='Unban the member you mention (name#0001)...')
            embed.add_field(name='Usage:',
                            value='?unban <`member`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help unbanid'):
            embed = discord.Embed(title='Help for unbanid',
                                  description='Unban the member with the id (504717510084395008)...')
            embed.add_field(name='Usage:',
                            value='?unbanid <`id`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help unbanall'):
            embed = discord.Embed(title='Help for unbanall',
                                  description='Unban all the members banned on the server...')
            embed.add_field(name='Usage:',
                            value='?unbanall',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help tempban'):
            embed = discord.Embed(title='Help for tempban',
                                  description='Ban a user for a specific time...')
            embed.add_field(name='Usage:',
                            value='?tempban <`member`> <`time`> [`reason`]\n'
                                  '\n'
                                  '**Zeiten:**\n'
                                  '`s` Sekunden\n'
                                  '`min` Minuten\n'
                                  '`h` Stunden\n'
                                  '`d` Tage\n'
                                  '`w` Wochen\n'
                                  '\n',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help banned'):
            embed = discord.Embed(title='Help for bannedUserList',
                                  description='Display all banned members...\n'
                                              '[WARNING SPAM]')
            embed.add_field(name='Usage:',
                            value='?banned',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help mute'):
            embed = discord.Embed(title='Help for mute',
                                  description='Mutes the member...')
            embed.add_field(name='Usage:',
                            value='?mute <`member`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help unmute'):
            embed = discord.Embed(title='Help for unmute',
                                  description='Unmutes the member...')
            embed.add_field(name='Usage:',
                            value='?unmute <`member`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help muterole'):
            embed = discord.Embed(title='Help for muterole',
                                  description='Creates mute role...')
            embed.add_field(name='Usage:',
                            value='?muterole',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help tempmute'):
            embed = discord.Embed(title='Help for tempmute',
                                  description='Mute a user for a specific time...')
            embed.add_field(name='Usage:',
                            value='?tempban <`member`> <`time`> [`reason`]\n'
                                  '\n'
                                  '**Zeiten:**\n'
                                  '`s` Sekunden\n'
                                  '`min` Minuten\n'
                                  '`h` Stunden\n'
                                  '`d` Tage\n'
                                  '`w` Wochen\n'
                                  '\n',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help kick'):
            embed = discord.Embed(title='Help for kick',
                                  description='kick a member...')
            embed.add_field(name='Usage:',
                            value='?kick <`member`> [`reason`]',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help vckick'):
            embed = discord.Embed(title='Help for Voicechannel Kick',
                                  description='Disconnect a member from a Voicechannel...')
            embed.add_field(name='Usage:',
                            value='?vckick <`member`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help slowmode'):
            embed = discord.Embed(title='Help for slowmode',
                                  description='Create or change the slowmode of the channel...')
            embed.add_field(name='Usage:',
                            value='?slowmode <`seconds`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help clear'):
            embed = discord.Embed(title='Help for clear',
                                  description='Clear a channel with a specific amount of messages...')
            embed.add_field(name='Usage:',
                            value='?clear <`amount`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

##################################################AUTOMOD PART##########################################################

def setup(bot):
    bot.add_cog(onMessage(bot))
