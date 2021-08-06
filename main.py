import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import bot
import os

bot = commands.Bot(intense=discord.Intents.all(), command_prefix='?', help_command=commands.MinimalHelpCommand())
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'Botid: {bot.user.id} - Name: {bot.user.name}')
    print(f'Bot Logged in as "{bot.user.name}"')
    bot.loop.create_task(status_task())


async def status_task():
    while True:
        await bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.playing,
                name='Some Commands 🔥 | !help'),
            status=discord.Status.online)
        await asyncio.sleep(3600)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run('TOKEN HERE')
