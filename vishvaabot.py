import telebot
import time
from pytube import YouTube

bot = telebot.TeleBot("6905063370:AAFYe9nQLrqTQ-v9swanwUwENHafYE7rh18")

@bot.message_handler(commands=["start"])
def message (message):
    bot.send_message(message.chat.id,"type your url?")

@bot.message_handler(func=lambda message:True)
def message(message):
    text = message.text
    bot.send_message(message.chat.id,"hello "+text)
    
bot.infinity_polling()