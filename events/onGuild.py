import json
from discord.ext import commands


class on_guild(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open('utils/json/on_guild.json', 'r+') as f:
            data = json.load(f)

        new_server = {
            "SERVERNAME": f"{str(guild.name)}",
            "MESSAGE_LOG_CHANNEL": (),
            "MODERATION_LOG_CHANNEL": (),
            "WELCOME_CHANNEL": (),
            "LEAVE_CHANNEL": (),
            "VERIFY_CHANNEL": (),
            "BOT_ROLE": (),
            "VERIFIED_ROLE": ()
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
            "Ticket_System": "true",
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


@commands.Cog.listener()
async def on_guild_leave(self, guild):
    pass

def setup(bot):
    bot.add_cog(on_guild(bot))
