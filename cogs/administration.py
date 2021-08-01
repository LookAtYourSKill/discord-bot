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
        if extension:
            await ctx.send(f'`{extension}` ist bereits aktiv!')
        self.bot.load_extension(f'cogs.{extension}')
        await ctx.send(f'Loaded Extension `{extension}`')

    @commands.command(name='unload', aliases=['deactivate'])
    @commands.has_permissions(administrator=True)
    async def unload(self, ctx, extension):
        if extension:
            await ctx.send(f'`{extension}` ist nicht aktiv!')
        self.bot.unload_extension(f'cogs.{extension}')
        await ctx.send(f'Unloaded Extension `{extension}`')

    @commands.command(name='reload')
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx, extension):
        self.bot.unload_extension(f'cogs.{extension}')
        self.bot.load_extension(f'cogs.{extension}')
        await ctx.send(f'Reloaded Extension `{extension}`')

def setup(bot):
    bot.add_cog(Administration(bot))
