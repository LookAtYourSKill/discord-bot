import json
import discord
from discord.ext import commands


class on_guild(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open('utils/json/on_guild.json', 'r+') as f:
            data = json.load(f)

        new_server = {
            "server_name": f"{str(guild.name)}",
            "message_log_channel": (),
            "moderation_log_channel": (),
            "welcome_channel": (),
            "leave_channel": (),
            "verify_channel": (),
            "bot_role": (),
            "verified_role": ()
        }

        data[str(guild.id)] = new_server
        with open('utils/json/on_guild.json', 'w') as f:
            json.dump(data, f, indent=4)

        with open('utils/json/warns.json', 'r') as f:
            data = json.load(f)

        new_warn = {
            "warns": {}
        }

        data[str(guild.id)] = new_warn
        with open('utils/json/warns.json', 'w') as f:
            json.dump(data, f, indent=4)

        with open('utils/json/active_check.json', 'r+') as f:
            data = json.load(f)

        new_checks = {
            "Administration": "true",
            "Automod": "true",
            "Channel": "true",
            "Fun": "true",
            "Help": "true",
            "Info": "true",
            "Math": "true",
            "Moderation": "true",
            "Music": "true",
            "Poll": "true",
            "Roles": "true",
            "Rules": "true",
            "Setup": "true",
            "Ticket": "true",
            "Timers": "true",
            "Translator": "true",
            "Utilities": "true",
            "Verify": "true"
        }

        data[str(guild.id)] = new_checks
        with open('utils/json/active_check.json', 'w') as f:
            json.dump(data, f, indent=4)

        with open('utils/json/temp_times.json', 'r') as f:
            data = json.load(f)

        new_tempmute_times = {
            "tempmutes": {

            },
            "tempbans": {

            }
        }

        data[str(guild.id)] = new_tempmute_times
        with open('utils/json/temp_times.json', 'w') as f:
            json.dump(data, f, indent=4)

        with open('utils/json/blacklist.json', 'r') as f:
            data = json.load(f)

        new_blacklist = {
            "blacklist": [

            ],
            "channel_blacklist": [

            ]
        }

        data[str(guild.id)] = new_blacklist
        with open('utils/json/blacklist.json', 'w') as f:
            json.dump(data, f, indent=4)

        with open('utils/json/utility_times.json', 'r') as f:
            data = json.load(f)

        new_utility_timer = {
            "giveaway-counter": 0,
            "giveaways": {
                "giveaway_info": {}
            },
            "reminder-counter": 0,
            "reminders": {
                "reminder_info": {}
            }
        }

        data[str(guild.id)] = new_utility_timer
        with open('utils/json/utility_times.json', 'w') as f:
            json.dump(data, f, indent=4)

        embed = discord.Embed(description='Hallo :wave:! Freut mich das du mich auf dein Server eingeladen hast!\n'
                                          'Hier sind ein paar nützliche Informationen, die das Discord Leben entspannter machen werden!\n'
                                          'Für den Anfang solltest du die folgenden Commands, für den reibungslosen Verlauf des Bots ausführen!')
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
        await guild.owner.send(embed=embed)


@commands.Cog.listener()
async def on_guild_leave(self, guild):
    pass

def setup(bot):
    bot.add_cog(on_guild(bot))
