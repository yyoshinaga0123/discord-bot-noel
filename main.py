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

# イベント情報を保持する辞書を作成
event_schedule = {}



#関数定義
#--------------------------------------------------------------------------------
#和訳、英訳してくれる
def translate_text(text, target_lang='EN'):
    url = "https://api-free.deepl.com/v2/translate"
    params = {
        "auth_key": config.D_TOKEN,
        "text": text,
        "target_lang": target_lang
    }
    response = requests.post(url, data=params)

    result = response.json()
    return result['translations'][0]['text']

def jtranslate_text(text, target_lang='JA'):
    url = "https://api-free.deepl.com/v2/translate"
    params = {
        "auth_key": config.D_TOKEN,
        "text": text,
        "target_lang": target_lang
    }
    response = requests.post(url, data=params)

    result = response.json()
    return result['translations'][0]['text']
#--------------------------------------------------------------------------------



#discord.pyの関数定義
#--------------------------------------------------------------------------------
#起動時に行う
@bot.event
async def on_ready():
    print(f"{bot.user.name}が起動したぞ")
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
#イベントが作成されたら通知する
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
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
#書かれた文についての処理
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    channel = config.t_id

    #日本語から英語へ
    if message.content.startswith('!jtr'):
        try:
            text_to_translate = message.content[len('!jtr '):]
            translated_text = translate_text(text_to_translate)
            await message.channel.send(translated_text)
        except Exception as e:
            await message.channel.send(f"Erroe: {e}")

    #英語から日本語へ
    if message.content.startswith('!tr'):
        try:
            jtext_to_translate = message.content[len('!tr '):]
            jtranslated_text = jtranslate_text(jtext_to_translate)
            await message.channel.send(jtranslated_text)
        except Exception as e:
            await message.channel.send(f"Erroe: {e}")


    #await bot.process_commands(message)
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
#ボイチャの入退室を通知する
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
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
#当日のイベント一覧を表示する
@bot.command()
async def devent(ctx):
    
    today = datetime.now(pytz.timezone('Asia/Tokyo')).strftime('%Y-%m-%d')
    channel = bot.get_channel(config.event_koku)  #イベント告知用
    if today in event_schedule:
        response = f'今日のイベント一覧:\n'
        for event in event_schedule[today]:
            response += f'名前: {event["name"]}, 開始時間: {event["start_time"]}, URL: {event["url"]}\n'
    else:
        response = '今日のイベントはありません'
    
    await ctx.send(response)
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