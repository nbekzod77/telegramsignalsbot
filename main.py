from flask import Flask, request
import telebot
import threading
import time

# 🔐 Token va Chat ID — qo'lda belgilangan
TOKEN = "7919237755:AAHTFKZ9EbZGuMCZDzBM3NIaE34Ju6C_-fk"
CHAT_ID = "6752354281"

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# 📥 Telegram'dan kelgan so'rovni qabul qiluvchi Webhook
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
    bot.process_new_updates([update])
    return "OK", 200

# 🌐 Oddiy test sahifa
@app.route("/")
def home():
    return "📡 Signal bot ishlayapti!", 200

# 💬 /start komandasi
@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(message.chat.id, "Assalomu alaykum, sardor! Bot signalga tayyor! 🚀")

# 🧪 Har qanday xabarga test javobi
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, "✅ Men signalni qabul qildim: " + message.text)

# 🔁 Har 1 soatda signal yuboruvchi thread
def send_hourly_signal():
    while True:
        bot.send_message(CHAT_ID, "📡 Har 1 soatda signal yuborildi!")
        time.sleep(3600)

# 🚀 Botni ishga tushiramiz
if __name__ == "__main__":
    threading.Thread(target=send_hourly_signal).start()
    app.run(host="0.0.0.0", port=5000)
