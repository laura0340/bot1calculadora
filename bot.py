#########################################################

from config import bot
import config
from time import sleep
import re

#########################################################

# Aquí vendrá la implementación de la lógica del bot

@bot.message_handler(commands=['ping']) # lo que el usuario pregunta
def on_command_ping(message):
    bot.send_message(
        message.chat.id, 
        'pong', #blo que le respondemos al usuario
        parse_mode="Markdown")

#########################################################

if __name__ == '__main__':
    bot.polling(timeout=20)

#########################################################
