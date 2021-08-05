from datetime import datetime
import datetime
import discord
from discord.ext import commands


class Report(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['r'])
    async def report(self, ctx, member: discord.Member = None, *, report=None):
        report_channel = discord.utils.get(ctx.guild.channels, name='reports')
        if member is None:
            return await ctx.send("Bitte nenne einen Spieler, den du ``reporten`` willst!")
        if report is None:
            return await ctx.send("Bitte gebe Infos zum Report!")
        else:
            embed = discord.Embed(title="Report", description=f"{ctx.author.mention} wurde reported von {member} ",
                                  colour=0x52b788)
            embed.set_thumbnail(url="")
            embed.add_field(name="Mehr Informationen:", value=f"{report}")
            embed.set_footer(icon_url=ctx.author.avatar_url,
                             text=f"Reagiere mit dem Emoji wenn du den Report abschicken willst, und den User reporten willst!")
            report_message = await report_channel.send(embed=embed)
            await report_message.add_reaction('✅')
            await report_message.add_reaction('❌')

            try:
                def check(reaction, user):
                    return user == ctx.author and str(reaction.emoji) in ["✅", "❌"]

                reaction, user = await self.bot.wait_for("reaction_add", timeout=60000, check=check)

                if str(reaction.emoji) == "✅":
                    embed2 = discord.Embed(title="Report Info | Angenommen",
                                           description=f"Der Report von {ctx.author.mention} wurde  angenommen!",
                                           colour=0x52b788)
                    embed2.set_footer(icon_url=ctx.author.avatar_url,
                                      text=f"Spieler report angenommen!"
                                      )

                    await ctx.author.send(embed=embed2)
                    await ctx.send(embed=embed2)

                elif str(reaction.emoji) == "❌":
                    embed3 = discord.Embed(title="Report Info | Abgelehnt",
                                           description=f"Der Report von {ctx.author.mention} wurde abgelehnt!",
                                           colour=0x52b788)
                    embed3.set_footer(icon_url=ctx.author.avatar_url,
                                      text=f"Spieler Report abgelehnt!"
                                      )

                    await ctx.author.send(embed=embed3)
                    await ctx.send(embed=embed3)

            except Exception as e:
                print(e)

def setup(bot):
    bot.add_cog(Report(bot))
