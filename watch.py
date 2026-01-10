import requests
import time
import os

URL = "https://relief-ticket.jp/events/artist/31/118"
KEYWORDS = ["受付中", "販売中", "◯"]

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

found = False

def notify(msg):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )

for _ in range(4320):  # 5秒×4320=約6時間
    r = requests.get(URL, timeout=10)
    text = r.text

    if any(k in text for k in KEYWORDS):
        if not found:
            notify("🎫【SnowMan】リセール出現の可能性あり！\n今すぐ確認！\n" + URL)
            found = True
    time.sleep(5)
