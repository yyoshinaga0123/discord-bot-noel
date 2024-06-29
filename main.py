import discord
import config                     #別でconfig.pyを作り、TOKENやチャンネルIDなどを載せる

from discord.ext import tasks, commands

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

bot.run(config.TOKEN)        #これがないと起動できない
