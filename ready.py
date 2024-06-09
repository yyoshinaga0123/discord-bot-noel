import discord
import config

from discord.ext import tasks, commands

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():                          #Bot起動時のコマンド
    print(f"{bot.user.name}が起動したぞ")       #起動したら「(Botの名前)が起動したぞ」とターミナル内に表示

bot.run(config.TOKEN)                          #これが無いと起動できない
