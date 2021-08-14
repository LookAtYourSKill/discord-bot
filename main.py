import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import bot
import os

bot = commands.Bot(intense=discord.Intents.all(), command_prefix='?')
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'Botid: {bot.user.id} - Name: {bot.user.name}')
    print(f'Bot Logged in as "{bot.user.name}"')
    bot.loop.create_task(status_task())
    while True:
        await asyncio.sleep(10)
        with open("./utils/json_files/spam-detection.json", "r+") as file:
            file.truncate(0)


async def status_task():
    while True:
        await bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.playing,
                name='Some Commands 🔥 | !help'),
            status=discord.Status.online)
        await asyncio.sleep(3600)

if __name__ == '__main__':
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')

    for filename in os.listdir('./events'):
        if filename.endswith('.py'):
            bot.load_extension(f'events.{filename[:-3]}')

bot.run('TOKEN')
