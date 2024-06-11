import telebot

bot = telebot.TeleBot('6905063370:AAFYe9nQLrqTQ-v9swanwUwENHafYE7rh18')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id,"type your name? ")
    text = message.text
    
    bot.send_message(message.chat.id,text)

bot.infinity_polling()