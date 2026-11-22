
import os
import json
import urllib.request
import urllib.parse
from datetime import datetime
from zoneinfo import ZoneInfo

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHANNEL_ID = os.getenv("CHANNEL_ID", "@konjo_bingo")
POST_TYPE = os.getenv("POST_TYPE", "morning")

today = datetime.now(ZoneInfo("Africa/Addis_Ababa"))
day = today.day

morning_posts = [
    "🌅 መልካም ጠዋት ውድ የቆንጆ ቢንጎ ቤተሰቦች!\n\nአዲስ ቀን፣ አዲስ ተስፋ፣ አዲስ ደስታ። ቀናችሁ በሰላም ይሁን! 💜\n\n🎮 @Kkonjobingo_bot",
    "☀️ ለክቡራን ደንበኞቻችን መልካም ቀን!\n\nደስታን ከወዳጆቻችን ጋር ማጋራት ውብ ነው። 💛\n\n🎮 @Kkonjobingo_bot"
]

noon_posts = [
    "💜 ውድ የቆንጆ ቢንጎ ቤተሰቦች፣ ዛሬ ቀናችሁ እንዴት እየሄደ ነው?\n\nበኮሜንት ደስታችሁን አጋሩን! 👇",
    "👑 የቆንጆ ቢንጎ ውድ ደንበኞች፣ ምን አይነት የጨዋታ ጊዜ ይመቻችኋል?\n\nአስተያየታችሁን አጋሩን! 💜"
]

evening_posts = [
    "🌙 መልካም ምሽት የቆንጆ ቢንጎ ቤተሰቦች!\n\nየጨዋታ ጊዜያችንን በደስታ እና በመዝናናት እናሳልፍ። 🎉\n\n🎮 ቦታችን: @Kkonjobingo_bot",
    "✨ ምሽቱን በደስታ እናሳምር!\n\nቆንጆ ቢንጎ — ደስታው ከእኛ ጋር ነው! 💜\n\n🎮 @Kkonjobingo_bot"
]

posts = {
    "morning": morning_posts,
    "noon": noon_posts,
    "evening": evening_posts
}

if POST_TYPE not in posts:
    raise ValueError("POST_TYPE must be morning, noon, or evening")

message = posts[POST_TYPE][day % len(posts[POST_TYPE])]

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = urllib.parse.urlencode({
    "chat_id": CHANNEL_ID,
    "text": message
}).encode()

request = urllib.request.Request(url, data=payload)

with urllib.request.urlopen(request, timeout=30) as response:
    result = json.loads(response.read().decode())

if not result.get("ok"):
    raise RuntimeError(f"Telegram API error: {result}")

print(f"Successfully posted {POST_TYPE} message.")

