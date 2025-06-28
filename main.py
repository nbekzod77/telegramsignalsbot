from flask import Flask, request
import telebot
import threading
import time

# 🔐 Bevosita TOKEN va CHAT_ID
TOKEN = "7919237755:AAHTFKZ9EbZGuMCZDzBM3NIaE34Ju6C_-fk"
CHAT_ID = "6752354281"

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# 🌐 Webhook yo‘li
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
    bot.process_new_updates([update])
    return "OK", 200

# 🟢 Oddiy "home" route
@app.route("/")
def home():
    return "📡 Signal bot ishlayapti!", 200

# 💬 /start komandasi
@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(message.chat.id, "Assalomu alaykum, sardor! Bot signalga tayyor! 🚀")

# 🔁 Har 1 soatda signal yuboruvchi thread
def send_hourly_signal():
    while True:
        bot.send_message(CHAT_ID, "📡 Har 1 soatda signal yuborildi!")
        time.sleep(3600)

# 🚀 Ishga tushirish
if __name__ == "__main__":
    threading.Thread(target=send_hourly_signal).start()
    app.run(host="0.0.0.0", port=5000)
