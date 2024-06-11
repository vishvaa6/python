import telebot

api = "6905063370:AAFYe9nQLrqTQ-v9swanwUwENHafYE7rh18"

bot= telebot.TeleBot(api)

@bot.message_handler(commands=['start'])
def send_welcome(message):  
    bot.reply_to(message,"hello world") 

@bot.message_handler(commands=['n'])
def send_welcome(message):  
    bot.send_video(message.chat.id,video=open("v.mp4", "rb"))

 







bot.infinity_polling()