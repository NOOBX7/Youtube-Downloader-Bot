from pyrogram import Client, Filters


@Client.on_message(Filters.command(["amith"]))
async def start(client, message):
    helptxt = f"Currently Only supports Youtube Single  (No playlist) Just Send Youtube Url"
    await message.reply_text(amithtxt)
