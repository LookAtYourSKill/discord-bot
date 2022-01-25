import asyncio
import json
import discord
from discord.ext import commands


class administration(commands.Cog):
    """
    `Admin commands`
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="setstatus")
    @commands.is_owner()
    @commands.cooldown(rate=30, per=1)
    async def setstatus(self, ctx: commands.Context, *, text: str):
        """
        Change or set the status for the bot
        **Usage :** ``?setstatus [text]``
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Administration"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Administration) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            await self.bot.change_presence(activity=discord.Game(name=text))
            embed = discord.Embed(title='<:open:869959941321011260> Erfolgreich',
                                  description=f'Successfully changed bot status to **{text}**')
            await ctx.send(embed=embed, delete_after=5)
            await asyncio.sleep(1)
            await ctx.message.delete()

    @commands.command(name='lock', aliases=['lockdown'])
    @commands.has_permissions(administrator=True)
    async def lock(self, ctx):
        """
        Lock a channel, so nobody can write in it
        **Usage :** ``?lock``
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Administration"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Administration) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            with open('utils/json/on_guild.json', 'r') as f:
                guild_data = json.load(f)

            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
            embed = discord.Embed(description=f'`{ctx.channel}` ist nun **im Lockdown**',
                                  color=0x4cd137)
            embed.add_field(name='**Information**',
                            value=f'Channel im Lockdown : `{ctx.channel}`\n'
                                  f'In Lockdown gesetzt von : `{ctx.author}`')
            await ctx.send(embed=embed, delete_after=5)
            await asyncio.sleep(1)
            await ctx.message.delete()

            if guild_data[str(ctx.guild.id)]["moderation_log_channel"]:
                channel = self.bot.get_channel(id=guild_data[str(ctx.guild.id)]['moderation_log_channel'])
                await channel.send(embed=embed)
            else:
                return

    @commands.command(name='release', aliases=['unlock'])
    @commands.has_permissions(administrator=True)
    async def unlock(self, ctx):
        """
        Unlock the channel you locked before
        **Usage :** ``?unlock``
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Administration"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Administration) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            with open('utils/json/on_guild.json', 'r') as f:
                guild_data = json.load(f)

            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)

            embed = discord.Embed(description=f'`{ctx.channel}` ist nun **nicht mehr im Lockdown**',
                                  color=0x4cd137)
            embed.add_field(name='**Information**',
                            value=f'Unlocked Channel : `{ctx.channel}`\n'
                                  f'Aus dem Lockdown genommen von : `{ctx.author}`')
            await ctx.send(embed=embed, delete_after=5)
            await asyncio.sleep(1)
            await ctx.message.delete()

            if guild_data[str(ctx.guild.id)]["moderation_log_channel"]:
                channel = self.bot.get_channel(id=guild_data[str(ctx.guild.id)]['moderation_log_channel'])
                await channel.send(embed=embed)
            else:
                return

    @commands.command(aliases=['announce'])
    @commands.has_permissions(administrator=True)
    async def say(self, ctx, *, text):
        """
        Give back your text with a `@everyone` at the beginning!
        **Usage :** ``?say [text]``
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Administration"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Administration) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            role = ctx.guild.default_role
            await ctx.send(f'{role}, {text}')

    @commands.command(name='load')
    @commands.is_owner()
    async def load(self, ctx, cog):
        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Administration"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Administration) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            try:
                self.bot.load_extension(f'cogs.{cog}')
                embed = discord.Embed(description=f'Das `Modul {cog}` wurde **erfolgreich geladen!**',
                                      color=discord.Color.green())
                await ctx.send(embed=embed)
            except discord.Forbidden:
                embed = discord.Embed(
                    description=f'Ein Fehler ist aufgetreten... Eventuell gibt es die Extension `{cog}` garnicht... Überprüfe bitte deine schreibweise!',
                    color=discord.Color.red())
                await ctx.send(embed=embed)

    @commands.command(name='unload')
    @commands.is_owner()
    async def unload(self, ctx, cog):
        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Administration"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Administration) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            try:
                self.bot.unload_extension(f'cogs.{cog}')
                embed = discord.Embed(description=f'Das `Modul {cog}` wurde **erfolgreich entladen!**',
                                      color=discord.Color.green())
                await ctx.send(embed=embed)
            except discord.Forbidden:
                embed = discord.Embed(
                    description=f'Ein Fehler ist aufgetreten... Eventuell gibt es die Extension `{cog}` garnicht... Überprüfe bitte deine schreibweise!',
                    color=discord.Color.red())
                await ctx.send(embed=embed)

    @commands.command(name='reload')
    @commands.is_owner()
    async def reload(self, ctx, cog):
        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Administration"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Administration) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            try:
                self.bot.unload_extension(f'cogs.{cog}')
                self.bot.load_extension(f'cogs.{cog}')
                embed = discord.Embed(description=f'Das `Modul {cog}` wurde **erfolgreich neu geladen!**',
                                      color=discord.Color.green())
                await ctx.send(embed=embed)
            except discord.Forbidden:
                embed = discord.Embed(
                    description=f'Ein Fehler ist aufgetreten... Eventuell gibt es die Extension `{cog}` garnicht... Überprüfe bitte deine schreibweise!',
                    color=discord.Color.red())
                await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(administration(bot))
