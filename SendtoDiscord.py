import discord
from discord.ext import commands

import PySimpleGUI as gui

token = 'ENTER-YOUR-BOT-TOKEN-HERE'
prefix = '&' # put in any random bot prefix. its not like its going to be used anyway

bot = commands.Bot(command_prefix=prefix) # initalizing the bot

@bot.event
async def on_ready():
    print('Bot online!')
    while True:
        text = gui.PopupGetText('Python to Discord\nPlease enter something to be sent to that Discord server.')
        await bot.send_message(bot.get_channel('ENTER YOUR CHANNEL ID HERE'), text)
    
bot.run(token)
