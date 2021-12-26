import discord
from discord.ext import commands


class raft(commands.Cog):
    """
    `Only the raft theme song`
    """

    def __init__(self, client):
        self.client = client

    @commands.command(name='raft')
    async def raft(self, ctx):
        """
        Plays the most chilled song in the world. The Raft Theme song
        - **?raft**
        """

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
        embed = discord.Embed(title='',
                              description='Now playing the **Raft Theme song!**\n'
                                          ' [Link to the song :D](https://www.youtube.com/watch?v=m2P5t8UZz6o)',
                              color=discord.Color.dark_blue())
        embed.set_image(url='https://cdn.discordapp.com/attachments/864513088396591156/875455286368948235/raftpng.png')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(raft(client))
