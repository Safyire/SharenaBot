import discord
from discord.ext import commands
from random import choice

bot = commands.Bot(command_prefix='-S ', description='Test description!')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)


@bot.command()
async def quote():
    await bot.say(choice(['Yes?', 'My turn!', 'Let\'s go!']))


bot.run('MzgwOTQ4ODM3MDAwNTQ0MjU3.DPAF7A.0YZPgXRLDN9dqv5KCYCqaORa2nI')
