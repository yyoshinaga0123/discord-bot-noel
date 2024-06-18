import discord
import config
import os
from discord.ext import tasks, commands
from discord.ui import Button, View

intents = discord.Intents.default()
intents.voice_states = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name}が起動したぞ！")
    await bot.change_presence(activity=discord.Game("コーディング"))


@bot.command()
async def button(ctx):
    

    #view = View()
    #view.add_item(Button(label="1番"), style=discord.ButtonStyle.green, custom_id="button1")
    #view.add_item(Button(label="2番"), style=discord.ButtonStyle.red, custom_id="button2")

    button1 = Button(label="1番", style=discord.ButtonStyle.green, custom_id="button1")
    button2 = Button(label="2番", style=discord.ButtonStyle.red, custom_id="button2")

    view = View()
    view.add_item(button1)
    view.add_item(button2)

    await ctx.send("ボタンをくりっくせよ.", view=view)

@bot.event
async def on_interaction(interaction):
    if interaction.type == discord.InteractionType.component:
        custom_id = interaction.data['custom_id']
        if custom_id == "button1":
            await interaction.response.send_message("1番ボタンが押された")
        elif custom_id == "button2":
            await interaction.response.send_message("2番ボタンが押された")




bot.run(config.TOKEN)