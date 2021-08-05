import discord
from discord.ext import commands


class createRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='CreateGaw', aliases=['gawrole', 'creategaw'])
    @commands.has_permissions(manage_roles=True)
    async def createGAWRole(self, ctx):
        for role in ctx.guild.roles():
            if role.name == 'Giveaway':
                embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                      description=f'Diese Rolle **existiert bereits!**')
                await ctx.send(embed=embed)
            else:
                giveawayrole = await ctx.guild.create_role(name="Giveaway", color=discord.Color.green())
                embed = discord.Embed(title='<:open:869959941321011260> Successful',
                                      description=f'`Die Rolle` **{giveawayrole}** `wurde erfolgreich erstellt!`')
                await ctx.send(embed=embed)

    @commands.command(name='CreateMute', aliases=['muterole', 'createmute'])
    @commands.has_permissions(manage_roles=True)
    async def createMute(self, ctx):
        try:
            for role in ctx.guild.roles():
                if role.name == 'Muted':
                    embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                          description='Diese Rolle **existiert bereits!**')
                    await ctx.send(embed=embed)
        except:
            muteRole = await ctx.guild.create_role(name='Muted')
            for channel in ctx.guild.channels():
                await channel.set_permissions(muteRole,
                                              speak=False,
                                              send_messages=False,
                                              read_messages=True,
                                              read_message_history=True,
                                              )
                embed = discord.Embed(title='<:open:869959941321011260>',
                                      description=f'Die Rolle `{muteRole} wurde erfolgreich erstellt!`')
                await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(createRoles(bot))