from pyrogram import Client, filters

api_id = 30064827
api_hash = "95664da98a77c74537af320b9fe15153"
bot_token = "8741820933:AAG_45-ca9lho7zhXmpa-ieDjyol_2qEaPQ"

app = Client("musicbot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("البوت شغال 🔥")

import os
import yt_dlp

@app.on_message(filters.command("play"))
def play(client, message):
    try:
        query = message.text.split(" ", 1)[1]
    except:
        message.reply_text("❗ اكتب اسم الأغنية بعد الأمر\nمثال: /play wail kfoury")
        return

    message.reply_text("🔎 جاري البحث عن الأغنية...")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'song.%(ext)s',
        'quiet': True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{query}", download=True)
            file = ydl.prepare_filename(info['entries'][0])

        message.reply_audio(audio=file, caption="🎧 تم تشغيل الأغنية")

        os.remove(file)

    except Exception as e:
        message.reply_text("❌ صار خطأ أثناء تحميل الأغنية")
    
app.run()
