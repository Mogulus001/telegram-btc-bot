import os
import time
import requests

TOKEN = os.getenv("TG_BOT_TOKEN")
CHAT_ID = os.getenv("TG_CHAT_ID")

def send_message(text):
    """Send message to your Telegram via your bot"""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=payload)

if __name__ == "__main__":
    send_message("✅ Bot started: monitoring BTC/USDT 15m for break & retest.")
    while True:
        time.sleep(900)  # every 15 minutes
        send_message("🔍 Checking BTC/USDT 15m for break & retest setup...")
