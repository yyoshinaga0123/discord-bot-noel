import discord
import config
import pytz
import random                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
from datetime import datetime
from discord.ext import tasks, commands

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# イベント情報を保持する辞書を作成
event_schedule = {}

@bot.event
async def on_ready():
    print(f"{bot.user.name}が起動したぞ")

@bot.event
async def on_scheduled_event_create(event):
    global event_schedule
        
    event_name = event.name
    utc_start_time = event.start_time
    
    jst = pytz.timezone('Asia/Tokyo')
    jst_start_time = utc_start_time.astimezone(jst)
    
    date_key = jst_start_time.strftime('%Y-%m-%d')
    
    # イベントスケジュールに新しいイベントを追加
    if date_key not in event_schedule:
        event_schedule[date_key] = []
    
    event_schedule[date_key].append({
        'name': event_name,
        'start_time': jst_start_time.strftime('%H:%M:%S'),
        'url': event.url
    })

    channel = bot.get_channel(config.event_koku)
    await channel.send(f'新しいイベントが作成されたでー:\n名前は「{event_name}」で、開始時間は{jst_start_time.strftime("%Y-%m-%d %H:%M:%S")}')
    await channel.send(f'イベントはこちら👇{event.url}')

@bot.command()
async def devent(ctx):
    
    today = datetime.now(pytz.timezone('Asia/Tokyo')).strftime('%Y-%m-%d')
    channel = bot.get_channel(config.event_koku)
    if today in event_schedule:
        response = f'今日のイベント一覧:\n'
        for event in event_schedule[today]:
            response += f'名前: {event["name"]}, 開始時間: {event["start_time"]}, URL: {event["url"]}\n'
    else:
        response = '今日のイベントはありません'
    
    await ctx.send(response)
'''
@bot.command()
async def wevent(ctx):
    
    week = datetime.now(pytz.timezone('Asia/Tokyo')).strftime('%Y-%m-%d')
    channel = bot.get_channel(config.event_koku)
    if week in event_schedule:
        response
'''
@bot.command()
async def mhiro(ctx):

    #channel = bot.get_channel(config.event_koku)
    hiroyuki = ['データなんかねぇよ', 'うるせぇよ', '黙れよ', '拳こそが正義', '正しいのは俺']
    random.shuffle(hiroyuki)
    
    await ctx.send(hiroyuki[0])


@bot.command()
async def hirokuji(ctx):
    
    kuji = ['大吉', '吉', '中吉', '小吉', '末吉', '凶', '大凶']
    random.shuffle(kuji)
    
    await ctx.send(kuji[0])

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    await bot.process_commands(message)

bot.run(config.TOKEN)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            1251520880941596775