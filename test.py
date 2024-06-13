import discord
import config

@bot.event
async def on_ready():
    print(f"{bot.user.name} started.)