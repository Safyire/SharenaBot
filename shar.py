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


bot.run('')  # Redacted
