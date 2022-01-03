from pyrogram import Client,filters


@app.on_message(filters.chat(chats=[kanal_id]))
def mess(client,message):
    message.forward(qabul_qiluvchi)
