import discord
import config
import os
from discord.ext import tasks, commands

intents = discord.Intents.default()
intents.voice_states = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name}が起動したぞ")

@bot.event
async def on_voice_state_update(member, before, after):
    botR  = bot.get_channel(config.enter_id) #テキストチャンネルのIDを貼る
    voice = [config.v_ippan, config.v_test]  #ボイスチャンネルのIDを貼る
    
    #入室通知
    if before.channel is None and after.channel and after.channel.id in voice:
        channel = after.channel
        await botR.send(f"{member}が{channel.name}に入室したぞ")
    #退室通知
    elif after.channel is None and before.channel and before.channel.id in voice:
        channel = before.channel
        await botR.send(f"{member}が{channel.name}から退室したぞ")

#コード内をテキストファイルに変換
@bot.command()
async def scode(ctx):
    filename = __file__

    with open(filename, 'r') as file:
        code = file.read()

    temp_filename = 'code.txt'
    with open(temp_filename, 'w')as temp_file:
        temp_file.write(code)

    await ctx.send(file=discord.File(temp_filename))

bot.run(config.TOKEN)