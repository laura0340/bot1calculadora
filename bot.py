#########################################################

from config import bot
import config
from time import sleep
import re

#########################################################

# Aquí vendrá la implementación de la lógica del bot

@bot.message_handler(commands=['start']) #decorador al comando start llama a la función de abajo
def on_command_start(message): #recibimos el mensaje, se ejecuta lo d abajo
    bot.send_chat_action(message.chat.id, 'typing') # mensaje que le sale al usuario escribiendo
    sleep(1)

    bot.send_message(
        message.chat.id,
        "Hola, soy un \U0001F916, ¿cómo estás?", # respuesta que le damos al usuario
        # para emoticones \U0001F916
        parse_mode="Markdown") # es un lenguaje para darle estilos básicos al texto







# debe ser el último de todo el código
# por el decorador, atrapa el mensaje si y solo si no coje nada más de lo que está antes
# cualquier mensaje que le llega, va a entrar por el true del mensaje
@bot.message_handler(func=lambda message: True)
def on_fallback(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)

    bot.reply_to( # responde a un mensaje en específico
        message,
        "\U0001F63F Ups, no entendí lo que me dijiste.")


#########################################################

if __name__ == '__main__':
    bot.polling(timeout=20)

#########################################################
