import DiscordUtils as DiscordUtils
from discord.ext import commands
from discord.ext.commands import bot
#lol
music = DiscordUtils.Music()


class MusicBot(commands.Cog):
    def __init__(self, ctx):
        self.bot = bot

    @commands.command(aliases=['j'])
    async def join(self, ctx):
        voicetrue = ctx.author.voice
        if voicetrue is None:
            return await ctx.send('You are not Connected to a voice channel!')
        await ctx.author.voice.channel.connect()
        await ctx.send('Joined your Channel!')

    @commands.command(aliases=['l'])
    async def leave(self, ctx):
        voicetrue = ctx.author.voice
        mevoicetrue = ctx.guild.me.voice
        if voicetrue is None:
            return await ctx.send('You are not connected to a Channel!')
        if mevoicetrue is None:
            return await ctx.send('I am currently in a voice channel!')
        await ctx.voice_client.disconnect()
        await ctx.send('Left your Channel!')

    @commands.command(aliases=['p'])
    async def play(self, ctx, *, url):
        player = music.get_player(guild_id=ctx.guild.id)
        if not player:
            player = music.create_player(ctx, ffmpeg_error_betterfix=True)
        if not ctx.voice_client.is_playing():
            await player.queue(url, search=True)
            song = await player.play()
            await ctx.send(f'I have started playing `{song.name}`!')
        else:
            song = await player.queue(url, search=True)
            await ctx.send(f'`{song.name}` has been added to playlist!')

    @commands.command()
    async def resume(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.resume()
        await ctx.send(f'Resumed Playing {song.name}!')

    @commands.command()
    async def pause(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.pause()
        await ctx.send(f'Paused Playing {song.name}!')

    @commands.command()
    async def queue(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        await ctx.send(','.join([song.name for song in player.current_queue()]))

    @commands.command()
    async def loop(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.toggle_song_loop()
        if song.is_looping:
            return await ctx.send(f'{song.name} is looping!')
        else:
            return await ctx.send(f'{song.name} is not looping!')

    @commands.command(aliases=['np'])
    async def nowplaying(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.now_playing()
        await ctx.send(f'The Song : {song.name} is now playing!')

    @commands.command(aliases=['remove'])
    async def remove_queue(self, ctx, index):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.remove_from_queue(int(index))
        await ctx.send(f'Removed {song.name} from queue!')

    @commands.command()
    async def skip(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.skip()
        await ctx.send(f'Skipped the song {song.name}!')


def setup(bot):
    bot.add_cog(MusicBot(bot))
