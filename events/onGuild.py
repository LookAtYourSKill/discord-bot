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
            "SERVERNAME": "BotTesting",
            "MESSAGE_LOG_CHANNEL": (),
            "MODERATION_LOG_CHANNEL": (),
            "WELCOME_CHANNEL": (),
            "LEAVE_CHANNEL": (),
            "VERIFY_CHANNEL": (),
            "BOT_ROLE": (),
            "VERIFIED_ROLE": (),
            "WARNS": {
                }
            }

        data[str(guild.id)] = new_server
        with open('utils/json/on_guild.json', 'w') as f:
            json.dump(data, f, indent=4)

    @commands.Cog.listener()
    async def on_guild_leave(self, guild):
        with open('utils/json/on_guild.json', 'r') as f:
            data = json.load(f)

        old_server = {
            "SERVERNAME": "BotTesting",
            "MESSAGE_LOG_CHANNEL": (),
            "MODERATION_LOG_CHANNEL": (),
            "WELCOME_CHANNEL": (),
            "LEAVE_CHANNEL": (),
            "VERIFY_CHANNEL": (),
            "BOT_ROLE": (),
            "VERIFIED_ROLE": (),
            "WARNS": {
                }
            }
        data[str(guild.id)].remove(old_server)
        with open('utils/json/on_guild.json', 'w') as f:
            json.dump(data, f, indent=4)


def setup(bot):
    bot.add_cog(on_guild(bot))
