import json
import discord
import youtube_dl
from discord.ext import commands


class music(commands.Cog):
    """
    `Isn't really working at all`
    """

    def __init__(self, client):
        self.client = client

    @commands.command(name='join')
    async def join(self, ctx):
        """
        Let the player join your channel
        - **?join**
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Music"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Music) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:

            if ctx.author.voice is None:
                embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                      description=f'You\'re not in a voice channel!')
                await ctx.send(embed=embed)
            voice_channel = ctx.author.voice.channel
            if ctx.voice_client is None:
                await voice_channel.connect()
                embed = discord.Embed(title='',
                                      description='Connected to your channel!')
                await ctx.send(embed=embed)
            else:
                await ctx.voice_client.move_to(voice_channel)
                embed = discord.Embed(title='',
                                      description=' Moved to your channel!')
                await ctx.send(embed=embed)

    @commands.command(name='leave', aliases=['l', 'dis'])
    async def disconnect(self, ctx):
        """
        Let the player disconnect from the channel you wanted him to join
        - **?l**
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Music"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Music) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description='Disconnected the channel!')
            await ctx.send(embed=embed)
            await ctx.voice_client.disconnect()

    @commands.command(name='play', aliases=['p'])
    async def play(self, ctx, url):
        """
        Try to play a song from the url you send
        - **?p [`url`]**
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Music"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Music) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 - reconnect_streamed 1 -reconnect_delay_max 5',
                              'options': '-vn',
                              'executable': r'C:\ffmpeg\ffmpeg-N-103179-gac0408522a-win64-gpl\bin\ffmpeg.exe'}
            YDL_OPTIONS = {'format': "bestaudio"}
            vc = ctx.voice_client

            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
                url2 = info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
                embed = discord.Embed(description='**Started Playing**')
                await ctx.send(embed=embed)
                vc.play(source)

    @commands.command()
    async def pause(self, ctx):
        """
        Let the player pause playing the music
        - **?pause**
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Music"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Music) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description=f'Paused Playing')
            await ctx.send(embed=embed)
            ctx.voice_client.pause()

    @commands.command()
    async def resume(self, ctx):
        """
        Let the player resume playing the music
        - **?resume**
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Music"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Music) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description=f'Resumed Playing')
            await ctx.send(embed=embed)
            ctx.voice_client.resume()

    @commands.command(name='volume')
    async def volume(self, ctx: commands.Context, *, volume: int):
        """
        Sets the volume of the player
        - **?volume [`volume`]**
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Music"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Music) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            if not ctx.voice_client.is_playing:
                return await ctx.send('Nothing being played at the moment.')

            if 0 > volume > 100:
                return await ctx.send('Volume must be between 0 and 100')

            ctx.voice_client.volume = volume / 100
            await ctx.send(f'Volume of the player set to {volume}%')

    @commands.command(name='raft')
    async def raft(self, ctx):
        """
        Plays the most chilled song in the world. The Raft Theme song
        - **?raft**
        """

        with open('utils/json/active_check.json', 'r') as f:
            data = json.load(f)

        if data[str(ctx.guild.id)]["Music"] == 'false':
            embed = discord.Embed(
                description=f'Diese **Extension (Music) ist momentan deaktiviert!** Wende dich bitte an **den Owner vom Bot** (LookAtYourSkill#6666)',
                color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            if ctx.author.voice is None:
                embed = discord.Embed(title='<:close:864599591692009513> **ERROR**',
                                      description=f'You\'re not in a voice channel!')
                await ctx.send(embed=embed)
                await ctx.message.delete()
            voice_channel = ctx.author.voice.channel
            if ctx.voice_client is None:
                await voice_channel.connect()
            else:
                await ctx.voice_client.move_to(voice_channel)

            vc = ctx.voice_client
            vc.play(discord.FFmpegPCMAudio(
                'C:/Users/simon/Videos/4K Video Downloader/Raft/RAFT 1.01 Official Soundtrack   Full.mp3'))
            embed = discord.Embed(description='Now playing the **Raft Theme song!**\n'
                                              ' [Link to the song :D](https://www.youtube.com/watch?v=m2P5t8UZz6o)',
                                  color=discord.Color.dark_blue())
            embed.set_image(
                url='https://cdn.discordapp.com/attachments/864513088396591156/875455286368948235/raftpng.png')
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(music(client))
