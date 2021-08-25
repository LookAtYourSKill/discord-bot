import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import bot
from termcolor import colored
import os

bot = commands.Bot(intents=discord.Intents.all(), command_prefix='?')
bot.remove_command('help')


@bot.event
async def on_ready():
    print(colored(f'Botid: {bot.user.id} - Name: {bot.user.name}#{bot.user.discriminator}', 'green'))
    bot.loop.create_task(status_task())
    while True:
        await asyncio.sleep(10)
        with open("utils/json/spam-detection.json", "r+") as file:
            file.truncate(0)


async def status_task():
    while True:
        await bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name=f'?help | {len(bot.guilds)} servers'),
            status=discord.Status.idle)
        await asyncio.sleep(3600)


active_extensions = ['cogs.administration',
                     'cogs.automod',
                     'cogs.error_handler',
                     'cogs.fun',
                     'cogs.gifs',
                     'cogs.giveaway',
                     'cogs.help',
                     'cogs.info',
                     'cogs.math',
                     'cogs.moderation',
                     'cogs.music',
                     'cogs.raft',
                     'cogs.roles',
                     'cogs.utilities',
                     'events.logevents',
                     'events.onJoin',
                     'events.onMessage',
                     'events.onRemove']

if __name__ == '__main__':
    for extension in active_extensions:
        try:
            bot.load_extension(extension)
            print(f'Loaded ' + colored(f'{extension} ', 'green') + f'Successful')
        except:
            print(colored(f'Error, something went wrong!', 'red'))

    # for filename in os.listdir('./cogs'):
    #    if filename.endswith('.py'):
    #        bot.load_extension(f'cogs.{filename[:-3]}')

    # for filename in os.listdir('./events'):
    #    if filename.endswith('.py'):
    #        bot.load_extension(f'events.{filename[:-3]}')

bot.run('')
