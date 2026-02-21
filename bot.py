import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(msg):
    bot.send_message(msg.chat.id, "Бот запущен и работает 🚀")

@bot.message_handler(func=lambda m: True)
def echo(msg):
    bot.send_message(msg.chat.id, "Сообщение получено ✅")

print("Bot started...")
bot.infinity_polling()
