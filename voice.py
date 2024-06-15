import discord
import config
from discord.ext import tasks, commands

intents = discord.Intents.default()
intents.voice_states = True
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

bot.run(config.TOKEN)