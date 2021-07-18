import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import bot
import os


class CustomHelpCommand(commands.HelpCommand):
    def __init__(self):
        super().__init__()

    async def send_bot_help(self, mapping):
        for cog in mapping:
            await self.get_destination().send(f'{cog.qualified_name}: {[command.name for command in mapping[cog]]}')

    async def send_cog_help(self, cog):
        await self.get_destination().send(f'{cog.qualified_name}: {[command.name for command in cog.get_commands()]}')

    async def send_group_help(self, group):
        await self.get_destination().send(
            f'{group.name}: {[command.name for index, command in enumerate(group.command())]}')

    async def send_command_help(self, command):
        await self.get_destination().send(command.name)


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


@commands.command(name='load')
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')


@commands.command(name='unload')
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')


@commands.command(name='reload')
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run('NzkwOTY1NDE5NjcwMjQxMjgx.X-IR8w.YqwSsjrovQzflAw-rKUpEPKv5RU')
