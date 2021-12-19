import asyncio
import os
import string
import random
import discord
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw
import dateutil.parser
import requests


class utilities(commands.Cog):
    """
    `A few commands may useless my not`
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='invite', help='?invite')
    async def invite(self, ctx):
        """
        Create an invite
        - **?invite**
        """

        invite = await ctx.channel.create_invite(reason="Automated Invite")
        embed = discord.Embed(title=' ',
                              description=f'{ctx.author.mention} Invite Link zum Server **{ctx.guild.name}**\n'
                                          f'[Invite]({invite})',
                              color=0x4cd137)
        await ctx.send(embed=embed)

    @commands.command(name='botinvite', help='?botinvite')
    @commands.has_permissions(administrator=True)
    async def botinvite(self, ctx):
        """
        Get two invites, with which you can invite the bot
        - **?botinvite**
        """

        embed = discord.Embed(title=' ',
                              description=f'{ctx.author.mention} hier sind zwei Invite Links zum Bot \n'
                                          f'[Botinvite (Custom Rechte)](https://discord.com/oauth2/authorize?client_id=790965419670241281&scope=bot&permissions=261993005047)\n'
                                          f'[Botinvite (Administrator Rechte)](https://discord.com/oauth2/authorize?client_id=790965419670241281&scope=bot&permissions=8)',
                              color=0x4cd137)
        await ctx.send(embed=embed)

    @commands.command(name='embed')
    async def embed(self, ctx, *, text: str):
        """
        Create an embed with your text
        - **?embed [`text`]**
        """

        embed = discord.Embed(title='',
                              description=text)
        await ctx.send(embed=embed)

    @commands.command(name='repeat', aliases=['mimic', 'copy', 'echo'])
    async def _do_repeat(self, ctx, *, inp: str):
        """
        Repeats your input
        - **?repeat [`input`]**
        """

        await ctx.send(inp)

    @_do_repeat.error
    async def do_repeat_handler(self, ctx, error):
        """A local Error Handler for our command do_repeat.
        This will only listen for errors in do_repeat.
        The global on_command_error will still be invoked after.
        """
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'inp':
                embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                      description=f'Nach **{ctx.command}** fehlt ein Argument!',
                                      color=0x4cd137)
                await ctx.send(embed=embed, delete_after=5)
                await asyncio.sleep(1)
                await ctx.message.delete()

    @commands.command(name='invites')
    async def user_invites(self, ctx, member: discord.Member = None):
        """
        Display all invites form a user
        - **?invites [`member`]**
        """

        member = member if member else ctx.author
        invites_raw = [invite for invite in (await ctx.guild.invites()) if invite.inviter.id == member.id]
        invites: int = 0
        for invite in invites_raw:
            invites += invite.uses
        embed = discord.Embed(title='Invites',
                              color=discord.Color.blue())
        embed.add_field(name=f'Invites from {member}',
                        value=f"You've invited **{invites}** members to the server!")
        embed.set_footer(text=f'Requested by {ctx.author.name}',
                         icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        # await ctx.send(f"Member {member.mention} has {invites} invites")

    @commands.command(name='senddm')
    async def senddm(self, ctx, member: discord.Member = None, *, text=None):
        """
        Send a user a direct message with the text you want
        - **?senddm [`member`] [`text`]**
        """

        embed = discord.Embed(title='You got MAIL!', color=discord.Color.orange())
        embed.add_field(name='From:',
                        value=f"{ctx.author.mention}",
                        inline=False)
        embed.add_field(name='Message: ',
                        value=f"{text}",
                        inline=True)
        await member.send(embed=embed)

        embed = discord.Embed(title='<:open:869959941321011260> Successfully',
                              description='**Die Nachricht** wurde `Erfolgreich gesendet`!')
        await ctx.send(embed=embed, delete_after=5)
        await asyncio.sleep(1)
        await ctx.message.delete()

    @commands.command(name='password', aliases=['pw'])
    async def password(self, ctx):
        """
        Create a safe password, which only will be visible in your Direct messages for about  10 seconds
        - **?password**
        """

        length = 20
        chars = string.ascii_letters + string.digits + '!@#$%^&*()'
        random.seed = (os.urandom(1024))

        await ctx.message.author.send('Dein Passwort wurde erstellt!', delete_after=5)
        await asyncio.sleep(1)
        await ctx.message.delete()
        await ctx.message.author.send(''.join(random.choice(chars) for i in range(length)), delete_after=10)

    @commands.command(name='reminder')
    async def reminder(self, ctx, zeit=None, *, reason='Nicht angegeben'):
        """
        Creates a reminder for a time you want
        - **?reminder [`time`] [`reason`]**
        """

        time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400, "w": 604800}
        remindertime = int(zeit[:-1]) * time_convert[zeit[-1]]
        if zeit is None:
            await ctx.send('Du musst eine Zeit angeben!')
        elif reason is None:
            embed = discord.Embed(title='Error',
                                  description='You did\'nt mentioned a reason.\n'
                                              'By standard it was set to \'nicht angegeben\'!')
        else:
            embed = discord.Embed(title='Reminder',
                                  description=f'You\'ll be reminded in `{zeit}` because of `{reason}`')
            await ctx.send(embed=embed)

            await asyncio.sleep(remindertime)
            await ctx.send(f'{ctx.author.mention} i should remind you now, ``reason = {reason}``')

    @commands.command()
    async def spotify(self, ctx, user: discord.Member = None):
        """
        Check if a user listen to spotify. If yes then he'll give back a edited picture with details
        - **spotify [`member`]**
        """

        if not user:
            user = ctx.author

        user = user or ctx.author
        spotify_result = next((activity for activity in user.activities if isinstance(activity, discord.Spotify)), None)

        if spotify_result is None:
            await ctx.send(f'``{user.name}`` **is not listening to Spotify.**')

        # Images
        track_background_image = Image.open('.\\assets\\spotify_template.png')
        album_image = Image.open(requests.get(spotify_result.album_cover_url, stream=True).raw).convert('RGBA')

        # Fonts
        title_font = ImageFont.truetype('theboldfont.ttf', 16)
        artist_font = ImageFont.truetype('theboldfont.ttf', 14)
        album_font = ImageFont.truetype('theboldfont.ttf', 14)
        start_duration_font = ImageFont.truetype('theboldfont.ttf', 12)
        end_duration_font = ImageFont.truetype('theboldfont.ttf', 12)

        # Positions
        title_text_position = 150, 30
        artist_text_position = 150, 60
        album_text_position = 150, 80
        start_duration_text_position = 150, 122
        end_duration_text_position = 515, 122

        # Draws
        draw_on_image = ImageDraw.Draw(track_background_image)
        draw_on_image.text(title_text_position, spotify_result.title, 'white', font=title_font)
        draw_on_image.text(artist_text_position, f'by {spotify_result.artist}', 'white', font=artist_font)
        draw_on_image.text(album_text_position, spotify_result.album, 'white', font=album_font)
        draw_on_image.text(start_duration_text_position, '0:00', 'white', font=start_duration_font)
        draw_on_image.text(end_duration_text_position,
                           f"{dateutil.parser.parse(str(spotify_result.duration)).strftime('%M:%S')}",
                           'white', font=end_duration_font)

        # Background colour
        album_color = album_image.getpixel((250, 100))
        background_image_color = Image.new('RGBA', track_background_image.size, album_color)
        background_image_color.paste(track_background_image, (0, 0), track_background_image)

        # Resize
        album_image_resize = album_image.resize((140, 160))
        background_image_color.paste(album_image_resize, (0, 0), album_image_resize)

        # Save image
        background_image_color.convert('RGB').save('spotify.jpg', 'JPEG')

        await ctx.send(file=discord.File('spotify.jpg'))


def setup(bot):
    bot.add_cog(utilities(bot))
