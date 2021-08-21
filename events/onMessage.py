import json
import discord
from discord.ext import commands

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

##################################################BLACKLIST CHECK#######################################################

        #with open("./utils/json/blacklist.json", 'r') as file:
        #    json.load(file)
        #    blacklist = '.utils/json/blacklist.json'
        #if message.author.bot:
        #    return
        #for bad_word in blacklist:
        #    if bad_word in message.content.strip().lower():
        #        await message.delete()
        #        embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
        #                              description='Deine Message `wurde gelöscht`, da du ein Wort `aus der Blacklist darin hattest!`\n**Bitte unterlasse dies!**')
        #        await message.channel.send(embed=embed, delete_after=5)

##################################################ANTI BAD FILE#########################################################

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

##################################################LINK PROTECTION#######################################################
        invLink = ['https://', 'http://']

        if message.author.bot:
            return
        for synonym in invLink:
            if synonym in message.content.lower():
                await message.delete()
                embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                      description='Hier sind **keine Links erlaubt**!')
                await message.channel.send(embed=embed, delete_after=5)

##################################################ONPING################################################################

        if message.content.startswith('<@!790965419670241281>'):
            embed = discord.Embed(title="Ping",
                                  description=f"Mein Prefix: **?**\n"
                                              f"Mit **?help** kannst du `dir alle Commands anschauen!`",
                                  color=0xff00c8)
            await message.author.send(embed=embed)
            await message.delete()

##################################################AFKS##################################################################
        #def remove_afk(self, afk):
        #    if '[AFK]' in afk.split():
        #        return ' '.join(afk.split()[1:])
        #    else:
        #        return afk

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
        if message.content.startswith('help reload_cog'):
            embed = discord.Embed(title='Help for reload_cog',
                                  description='`Reload Extension you mention...`')
            embed.add_field(name='__Usage:__',
                            value='**?reload_cog** <`extension`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help reload_event'):
            embed = discord.Embed(title='Help for reload_event',
                                  description='`Reload the Event you mention...`')
            embed.add_field(name='__Usage:__',
                            value='**?reload_event** <`extension`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help unload_cog'):
            embed = discord.Embed(title='Help for unload_cog',
                                  description='`Unload the Extension you want to...`')
            embed.add_field(name='__Usage:__',
                            value='**?unload_cog** <`extension`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help unload_event'):
            embed = discord.Embed(title='Help for unload_event',
                                  description='`Unload the Event you want to...`')
            embed.add_field(name='__Usage:__',
                            value='**?unload_event** <`extension`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help load_cog'):
            embed = discord.Embed(title='Help for load_cog',
                                  description='`Load the Extension you want to...`')
            embed.add_field(name='__Usage:__',
                            value='**?load_cog** <`extension`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help load_event'):
            embed = discord.Embed(title='Help for load_event',
                                  description='`Load the Event you want to...`')
            embed.add_field(name='__Usage:__',
                            value='**?load_event** <`extension`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help lock'):
            embed = discord.Embed(title='Help for lock',
                                  description='`Lock the channel where you send the command...`')
            embed.add_field(name='__Usage:__',
                            value='**?lock**',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help unlock'):
            embed = discord.Embed(title='Help for unlock',
                                  description='`unlock the channel where you send the command...`')
            embed.add_field(name='__Usage:__',
                            value='**?unlock**',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help say'):
            embed = discord.Embed(title='Help for say',
                                  description='`Gives your message back, with an @everyone...`')
            embed.add_field(name='__Usage:__',
                            value='**?say** <`message`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

##################################################MODERATION PART#######################################################

        if message.content.startswith('help ban'):
            embed = discord.Embed(title='Help for ban',
                                  description='`Ban the member you mention or the id...`')
            embed.add_field(name='__Usage:__',
                            value='**?ban** <`id or mention`> [`reason`]',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help unban'):
            embed = discord.Embed(title='Help for unban',
                                  description='`Unban the member you mention (name#0001)...`')
            embed.add_field(name='__Usage:__',
                            value='**?unban** <`member`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help unbanid'):
            embed = discord.Embed(title='Help for unbanid',
                                  description='`Unban the member with the id (504717510084395008)...`')
            embed.add_field(name='__Usage:__',
                            value='**?unbanid** <`id`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help unbanall'):
            embed = discord.Embed(title='Help for unbanall',
                                  description='`Unban all the members banned on the server...`')
            embed.add_field(name='__Usage:__',
                            value='**?unbanall**',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help tempban'):
            embed = discord.Embed(title='Help for tempban',
                                  description='`Ban a user for a specific time...`')
            embed.add_field(name='__Usage:__',
                            value='**?tempban** <`member`> <`time`> [`reason`]\n'
                                  '\n'
                                  '**Zeiten:**\n'
                                  '`s` Sekunden\n'
                                  '`m` Minuten\n'
                                  '`h` Stunden\n'
                                  '`d` Tagen\n'
                                  '`w` Wochen\n'
                                  '\n',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help banned'):
            embed = discord.Embed(title='Help for bannedUserList',
                                  description='`Display all banned members...`\n'
                                              '`[WARNING SPAM]`')
            embed.add_field(name='__Usage:__',
                            value='**?banned**',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help mute'):
            embed = discord.Embed(title='Help for mute',
                                  description='`Mutes a member...`')
            embed.add_field(name='__Usage:__',
                            value='**?mute** <`member`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help unmute'):
            embed = discord.Embed(title='Help for unmute',
                                  description='`Unmutes a member...`')
            embed.add_field(name='__Usage:__',
                            value='**?unmute** <`member`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help muterole'):
            embed = discord.Embed(title='Help for muterole',
                                  description='`Creates mute role...`')
            embed.add_field(name='__Usage:__',
                            value='**?muterole**',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help tempmute'):
            embed = discord.Embed(title='Help for tempmute',
                                  description='`Mute a user for a specific time...`')
            embed.add_field(name='__Usage:__',
                            value='**?tempmute** <`member`> <`time`> [`reason`]\n'
                                  '\n'
                                  '**Zeiten:**\n'
                                  '`s` Sekunden\n'
                                  '`m` Minuten\n'
                                  '`h` Stunden\n'
                                  '`d` Tagen\n'
                                  '`w` Wochen\n'
                                  '\n',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help kick'):
            embed = discord.Embed(title='Help for kick',
                                  description='`Kick a member...`')
            embed.add_field(name='__Usage:__',
                            value='**?kick** <`member`> [`reason`]',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help vckick'):
            embed = discord.Embed(title='Help for Voicechannel Kick',
                                  description='`Disconnect a member from a Voicechannel...`')
            embed.add_field(name='__Usage:__',
                            value='**?vckick** <`member`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help slowmode'):
            embed = discord.Embed(title='Help for slowmode',
                                  description='`Create or change the slowmode of the channel...`')
            embed.add_field(name='__Usage:__',
                            value='**?slowmode** <`seconds`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help clear'):
            embed = discord.Embed(title='Help for clear',
                                  description='`Clear a channel with a specific amount of messages...`')
            embed.add_field(name='__Usage:__',
                            value='**?clear** <`amount`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help nuke'):
            embed = discord.Embed(title='Help for nuke',
                                  description='`Delete a channel and create the same channel...`')
            embed.add_field(name='__Usage:__',
                            value='**?nuke** <`channel`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

##################################################AUTOMOD PART##########################################################

def setup(bot):
    bot.add_cog(onMessage(bot))
