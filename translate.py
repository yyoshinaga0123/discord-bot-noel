import discord
import requests
import os
import config
from discord.ext import tasks, commands

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

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

@bot.event
async def on_ready():
    print(f"{bot.user.name}が起動したぞ")

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

bot.run(config.TOKEN)