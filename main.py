from flask import Flask
from threading import Thread
import time
import requests
from keep_alive import keep_alive

# === BOT SOZLAMALARI ===
TOKEN = "7919237755:AAHTFKZ9EbZGuMCZDzBM3NIaE34Ju6C_-fk"
CHAT_ID = 6752354281  # Misol: 987654321

# === TELEGRAMGA XABAR YUBORISH ===
def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

# === ISHLOVCHI SIKL ===
def run_bot():
    while True:
        send_message("✅ Bot ishga tushdi va signalga tayyor!")
        time.sleep(3600)  # Har 1 soatda signal jo‘natadi

# === FLASK KEEP ALIVE ===
keep_alive()
run_bot()