from pyrogram import Client, filters

api_id = 30064827
api_hash = "95664da98a77c74537af320b9fe15153"
bot_token = "8741820933:AAG_45-ca9lho7zhXmpa-ieDjyol_2qEaPQ"

app = Client("musicbot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("🔎 جاري البحث عن @app.on_message(filters.regex("^(تشغيل|شغل|play|اغنية)"))
def play(client, message):
    text = message.text.strip()

    # حذف الكلمة الأولى (تشغيل / شغل / ...)
    parts = text.split(" ", 1)
    if len(parts) < 2:
        message.reply_text("❗ اكتب اسم الأغنية بعد الأمر\nمثال: تشغيل وائل كفوري")
        return

    query = parts[1]

    msg = message.reply_text("🔎 جاري البحث عن الأغنية...")

    ydl_opts = {
        'format': 'bestaudio',
        'outtmpl': 'song.%(ext)s',
        'quiet': True,
        'noplaylist': True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch1:{query}", download=True)
            file = ydl.prepare_filename(info['entries'][0])

        msg.edit("📥 جاري إرسال الأغنية...")

        message.reply_document(file, caption=f"🎧 {query}")

        os.remove(file)

        msg.delete()

    except Exception as e:
        print(e)
        msg.edit("❌ فشل تحميل الأغنية، جرّب اسم أوضح")

app.run()
