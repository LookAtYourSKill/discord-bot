import asyncio
import os
import discord
from discord.ext import commands


class toggle(commands.Cog):
    """
    `To disable and activate plugins`
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='toggle')
    @commands.is_owner()
    async def toggle(self, ctx, extension=None):
        """
        Toggle a extension from the cogs or event folder with chat interaction
        """

        member = ctx.author
        embed = discord.Embed(title='',
                              description='')
        embed.add_field(name='Aus welcher Kategorie möchtest du eine Extension togglen?',
                        value='Zur verfügung stehen momentan `Cogs` und `Events`')
        embed.set_footer(text='Um den Command zu beenden schreibe einfach exit!')
        await ctx.send(embed=embed)
        while True:
            message = await self.bot.wait_for('message', check=lambda message: message.author == member)
            if 'Cogs' in message.content or 'cogs' in message.content:
                embed = discord.Embed(title='',
                                      description='')
                embed.add_field(name='Du hast **Cogs gewählt!**\n'
                                     'Hier eine Liste der Cogs:',
                                value='`administration`, `automod`, `channel`, `error_handler`, `fun`, `gifs`, `giveaway`, `info`, `math`, `moderation`, `music`, `raft`, `roles`, `rules`, `setup`, `toggle`, `utilities`, `verify`')
                embed.set_footer(text='Um den Command zu beenden schreibe einfach exit!')
                await ctx.send(embed=embed)
                while True:
                    message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                    if 'administration' in message.content:
                        embed = discord.Embed(title='Kategorie : Cogs',
                                              description='Du hast in der **Kategorie Cogs** die Extension `administration` ausgewählt.')
                        message = await ctx.send(embed=embed)
                        await asyncio.sleep(2)
                        embed = discord.Embed(title='Kategorie : Cogs, Extension : administration',
                                              description='Was möchtest du mit der Extension machen?\n'
                                                          '`reload`, `unload`, `Load`')
                        await message.edit(embed=embed)
                        while True:
                            message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                            if 'reload' in message.content:
                                self.bot.unload_extension('cogs.administration')
                                self.bot.load_extension('cogs.administration')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Reloaded the Extension `administration`')
                                await ctx.send(embed=embed)

                            if 'unload' in message.content:
                                self.bot.unload_extension('cogs.administration')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Unload the Extension `administration`')
                                await ctx.send(embed=embed)

                            if 'Load' in message.content:
                                self.bot.load_extension('cogs.administration')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Loaded the Extension `administration`')
                                await ctx.send(embed=embed)

                    if 'automod' in message.content:
                        embed = discord.Embed(title='Kategorie : Cogs',
                                              description='Du hast in der **Kategorie Cogs** die Extension `automod` ausgewählt.')
                        message = await ctx.send(embed=embed)
                        await asyncio.sleep(2)
                        embed = discord.Embed(title='Kategorie : Cogs, Extension : automod',
                                              description='Was möchtest du mit der Extension machen?\n'
                                                          '`reload`, `unload`, `Load`')
                        await message.edit(embed=embed)
                        while True:
                            message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                            if 'reload' in message.content:
                                self.bot.unload_extension('cogs.automod')
                                self.bot.load_extension('cogs.automod')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Reloaded the Extension `automod`')
                                await ctx.send(embed=embed)

                            if 'unload' in message.content:
                                self.bot.unload_extension('cogs.automod')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Unload the Extension `automod`')
                                await ctx.send(embed=embed)

                            if 'Load' in message.content:
                                self.bot.load_extension('cogs.automod')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Loaded the Extension `automod`')
                                await ctx.send(embed=embed)

                    if 'channel' in message.content:
                        embed = discord.Embed(title='Kategorie : Cogs',
                                              description='Du hast in der **Kategorie Cogs** die Extension `channel` ausgewählt.')
                        message = await ctx.send(embed=embed)
                        await asyncio.sleep(2)
                        embed = discord.Embed(title='Kategorie : Cogs, Extension : channel',
                                              description='Was möchtest du mit der Extension machen?\n'
                                                          '`reload`, `unload`, `Load`')
                        await message.edit(embed=embed)
                        while True:
                            message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                            if 'reload' in message.content:
                                self.bot.unload_extension('cogs.channel')
                                self.bot.load_extension('cogs.channel')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Reloaded the Extension `channel`')
                                await ctx.send(embed=embed)

                            if 'unload' in message.content:
                                self.bot.unload_extension('cogs.channel')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Unload the Extension `channel`')
                                await ctx.send(embed=embed)

                            if 'Load' in message.content:
                                self.bot.load_extension('cogs.channel')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Loaded the Extension `channel`')
                                await ctx.send(embed=embed)

                    if 'error_handler' in message.content:
                        embed = discord.Embed(title='Kategorie : Cogs',
                                              description='Du hast in der **Kategorie Cogs** die Extension `error_handler` ausgewählt.')
                        message = await ctx.send(embed=embed)
                        await asyncio.sleep(2)
                        embed = discord.Embed(title='Kategorie : Cogs, Extension : error_handler',
                                              description='Was möchtest du mit der Extension machen?\n'
                                                          '`reload`, `unload`, `Load`')
                        await message.edit(embed=embed)
                        while True:
                            message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                            if 'reload' in message.content:
                                self.bot.unload_extension('cogs.error_handler')
                                self.bot.load_extension('cogs.error_handler')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Reloaded the Extension `error_handler`')
                                await ctx.send(embed=embed)

                            if 'unload' in message.content:
                                self.bot.unload_extension('cogs.error_handler')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Unload the Extension `error_handler`')
                                await ctx.send(embed=embed)

                            if 'Load' in message.content:
                                self.bot.load_extension('cogs.error_handler')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Loaded the Extension `error_handler`')
                                await ctx.send(embed=embed)

                    if 'fun' in message.content:
                        embed = discord.Embed(title='Kategorie : Cogs',
                                              description='Du hast in der **Kategorie Cogs** die Extension `fun` ausgewählt.')
                        message = await ctx.send(embed=embed)
                        await asyncio.sleep(2)
                        embed = discord.Embed(title='Kategorie : Cogs, Extension : fun',
                                              description='Was möchtest du mit der Extension machen?\n'
                                                          '`reload`, `unload`, `Load`')
                        await message.edit(embed=embed)
                        while True:
                            message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                            if 'reload' in message.content:
                                self.bot.unload_extension('cogs.fun')
                                self.bot.load_extension('cogs.fun')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Reloaded the Extension `fun`')
                                await ctx.send(embed=embed)

                            if 'unload' in message.content:
                                self.bot.unload_extension('cogs.fun')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Unload the Extension `fun`')
                                await ctx.send(embed=embed)

                            if 'Load' in message.content:
                                self.bot.load_extension('cogs.fun')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Loaded the Extension `fun`')
                                await ctx.send(embed=embed)

                    if 'gifs' in message.content:
                        embed = discord.Embed(title='Kategorie : Cogs',
                                              description='Du hast in der **Kategorie Cogs** die Extension `gifs` ausgewählt.')
                        message = await ctx.send(embed=embed)
                        await asyncio.sleep(2)
                        embed = discord.Embed(title='Kategorie : Cogs, Extension : gifs',
                                              description='Was möchtest du mit der Extension machen?\n'
                                                          '`reload`, `unload`, `Load`')
                        await message.edit(embed=embed)
                        while True:
                            message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                            if 'reload' in message.content:
                                self.bot.unload_extension('cogs.gifs')
                                self.bot.load_extension('cogs.gifs')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Reloaded the Extension `gifs`')
                                await ctx.send(embed=embed)

                            if 'unload' in message.content:
                                self.bot.unload_extension('cogs.gifs')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Unload the Extension `gifs`')
                                await ctx.send(embed=embed)

                            if 'Load' in message.content:
                                self.bot.load_extension('cogs.gifs')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Loaded the Extension `gifs`')
                                await ctx.send(embed=embed)

                    if 'giveaway' in message.content:
                        embed = discord.Embed(title='Kategorie : Cogs',
                                              description='Du hast in der **Kategorie Cogs** die Extension `giveaway` ausgewählt.')
                        message = await ctx.send(embed=embed)
                        await asyncio.sleep(2)
                        embed = discord.Embed(title='Kategorie : Cogs, Extension : giveaway',
                                              description='Was möchtest du mit der Extension machen?\n'
                                                          '`reload`, `unload`, `Load`')
                        await message.edit(embed=embed)
                        while True:
                            message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                            if 'reload' in message.content:
                                self.bot.unload_extension('cogs.giveaway')
                                self.bot.load_extension('cogs.giveaway')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Reloaded the Extension `giveaway`')
                                await ctx.send(embed=embed)

                            if 'unload' in message.content:
                                self.bot.unload_extension('cogs.giveaway')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Unload the Extension `giveaway`')
                                await ctx.send(embed=embed)

                            if 'Load' in message.content:
                                self.bot.load_extension('cogs.giveaway')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Loaded the Extension `giveaway`')
                                await ctx.send(embed=embed)

                    if 'help' in message.content:
                        embed = discord.Embed(title='Kategorie : Cogs',
                                              description='Du hast in der **Kategorie Cogs** die Extension `help` ausgewählt.')
                        message = await ctx.send(embed=embed)
                        await asyncio.sleep(2)
                        embed = discord.Embed(title='Kategorie : Cogs, Extension : help',
                                              description='Was möchtest du mit der Extension machen?\n'
                                                          '`reload`, `unload`, `Load`')
                        await message.edit(embed=embed)
                        while True:
                            message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                            if 'reload' in message.content:
                                self.bot.unload_extension('cogs.help')
                                self.bot.load_extension('cogs.help')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Reloaded the Extension `help`')
                                await ctx.send(embed=embed)

                            if 'unload' in message.content:
                                self.bot.unload_extension('cogs.help')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Unload the Extension `help`')
                                await ctx.send(embed=embed)

                            if 'Load' in message.content:
                                self.bot.load_extension('cogs.help')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Loaded the Extension `help`')
                                await ctx.send(embed=embed)

                    if 'info' in message.content:
                        embed = discord.Embed(title='Kategorie : Cogs',
                                              description='Du hast in der **Kategorie Cogs** die Extension `info` ausgewählt.')
                        message = await ctx.send(embed=embed)
                        await asyncio.sleep(2)
                        embed = discord.Embed(title='Kategorie : Cogs, Extension : info',
                                              description='Was möchtest du mit der Extension machen?\n'
                                                          '`reload`, `unload`, `Load`')
                        await message.edit(embed=embed)
                        while True:
                            message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                            if 'reload' in message.content:
                                self.bot.unload_extension('cogs.info')
                                self.bot.load_extension('cogs.info')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Reloaded the Extension `info`')
                                await ctx.send(embed=embed)

                            if 'unload' in message.content:
                                self.bot.unload_extension('cogs.info')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Unload the Extension `info`')
                                await ctx.send(embed=embed)

                            if 'Load' in message.content:
                                self.bot.load_extension('cogs.info')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Loaded the Extension `info`')
                                await ctx.send(embed=embed)

                    if 'math' in message.content:
                        embed = discord.Embed(title='Kategorie : Cogs',
                                              description='Du hast in der **Kategorie Cogs** die Extension `math` ausgewählt.')
                        message = await ctx.send(embed=embed)
                        await asyncio.sleep(2)
                        embed = discord.Embed(title='Kategorie : Cogs, Extension : math',
                                              description='Was möchtest du mit der Extension machen?\n'
                                                          '`reload`, `unload`, `Load`')
                        await message.edit(embed=embed)
                        while True:
                            message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                            if 'reload' in message.content:
                                self.bot.unload_extension('cogs.math')
                                self.bot.load_extension('cogs.math')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Reloaded the Extension `math`')
                                await ctx.send(embed=embed)

                            if 'unload' in message.content:
                                self.bot.unload_extension('cogs.math')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Unload the Extension `math`')
                                await ctx.send(embed=embed)

                            if 'Load' in message.content:
                                self.bot.load_extension('cogs.math')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Loaded the Extension `math`')
                                await ctx.send(embed=embed)

                    if 'moderation' in message.content:
                        embed = discord.Embed(title='Kategorie : Cogs',
                                              description='Du hast in der **Kategorie Cogs** die Extension `moderation` ausgewählt.')
                        message = await ctx.send(embed=embed)
                        await asyncio.sleep(2)
                        embed = discord.Embed(title='Kategorie : Cogs, Extension : moderation',
                                              description='Was möchtest du mit der Extension machen?\n'
                                                          '`reload`, `unload`, `Load`')
                        await message.edit(embed=embed)
                        while True:
                            message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                            if 'reload' in message.content:
                                self.bot.unload_extension('cogs.moderation')
                                self.bot.load_extension('cogs.moderation')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Reloaded the Extension `moderation`')
                                await ctx.send(embed=embed)

                            if 'unload' in message.content:
                                self.bot.unload_extension('cogs.moderation')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Unload the Extension `moderation`')
                                await ctx.send(embed=embed)

                            if 'Load' in message.content:
                                self.bot.load_extension('cogs.moderation')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Loaded the Extension `moderation`')
                                await ctx.send(embed=embed)

                    if 'music' in message.content:
                        embed = discord.Embed(title='Kategorie : Cogs',
                                              description='Du hast in der **Kategorie Cogs** die Extension `music` ausgewählt.')
                        message = await ctx.send(embed=embed)
                        await asyncio.sleep(2)
                        embed = discord.Embed(title='Kategorie : Cogs, Extension : music',
                                              description='Was möchtest du mit der Extension machen?\n'
                                                          '`reload`, `unload`, `Load`')
                        await message.edit(embed=embed)
                        while True:
                            message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                            if 'reload' in message.content:
                                self.bot.unload_extension('cogs.music')
                                self.bot.load_extension('cogs.music')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Reloaded the Extension `music`')
                                await ctx.send(embed=embed)

                            if 'unload' in message.content:
                                self.bot.unload_extension('cogs.music')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Unload the Extension `music`')
                                await ctx.send(embed=embed)

                            if 'Load' in message.content:
                                self.bot.load_extension('cogs.music')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Loaded the Extension `music`')
                                await ctx.send(embed=embed)

                    if 'raft' in message.content:
                        embed = discord.Embed(title='Kategorie : Cogs',
                                              description='Du hast in der **Kategorie Cogs** die Extension `raft` ausgewählt.')
                        message = await ctx.send(embed=embed)
                        await asyncio.sleep(2)
                        embed = discord.Embed(title='Kategorie : Cogs, Extension : raft',
                                              description='Was möchtest du mit der Extension machen?\n'
                                                          '`reload`, `unload`, `Load`')
                        await message.edit(embed=embed)
                        while True:
                            message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                            if 'reload' in message.content:
                                self.bot.unload_extension('cogs.raft')
                                self.bot.load_extension('cogs.raft')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Reloaded the Extension `raft`')
                                await ctx.send(embed=embed)

                            if 'unload' in message.content:
                                self.bot.unload_extension('cogs.raft')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Unload the Extension `raft`')
                                await ctx.send(embed=embed)

                            if 'Load' in message.content:
                                self.bot.load_extension('cogs.raft')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Loaded the Extension `raft`')
                                await ctx.send(embed=embed)

                    if 'roles' in message.content:
                        embed = discord.Embed(title='Kategorie : Cogs',
                                              description='Du hast in der **Kategorie Cogs** die Extension `roles` ausgewählt.')
                        message = await ctx.send(embed=embed)
                        await asyncio.sleep(2)
                        embed = discord.Embed(title='Kategorie : Cogs, Extension : roles',
                                              description='Was möchtest du mit der Extension machen?\n'
                                                          '`reload`, `unload`, `Load`')
                        await message.edit(embed=embed)
                        while True:
                            message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                            if 'reload' in message.content:
                                self.bot.unload_extension('cogs.roles')
                                self.bot.load_extension('cogs.roles')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Reloaded the Extension `roles`')
                                await ctx.send(embed=embed)

                            if 'unload' in message.content:
                                self.bot.unload_extension('cogs.roles')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Unload the Extension `roles`')
                                await ctx.send(embed=embed)

                            if 'Load' in message.content:
                                self.bot.load_extension('cogs.roles')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Loaded the Extension `roles`')
                                await ctx.send(embed=embed)

                    if 'rules' in message.content:
                        embed = discord.Embed(title='Kategorie : Cogs',
                                              description='Du hast in der **Kategorie Cogs** die Extension `rules` ausgewählt.')
                        message = await ctx.send(embed=embed)
                        await asyncio.sleep(2)
                        embed = discord.Embed(title='Kategorie : Cogs, Extension : rules',
                                              description='Was möchtest du mit der Extension machen?\n'
                                                          '`reload`, `unload`, `Load`')
                        await message.edit(embed=embed)
                        while True:
                            message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                            if 'reload' in message.content:
                                self.bot.unload_extension('cogs.rules')
                                self.bot.load_extension('cogs.rules')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Reloaded the Extension `rules`')
                                await ctx.send(embed=embed)

                            if 'unload' in message.content:
                                self.bot.unload_extension('cogs.rules')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Unload the Extension `rules`')
                                await ctx.send(embed=embed)

                            if 'Load' in message.content:
                                self.bot.load_extension('cogs.rules')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Loaded the Extension `rules`')
                                await ctx.send(embed=embed)

                    if 'setup' in message.content:
                        embed = discord.Embed(title='Kategorie : Cogs',
                                              description='Du hast in der **Kategorie Cogs** die Extension `setup` ausgewählt.')
                        message = await ctx.send(embed=embed)
                        await asyncio.sleep(2)
                        embed = discord.Embed(title='Kategorie : Cogs, Extension : setup',
                                              description='Was möchtest du mit der Extension machen?\n'
                                                          '`reload`, `unload`, `Load`')
                        await message.edit(embed=embed)
                        while True:
                            message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                            if 'reload' in message.content:
                                self.bot.unload_extension('cogs.setup')
                                self.bot.load_extension('cogs.setup')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Reloaded the Extension `setup`')
                                await ctx.send(embed=embed)

                            if 'unload' in message.content:
                                self.bot.unload_extension('cogs.setup')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Unload the Extension `setup`')
                                await ctx.send(embed=embed)

                            if 'Load' in message.content:
                                self.bot.load_extension('cogs.setup')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Loaded the Extension `setup`')
                                await ctx.send(embed=embed)

                    if 'toggle' in message.content:
                        embed = discord.Embed(title='Kategorie : Cogs',
                                              description='Du hast in der **Kategorie Cogs** die Extension `toggle` ausgewählt.')
                        message = await ctx.send(embed=embed)
                        await asyncio.sleep(2)
                        embed = discord.Embed(title='Kategorie : Cogs, Extension : toggle',
                                              description='Was möchtest du mit der Extension machen?\n'
                                                          '`reload`, `unload`, `Load`')
                        await message.edit(embed=embed)
                        while True:
                            message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                            if 'reload' in message.content:
                                self.bot.unload_extension('cogs.toggle')
                                self.bot.load_extension('cogs.toggle')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Reloaded the Extension `toggle`')
                                await ctx.send(embed=embed)

                            if 'unload' in message.content:
                                self.bot.unload_extension('cogs.toggle')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Unload the Extension `toggle`')
                                await ctx.send(embed=embed)

                            if 'Load' in message.content:
                                self.bot.load_extension('cogs.toggle')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Loaded the Extension `toggle`')
                                await ctx.send(embed=embed)

                    if 'utilities' in message.content:
                        embed = discord.Embed(title='Kategorie : Cogs',
                                              description='Du hast in der **Kategorie Cogs** die Extension `utilities` ausgewählt.')
                        message = await ctx.send(embed=embed)
                        await asyncio.sleep(2)
                        embed = discord.Embed(title='Kategorie : Cogs, Extension : utilities',
                                              description='Was möchtest du mit der Extension machen?\n'
                                                          '`reload`, `unload`, `Load`')
                        await message.edit(embed=embed)
                        while True:
                            message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                            if 'reload' in message.content:
                                self.bot.unload_extension('cogs.utilities')
                                self.bot.load_extension('cogs.utilities')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Reloaded the Extension `utilities`')
                                await ctx.send(embed=embed)

                            if 'unload' in message.content:
                                self.bot.unload_extension('cogs.utilities')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Unload the Extension `utilities`')
                                await ctx.send(embed=embed)

                            if 'Load' in message.content:
                                self.bot.load_extension('cogs.utilities')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Loaded the Extension `utilities`')
                                await ctx.send(embed=embed)

                    elif 'exit' in message.content or 'Exit' in message.content:
                        embed = discord.Embed(title='Du hast die Auswahl von Cogs verlassen!',
                                              description='Jetzt kannst du `Events` auswählen, oder den command komplett verlassen mit `exit`')
                        embed.set_footer(text='You exited the selection between Cogs')
                        await ctx.send(embed=embed)
                        break

                    if 'verify' in message.content:
                        embed = discord.Embed(title='Kategorie : Cogs',
                                              description='Du hast in der **Kategorie Cogs** die Extension `verify` ausgewählt.')
                        message = await ctx.send(embed=embed)
                        await asyncio.sleep(2)
                        embed = discord.Embed(title='Kategorie : Cogs, Extension : verify',
                                              description='Was möchtest du mit der Extension machen?\n'
                                                          '`reload`, `unload`, `Load`')
                        await message.edit(embed=embed)
                        while True:
                            message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                            if 'reload' in message.content:
                                self.bot.unload_extension('cogs.verify')
                                self.bot.load_extension('cogs.verify')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Reloaded the Extension `verify`')
                                await ctx.send(embed=embed)

                            if 'unload' in message.content:
                                self.bot.unload_extension('cogs.verify')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Unload the Extension `verify`')
                                await ctx.send(embed=embed)

                            if 'Load' in message.content:
                                self.bot.load_extension('cogs.verify')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Loaded the Extension `verify`')
                                await ctx.send(embed=embed)

                    elif 'exit' in message.content or 'Exit' in message.content:
                        embed = discord.Embed(title='Du hast die Auswahl von Cogs verlassen!',
                                              description='Jetzt kannst du `Events` auswählen, oder den command komplett verlassen mit `exit`')
                        embed.set_footer(text='You exited the selection between Cogs')
                        await ctx.send(embed=embed)
                        break

            elif "Events" in message.content or 'events' in message.content:
                embed = discord.Embed(title='',
                                      description='')
                embed.add_field(name='Du hast Events gewählt!\n'
                                     'Hier ist eine Liste der Events',
                                value='`logEvents`, `onGuild`, `onJoin`, `onMessage`, `onRemove`')
                embed.set_footer(text='Um den Command zu beenden schreibe einfach exit!')
                await ctx.send(embed=embed)
                while True:
                    message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                    if 'logEvents' in message.content:
                        embed = discord.Embed(title='Kategorie : Events',
                                              description='Du hast in der **Kategorie Events** die Extension `logEvents` ausgewählt.')
                        message = await ctx.send(embed=embed)
                        await asyncio.sleep(2)
                        embed = discord.Embed(title='Kategorie : Events, Extension : logEvents',
                                              description='Was möchtest du mit der Extension machen?\n'
                                                          '`reload`, `unload`, `Load`')
                        await message.edit(embed=embed)
                        while True:
                            message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                            if 'reload' in message.content:
                                self.bot.unload_extension('events.logEvents')
                                self.bot.load_extension('events.logEvents')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Reloaded the Extension `logEvents`')
                                await ctx.send(embed=embed)

                            if 'unload' in message.content:
                                self.bot.unload_extension('events.logEvents')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Unload the Extension `logEvents`')
                                await ctx.send(embed=embed)

                            if 'Load' in message.content:
                                self.bot.load_extension('events.logEvents')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Loaded the Extension `logEvents`')
                                await ctx.send(embed=embed)

                    if 'LogEvents' in message.content or 'Logevents' in message.content:
                        embed = discord.Embed(title='Kategorie : Events',
                                              description='Du meintest wahrscheinlich die Extension `logEvents`...')
                        message = await ctx.send(embed=embed, delete_after=5)
                        await asyncio.sleep(2)
                        embed = discord.Embed(title='Kategorie : Events, Extension : logEvents',
                                              description='Was möchtest du mit der Extension machen?\n'
                                                          '`reload`, `unload`, `Load`')
                        await message.edit(embed=embed)
                        while True:
                            message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                            if 'reload' in message.content:
                                self.bot.unload_extension('events.logEvents')
                                self.bot.load_extension('events.logEvents')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Reloaded the Extension `logEvents`')
                                await ctx.send(embed=embed)

                            if 'unload' in message.content:
                                self.bot.unload_extension('events.logEvents')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Unload the Extension `logEvents`')
                                await ctx.send(embed=embed)

                            if 'Load' in message.content:
                                self.bot.load_extension('events.logEvents')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Loaded the Extension `logEvents`')
                                await ctx.send(embed=embed)

                    if 'onGuild' in message.content:
                        embed = discord.Embed(title='Kategorie : Events',
                                              description='Du hast in der **Kategorie Events** die Extension `onGuild` ausgewählt.')
                        message = await ctx.send(embed=embed)
                        await asyncio.sleep(2)
                        embed = discord.Embed(title='Kategorie : Events, Extension : onGuild',
                                              description='Was möchtest du mit der Extension machen?\n'
                                                          '`reload`, `unload`, `Load`')
                        await message.edit(embed=embed)
                        while True:
                            message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                            if 'reload' in message.content:
                                self.bot.unload_extension('events.onGuild')
                                self.bot.load_extension('events.onGuild')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Reloaded the Extension `onGuild`')
                                await ctx.send(embed=embed)

                            if 'unload' in message.content:
                                self.bot.unload_extension('events.onGuild')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Unload the Extension `onGuild`')
                                await ctx.send(embed=embed)

                            if 'Load' in message.content:
                                self.bot.load_extension('events.onGuild')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Loaded the Extension `onGuild`')
                                await ctx.send(embed=embed)

                    if 'OnGuild' in message.content or 'Onguild' in message.content:
                        embed = discord.Embed(title='Kategorie : Events',
                                              description='Du meintest wahrscheinlich die Extension `onGuild`...')
                        message = await ctx.send(embed=embed)
                        await asyncio.sleep(2)
                        embed = discord.Embed(title='Kategorie : Events, Extension : onGuild',
                                              description='Was möchtest du mit der Extension machen?\n'
                                                          '`reload`, `unload`, `Load`')
                        await message.edit(embed=embed)
                        while True:
                            message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                            if 'reload' in message.content:
                                self.bot.unload_extension('events.onGuild')
                                self.bot.load_extension('events.onGuild')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Reloaded the Extension `onGuild`')
                                await ctx.send(embed=embed)

                            if 'unload' in message.content:
                                self.bot.unload_extension('events.onGuild')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Unload the Extension `onGuild`')
                                await ctx.send(embed=embed)

                            if 'Load' in message.content:
                                self.bot.load_extension('events.onGuild')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Loaded the Extension `onGuild`')
                                await ctx.send(embed=embed)

                    if 'onJoin' in message.content:
                        embed = discord.Embed(title='Kategorie : Events',
                                              description='Du hast in der **Kategorie Events** die Extension `onJoin` ausgewählt.')
                        message = await ctx.send(embed=embed)
                        await asyncio.sleep(2)
                        embed = discord.Embed(title='Kategorie : Events, Extension : onJoin',
                                              description='Was möchtest du mit der Extension machen?\n'
                                                          '`reload`, `unload`, `Load`')
                        await message.edit(embed=embed)
                        while True:
                            message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                            if 'reload' in message.content:
                                self.bot.unload_extension('events.onJoin')
                                self.bot.load_extension('events.onJoin')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Reloaded the Extension `onJoin`')
                                await ctx.send(embed=embed)

                            if 'unload' in message.content:
                                self.bot.unload_extension('events.onJoin')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Unload the Extension `onJoin`')
                                await ctx.send(embed=embed)

                            if 'Load' in message.content:
                                self.bot.load_extension('events.onJoin')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Loaded the Extension `onJoin`')
                                await ctx.send(embed=embed)

                    if 'OnJoin' in message.content or 'Onjoin' in message.content:
                        embed = discord.Embed(title='Kategorie : Events',
                                              description='Du meintest wahrscheinlich die Extension `onJoin`...')
                        message = await ctx.send(embed=embed)
                        await asyncio.sleep(2)
                        embed = discord.Embed(title='Kategorie : Events, Extension : onJoin',
                                              description='Was möchtest du mit der Extension machen?\n'
                                                          '`reload`, `unload`, `Load`')
                        await message.edit(embed=embed)
                        while True:
                            message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                            if 'reload' in message.content:
                                self.bot.unload_extension('events.onJoin')
                                self.bot.load_extension('events.onJoin')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Reloaded the Extension `onJoin`')
                                await ctx.send(embed=embed)

                            if 'unload' in message.content:
                                self.bot.unload_extension('events.onJoin')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Unload the Extension `onJoin`')
                                await ctx.send(embed=embed)

                            if 'Load' in message.content:
                                self.bot.load_extension('events.onJoin')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Loaded the Extension `onJoin`')
                                await ctx.send(embed=embed)

                    if 'onMessage' in message.content:
                        embed = discord.Embed(title='Kategorie : Events',
                                              description='Du hast in der **Kategorie Events** die Extension `onMessage` ausgewählt.')
                        message = await ctx.send(embed=embed)
                        await asyncio.sleep(2)
                        embed = discord.Embed(title='Kategorie : Events, Extension : onMessage',
                                              description='Was möchtest du mit der Extension machen?\n'
                                                          '`reload`, `unload`, `Load`')
                        await message.edit(embed=embed)
                        while True:
                            message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                            if 'reload' in message.content:
                                self.bot.unload_extension('events.onMessage')
                                self.bot.load_extension('events.onMessage')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Reloaded the Extension `onMessage`')
                                await ctx.send(embed=embed)

                            if 'unload' in message.content:
                                self.bot.unload_extension('events.onMessage')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Unload the Extension `onMessage`')
                                await ctx.send(embed=embed)

                            if 'Load' in message.content:
                                self.bot.load_extension('events.onMessage')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Loaded the Extension `onMessage`')
                                await ctx.send(embed=embed)

                    if 'OnMessage' in message.content or 'Onmessage' in message.content:
                        embed = discord.Embed(title='Kategorie : Events',
                                              description='Du meintest wahrscheinlich die Extension `onMessage`...')
                        message = await ctx.send(embed=embed)
                        await asyncio.sleep(2)
                        embed = discord.Embed(title='Kategorie : Events, Extension : onMessage',
                                              description='Was möchtest du mit der Extension machen?\n'
                                                          '`reload`, `unload`, `Load`')
                        await message.edit(embed=embed)
                        while True:
                            message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                            if 'reload' in message.content:
                                self.bot.unload_extension('events.onMessage')
                                self.bot.load_extension('events.onMessage')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Reloaded the Extension `onMessage`')
                                await ctx.send(embed=embed)

                            if 'unload' in message.content:
                                self.bot.unload_extension('events.onMessage')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Unload the Extension `onMessage`')
                                await ctx.send(embed=embed)

                            if 'Load' in message.content:
                                self.bot.load_extension('events.onMessage')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Loaded the Extension `onMessage`')
                                await ctx.send(embed=embed)

                    if 'onRemove' in message.content:
                        embed = discord.Embed(title='Kategorie : Events',
                                              description='Du hast in der **Kategorie Events** die Extension `onRemove` ausgewählt.')
                        message = await ctx.send(embed=embed)
                        embed = discord.Embed(title='Kategorie : Events, Extension : onMessage',
                                              description='Was möchtest du mit der Extension machen?\n'
                                                          '`reload`, `unload`, `Load`')
                        await message.edit(embed=embed)
                        while True:
                            message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                            if 'reload' in message.content:
                                self.bot.unload_extension('events.onRemove')
                                self.bot.load_extension('events.onRemove')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Reloaded the Extension `onRemove`')
                                await ctx.send(embed=embed)

                            if 'unload' in message.content:
                                self.bot.unload_extension('events.onRemove')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Unload the Extension `onRemove`')
                                await ctx.send(embed=embed)

                            if 'Load' in message.content:
                                self.bot.load_extension('events.onRemove')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Loaded the Extension `onRemove`')
                                await ctx.send(embed=embed)

                    if 'OnRemove' in message.content or 'Onremove' in message.content:
                        embed = discord.Embed(title='Kategorie : Events',
                                              description='Du meintest wahrscheinlich die Extension `onRemove`...')
                        message = await ctx.send(embed=embed)
                        embed = discord.Embed(title='Kategorie : Events, Extension : onMessage',
                                              description='Was möchtest du mit der Extension machen?\n'
                                                          '`reload`, `unload`, `Load`')
                        await message.edit(embed=embed)
                        while True:
                            message = await self.bot.wait_for('message', check=lambda message: message.author == member)
                            if 'reload' in message.content:
                                self.bot.unload_extension('events.onRemove')
                                self.bot.load_extension('events.onRemove')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Reloaded the Extension `onRemove`')
                                await ctx.send(embed=embed)

                            if 'unload' in message.content:
                                self.bot.unload_extension('events.onRemove')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Unload the Extension `onRemove`')
                                await ctx.send(embed=embed)

                            if 'Load' in message.content:
                                self.bot.load_extension('events.onRemove')
                                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                                      description='Loaded the Extension `onRemove`')
                                await ctx.send(embed=embed)

                    elif 'exit' in message.content or 'Exit' in message.content:
                        embed = discord.Embed(title='Du hast die Auswahl von Events verlassen!',
                                              description='Jetzt kannst du `Cogs` auswählen, oder den command komplett verlassen mit `exit`')
                        embed.set_footer(text='You exited the selection between Cogs')
                        await ctx.send(embed=embed)
                        break

            elif 'exit' in message.content or 'Exit' in message.content:
                embed = discord.Embed(title='Du hast den Command verlassen!',
                                      description='You exited the command')
                await ctx.send(embed=embed)
                break

            else:
                embed = discord.Embed(title='',
                                      description='')
                embed.add_field(name='Ungültige Eingabe!',
                                value='Bitte benutzt `Cogs`, `Events` oder `Exit`')
                await ctx.send(embed=embed, delete_after=5)


def setup(bot):
    bot.add_cog(toggle(bot))
