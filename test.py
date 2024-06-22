import discord
import config
import pytz
import random
import requests
import os
import aiofiles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             # type: ignore
from datetime import datetime
from discord.ext import tasks, commands

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

#discord.pyの関数定義
#--------------------------------------------------------------------------------
#起動時に行う
@bot.event
async def on_ready():
    print(f"{bot.user.name}が起動したぞ")
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
#コード内をテキストファイルに変換
@bot.command()
async def scode(ctx):
    try:
        print("ここまでヨシ！")
        filename = __file__

        print("ここからが問題？")
        with open(filename, 'r') as file:
            code = file.read()
    
        temp_filename = 'code.txt'

        with open(temp_filename, 'w') as temp_file:
            temp_file.write(code)

        await ctx.send(file=discord.File(temp_filename))

    except Exception as e:
        await ctx.send(f"error{e}")

'''
    with open(filename, 'r') as file:
        code = file.read()

    temp_filename = 'code.txt'
    with open(temp_filename, 'w')as temp_file:
        temp_file.write(code)

    await ctx.send(file=discord.File(temp_filename))
'''
#--------------------------------------------------------------------------------


bot.run(config.TOKEN)