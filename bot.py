from pyrogram import Client, filters

api_id = 30064827
api_hash = "95664da98a77c74537af320b9fe15153"
bot_token ="8741820933:AAG_45-ca9lho7zhXmpa-ieDjyol_2qEaPQ
"

app = Client("musicbot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("البوت شغال 🔥")

app.run()
