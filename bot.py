import telebot

bot = telebot.TeleBot("8132197812:AAEftaW-q09-Sioe3gSf_nXgcWrInxvP3cE")

@bot.message_handler(['start', 'help'])
def start(msg:telebot.types.Message):
    bot.reply_to(msg, "Hello, World!")

@bot.message_handler(['goodbye'])
def goodbye(msg:telebot.types.Message):
    bot.reply_to(msg, "Goodbye, World!")

bot.infinity_polling()