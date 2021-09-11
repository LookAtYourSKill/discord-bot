import datetime
import json
import random

import discord
from discord.ext import commands


class onMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

###################################################AUTOMOD##############################################################
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        counter = 0
        with open("C:/Users/simon/PycharmProjects/Discord Bot/Discord Bot/utils/json/spam-detection.json", "r+") as file:
            for lines in file:
                if lines.strip("\n") == str(message.author.id):
                    counter += 1

            file.writelines(f"{str(message.author.id)}\n")
            if counter > 7:
                await message.guild.kick(message.author, reason="Spam Detection")
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

        with open("C:/Users/simon/PycharmProjects/Discord Bot/Discord Bot/utils/json/blacklist.json", 'r') as f:
            data = json.load(f)
        for bad_word in data["blacklist"]:
            #print(bad_word)
            if bad_word in message.content.lower():
                #print(message.content.lower())
                await message.delete()
                embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                      description='Deine Message `wurde gelöscht`, da du ein Wort `aus der Blacklist darin hattest!`\n**Bitte unterlasse dies!**')
                await message.channel.send(embed=embed, delete_after=5)

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
        # def remove_afk(self, afk):
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

        if message.content.startswith('help blacklist_add'):
            embed = discord.Embed(title='Help for blacklist_add',
                                  description='`Add a word to a blacklist...`')
            embed.add_field(name='__Usage:__',
                            value='**?blacklist_add** <`bad_word`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help blacklist_remove'):
            embed = discord.Embed(title='Help for blacklist_remove',
                                  description='`Remove a word to a blacklist...`')
            embed.add_field(name='__Usage:__',
                            value='**?blacklist_remove** <`bad_word`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help blacklist_show'):
            embed = discord.Embed(title='Help for blacklist_show',
                                  description='`Display all words on the blacklist...`')
            embed.add_field(name='__Usage:__',
                            value='**?blacklist_show**',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help blacklist_clear'):
            embed = discord.Embed(title='Help for blacklist_clear',
                                  description='`Clear the blacklist...`')
            embed.add_field(name='__Usage:__',
                            value='**?blacklist_clear**',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

##################################################INFOS#################################################################

        if message.content.startswith('help server'):
            embed = discord.Embed(title='Help for server',
                                  description='`Display Infos about the server...`')
            embed.add_field(name='__Usage:__',
                            value='**?server**',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help user'):
            embed = discord.Embed(title='Help for user',
                                  description='`Display Infos about a user...`')
            embed.add_field(name='__Usage:__',
                            value='**?user** <`member`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help bot'):
            embed = discord.Embed(title='Help for bot',
                                  description='`Display Infos about this bot...`')
            embed.add_field(name='__Usage:__',
                            value='**?bot**',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help avatar'):
            embed = discord.Embed(title='Help for avatar',
                                  description='`Display a users avatar...`')
            embed.add_field(name='__Usage:__',
                            value='**?avatar** `member`',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help members'):
            embed = discord.Embed(title='Help for members',
                                  description='`Shows you how many users are on the server...`')
            embed.add_field(name='__Usage:__',
                            value='**?bot**',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

##################################################UTILITIES#############################################################

        if message.content.startswith('help invite'):
            embed = discord.Embed(title='Help for invite',
                                  description='`Create an invite...`')
            embed.add_field(name='__Usage:__',
                            value='**?invite**',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help invites'):
            embed = discord.Embed(title='Help for invites',
                                  description='`Shows the invites of a member...`')
            embed.add_field(name='__Usage:__',
                            value='**?invites** <`member`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help botinvite'):
            embed = discord.Embed(title='Help for botinvite',
                                  description='`Give you 2 invites for the bot...`')
            embed.add_field(name='__Usage:__',
                            value='**?botinvite**',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help repeat'):
            embed = discord.Embed(title='Help for repeat',
                                  description='`Give your text back...`')
            embed.add_field(name='__Usage:__',
                            value='**?repeat** <`text`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help embed'):
            embed = discord.Embed(title='Help for embed',
                                  description='`Creates an Embed, with the text you wrote...`')
            embed.add_field(name='__Usage:__',
                            value='**?embed** <`text`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help senddm'):
            embed = discord.Embed(title='Help for senddm',
                                  description='`Send a user an dm with the text you want...`')
            embed.add_field(name='__Usage:__',
                            value='**?senddm** <`text`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help password'):
            embed = discord.Embed(title='Help for password',
                                  description='`Creates an random password with 20 random digits...`')
            embed.add_field(name='__Usage:__',
                            value='**?password**',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

##################################################MATH##################################################################

        if message.content.startswith('help addition'):
            embed = discord.Embed(title='Help for addition',
                                  description='`Add you 2 digits together...`')
            embed.add_field(name='__Usage:__',
                            value='**?addition** `<first>` `<second>`',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help subtraction'):
            embed = discord.Embed(title='Help for subtraction',
                                  description='`Subtract you 2 digits together...`')
            embed.add_field(name='__Usage:__',
                            value='**?subtraction** `<first>` `<second>`',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help multiplication'):
            embed = discord.Embed(title='Help for multiplication',
                                  description='`Multiply you 2 digits together...`')
            embed.add_field(name='__Usage:__',
                            value='**?multiplication** `<first>` `<second>`',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help dividation'):
            embed = discord.Embed(title='Help for dividation',
                                  description='`Divide you 2 digits together...`')
            embed.add_field(name='__Usage:__',
                            value='**?dividation** `<first>` `<second>`',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

##################################################ROLES#################################################################

        if message.content.startswith('help giverole'):
            embed = discord.Embed(title='Help for giverole',
                                  description='`Give a role to a user...`')
            embed.add_field(name='__Usage:__',
                            value='**?giverole** <`member`> <`role`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help removerole'):
            embed = discord.Embed(title='Help for removerole',
                                  description='`Remove a role from a user...`')
            embed.add_field(name='__Usage:__',
                            value='**?giverole** <`member`> <`role`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help addrole'):
            embed = discord.Embed(title='Help for addrole',
                                  description='`Create a new role...`')
            embed.add_field(name='__Usage:__',
                            value='**?addrole** <`rolename`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help deleterole'):
            embed = discord.Embed(title='Help for deleterole',
                                  description='`Delete an existing role...`')
            embed.add_field(name='__Usage:__',
                            value='**?deleterole** <`rolename`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

##################################################GIVEAWAY##############################################################

        if message.content.startswith('help create'):
            embed = discord.Embed(title='Help for create',
                                  description='`Create a giveaway...`')
            embed.add_field(name='__Usage:__',
                            value='**?create** <`time`> <`prize`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help gawrole'):
            embed = discord.Embed(title='Help for gawrole',
                                  description='`Create the required role for the giveaways...`')
            embed.add_field(name='__Usage:__',
                            value='**?gawrole**',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

##################################################MUSIC#################################################################

        if message.content.startswith('help play'):
            embed = discord.Embed(title='Help for play',
                                  description='`Add a song to play in a voice channel...`')
            embed.add_field(name='__Usage:__',
                            value='**?play** <`song_url`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help leave'):
            embed = discord.Embed(title='Help for leave',
                                  description='`Let the bot leave from the voice channel...`')
            embed.add_field(name='__Usage:__',
                            value='**?leave**',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help resume'):
            embed = discord.Embed(title='Help for resume',
                                  description='`Let the bot resuming playing the song...`')
            embed.add_field(name='__Usage:__',
                            value='**?resume**',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help pause'):
            embed = discord.Embed(title='Help for pause',
                                  description='`Let the bot pause playing the song...`')
            embed.add_field(name='__Usage:__',
                            value='**?pause**',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help nowplaying'):
            embed = discord.Embed(title='Help for nowplaying',
                                  description='`Display what song the bot play now...`')
            embed.add_field(name='__Usage:__',
                            value='**?leave**',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

##################################################FOR THE VIBE##########################################################

        if message.content.startswith('help raft'):
            embed = discord.Embed(title='Help for raft',
                                  description='`Playing the raft theme song...`')
            embed.add_field(name='__Usage:__',
                            value='**?raft**',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

##################################################FUN###################################################################

        if message.content.startswith('help 8ball'):
            embed = discord.Embed(title='Help for 8ball',
                                  description='`You can ask a question and the bot will answer it randomly...`')
            embed.add_field(name='__Usage:__',
                            value='**?8ball** <`question`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help roll'):
            embed = discord.Embed(title='Help for roll',
                                  description='`Let a dice roll...`')
            embed.add_field(name='__Usage:__',
                            value='**?roll**',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help rps'):
            embed = discord.Embed(title='Help for rps',
                                  description='`Play rock paper scissors against the bot...`')
            embed.add_field(name='__Usage:__',
                            value='**?rps** <`\'rock\', \'paper\' or \'scissors\'`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help slots'):
            embed = discord.Embed(title='Help for slots',
                                  description='`Playing on a automat like in a casino...`')
            embed.add_field(name='__Usage:__',
                            value='**?slots**',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

##################################################GIFS##################################################################

        if message.content.startswith('help hug'):
            embed = discord.Embed(title='Help for hug',
                                  description='`You can visually hug a person...`')
            embed.add_field(name='__Usage:__',
                            value='**?hug** <`member`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help laugh'):
            embed = discord.Embed(title='Help for laugh',
                                  description='`You can laugh...`')
            embed.add_field(name='__Usage:__',
                            value='**?laugh**',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help punch'):
            embed = discord.Embed(title='Help for punch',
                                  description='`You can visually punch a person...`')
            embed.add_field(name='__Usage:__',
                            value='**?punch** <`member`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help cry'):
            embed = discord.Embed(title='Help for cry',
                                  description='`You can cry...`')
            embed.add_field(name='__Usage:__',
                            value='**?cry**',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help kiss'):
            embed = discord.Embed(title='Help for kiss',
                                  description='`You can visually kiss a person...`')
            embed.add_field(name='__Usage:__',
                            value='**?kiss** <`member`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help cat'):
            embed = discord.Embed(title='Help for cat',
                                  description='`The bot gives out a cat gif...`')
            embed.add_field(name='__Usage:__',
                            value='**?slots**',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help rage'):
            embed = discord.Embed(title='Help for rage',
                                  description='`You can rage...`')
            embed.add_field(name='__Usage:__',
                            value='**?slots**',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help highfive'):
            embed = discord.Embed(title='Help for highfive',
                                  description='`You can highfive a person...`')
            embed.add_field(name='__Usage:__',
                            value='**?highfive** <`member`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

        if message.content.startswith('help handshake'):
            embed = discord.Embed(title='Help for handshake',
                                  description='`You can handshake a person...`')
            embed.add_field(name='__Usage:__',
                            value='**?handshake** <`member`>',
                            inline=False)
            embed.set_footer(text='<> verpflichtend | [] optional')
            await message.channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, old, new):
        channel = self.bot.get_channel(872945922743619657)
        embed = discord.Embed(title="Message Edited",
                              description=f"{old.author.mention} has edited a message in {old.channel.mention} [Jump to the Message]({new.jump_url})",
                              color=discord.Color.random(),
                              timestamp=datetime.datetime.utcnow())
        embed.add_field(name="Old Message",
                        value=f'{old.content}',
                        inline=False)
        embed.add_field(name="New Message",
                        value=f'{new.content}',
                        inline=False)
        #embed.add_field(name="Channel", value=f'{old.channel.mention}', inline=False)
        #embed.add_field(name="Author", value=f'{old.author.mention}', inline=False)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        channel = self.bot.get_channel(872945922743619657)
        embed = discord.Embed(title="Message Deleted",
                              description=f'A message from {message.author.mention} was deleted in {message.channel.mention} ',
                              color=discord.Color.random(),
                              timestamp=datetime.datetime.utcnow())
        embed.add_field(name="Message",
                        value=f'{message.content}',
                        inline=False)
        #embed.add_field(name="Author", value=f'{message.author.mention}', inline=False)
        #embed.add_field(name="Channel", value=f'{message.channel.mention}', inline=False)
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(onMessage(bot))
