import discord
from discord.ext import commands


class Administration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="setstatus")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(rate=1, per=30)
    async def setstatus(self, ctx: commands.Context, *, text: str):
        await self.bot.change_presence(activity=discord.Game(name=text))
        embed = discord.Embed(title='<:open:869959941321011260> Erfolgreich',
                              description=f'Successfully changed bot status to **{text}**')
        await ctx.send(embed=embed)

    @commands.command(name='load', aliases=['activate'])
    @commands.has_permissions(administrator=True)
    async def load(self, ctx, extension):
        self.bot.load_extension(f'cogs.{extension}')
        embed = discord.Embed(title='<:open:869959941321011260> Successfully',
                              description=f'**Loaded** Extension `{extension}`')
        await ctx.send(embed=embed)

    #@load.error()
    #async def load_error(self, ctx, error, extension):
    #    if isinstance(error, commands.NotOwner):
    #        await ctx.channel.send("You must be the owner to use this command.")
    #        print(error)
    #    if isinstance(error, commands.MissingRequiredArgument):
    #        await ctx.channel.send("You must tell me which extension to load")
    #        print(error)
    #    if isinstance(error, commands.ExtensionAlreadyLoaded):
    #        await ctx.channel.send("Extension Already loaded")
    #        print(error)
    #    else:
    #         await ctx.channel.send("An error as occured, please contact the bot owner")
    #         print(error)

    @commands.command(name='unload', aliases=['deactivate'])
    @commands.has_permissions(administrator=True)
    async def unload(self, ctx, extension):
        self.bot.unload_extension(f'cogs.{extension}')
        embed = discord.Embed(title='<:open:869959941321011260> Successfully',
                              description=f'**Unloaded** Extension `{extension}`')
        await ctx.send(embed=embed)

    @commands.command(name='reload')
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx, extension):
        self.bot.unload_extension(f'cogs.{extension}')
        self.bot.load_extension(f'cogs.{extension}')
        embed = discord.Embed(title='<:open:869959941321011260> Successfully',
                              description=f'**Reloaded** Extension `{extension}`')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Administration(bot))
