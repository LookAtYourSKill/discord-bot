import os

import discord
from discord.ext import commands
from discord.errors import Forbidden


async def send_embed(ctx, embed):
    try:
        await ctx.send(embed=embed)
    except Forbidden:
        try:
            await ctx.send("Hey, seems like I can't send embeds. Please check my permissions :)")
        except Forbidden:
            await ctx.author.send(
                f"Hey, seems like I can't send any message in {ctx.channel.name} on {ctx.guild.name}\n"
                f"May you inform the server team about this issue? :slight_smile: ", embed=embed)


class Help(commands.Cog):
    """
    Sends this help message
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, *content):
        """Shows all modules of that bot"""

        prefix = '?'
        version = 1

        owner = 493370963807830016
        owner_name = 'LookAtYourSkill#6822'

        if not content:
            try:
                owner = ctx.guild.get_member(owner).mention

            except AttributeError as e:
                owner = owner

            emb = discord.Embed(title='Commands and modules', color=discord.Color.blue(),
                                description=f'Use `{prefix}help <module>` to gain more information about that module ')

            cogs_desc = ''
            for cog in self.bot.cogs:
                cogs_desc += f'- `{cog}`\n'  # {self.bot.cogs[cog].__doc__}\n'

            emb.add_field(name='Modules', value=cogs_desc, inline=False)

            commands_desc = ''
            for command in self.bot.walk_commands():
                if not command.cog_name and not command.hidden:
                    commands_desc += f'{command.name} - {command.help}\n'
                    print(commands_desc)

            if commands_desc:
                emb.add_field(name='Not belonging to a module', value=commands_desc, inline=False)

            emb.add_field(name="About", value=f"The Bots is developed by {owner_name}, based on discord.py.\n"
                                              f"This version of it is maintained by {owner}")

        elif len(content) == 1:

            for cog in self.bot.cogs:
                if cog.lower() == content[0].lower():

                    emb = discord.Embed(title=f'{cog} - Commands', description=self.bot.cogs[cog].__doc__,
                                        color=discord.Color.green())

                    for command in self.bot.get_cog(cog).get_commands():
                        if not command.hidden:
                            emb.add_field(name=f"`{prefix}{command.name}`", value=command.help, inline=False)
                    break

            else:
                emb = discord.Embed(title="What's that?!",
                                    description=f"I've never heard from a module called `{content[0]}` before ",
                                    color=discord.Color.orange())

        elif len(content) > 1:
            emb = discord.Embed(title="That's too much.",
                                description="Please request only one module at once ",
                                color=discord.Color.orange())

        else:
            emb = discord.Embed(title="It's a magical place.",
                                description="I don't know how you got here. But I didn't see this coming at all.",
                                color=discord.Color.red())

        await send_embed(ctx, emb)


def setup(bot):
    bot.add_cog(Help(bot))
