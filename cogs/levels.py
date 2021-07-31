import datetime
import json
import discord
import pytz
from discord.ext import commands

bot = commands.Bot(intense=discord.Intents.all(), command_prefix='?', help_command=commands.MinimalHelpCommand())
bot.remove_command('help')


class Level(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['rank'])
    async def level(self, ctx, user):
        if not user:
            id = ctx.message.author.id
            with open('C:/Users/simon/PycharmProjects/pythonProject/Discord Bot/utils/json_files/users.json', 'r') as f:
                users = json.load(f)
            level = users[str(id)]['level']
            de = pytz.timezone('Europe/Berlin')
            embed = discord.Embed(title='',
                                  description='',
                                  timestamp=datetime.datetime.utcnow().astimezone(tz=de))
            embed.set_author(name=user.name, icon_url=user.avatar_url)
            embed.add_field(name='Level',
                            value=f'```{level}```',
                            inline=True)
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f'Requested by {ctx.author}')
            await ctx.send(embed=embed)
        else:
            id = user.id
            with open('C:/Users/simon/PycharmProjects/pythonProject/Discord Bot/utils/json_files/users.json', 'r') as f:
                users = json.load(f)
            level = users[str(id)]['level']
            de = pytz.timezone('Europe/Berlin')
            embed = discord.Embed(title='',
                                  description='',
                                  timestamp=datetime.datetime.utcnow().astimezone(tz=de))
            embed.set_author(name=f'{user.name}',
                             icon_url=f'{user.avatar_url}')
            embed.add_field(name='Level',
                            value=f'```{level}```',
                            inline=True)
            embed.set_footer(text=f'Angefordert von {user.name}#{user.discriminator}', )
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f'Requested by {ctx.author}')
            await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def update_data(self, user, users):
        if not f'{user.id}' in users:
            users[f'{user.id}'] = {}
            users[f'{user.id}']['experience'] = 0
            users[f'{user.id}']['level'] = 0

    @commands.Cog.listener()
    async def add_experience(self, users, user, exp):
        users[f'{user.id}']['experience'] += exp

    @commands.Cog.listener()
    async def level_up(self, ctx, users, user):
        with open('C:/Users/simon/PycharmProjects/pythonProject/Discord Bot/utils/json_files/levels.json', 'r') as g:
            levels = json.load(g)

        experience = users[f'{user.id}']['experience']
        level_start = users[f'{user.id}']['level']
        level_end = int(experience ** (1 / 4))
        if level_start < level_end:
            embed = discord.Embed(title='🎉**Level Up**🎉',
                                  description=f'{user.name}#{user.discriminator} hat ein Level Up!\n'
                                              f'Jetzt ist er **Level: {level_end}**!')
            await ctx.send(embed=embed)
            users[f'{user.id}']['level'] = level_end

    @commands.Cog.listener()
    async def on_member_join(self):
        with open('C:/Users/simon/PycharmProjects/pythonProject/Discord Bot/utils/json_files/users.json', 'r') as f:
            users = json.load(f)

        await self.update_data(users)

        with open('C:/Users/simon/PycharmProjects/pythonProject/Discord Bot/utils/json_files/users.json', 'r') as f:
            json.dump(users, f, indent=4)

    @commands.command()
    async def update_data(self, users, user):
        if not f'{user.id}' in users:
            users[f'{user.id}'] = {}
            users[f'{user.id}']['experience'] = 0
            users[f'{user.id}']['level'] = 0

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot is False:
            with open('C:/Users/simon/PycharmProjects/pythonProject/Discord Bot/utils/json_files/users.json', 'r') as f:
                users = json.load(f)

            await self.update_data(users, message.author)
            await self.add_experience(users, message.author, 5)
            await self.level_up(users, message.author, message)

            with open('C:/Users/simon/PycharmProjects/pythonProject/Discord Bot/utils/json_files/users.json', 'w') as f:
                json.dump(users, f, indent=4)

        await bot.process_commands(message)


def setup(bot):
    bot.add_cog(Level(bot))
