import pyrogram
import os
from pyrogram import Client, filters
from pyrogram.types import Message, User


bot_token = os.getenv("BOT_TOKEN")
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bughunter0 = Client(
    "botname",
    bot_token=bot_token,
    api_id=api_id,
    api_hash=api_hash
)

@bughunter0.on_message(filters.command(["start"]))
async def start(bot, update):
    await update.reply_text("Start Message Here")

@bughunter0.on_message(filters.forwarded and filters.channel)
async def channeltag(bot, message):
   try:
       forward_msg = await message.copy(message.chat.id)
       await message.delete()
   except:
       await message.reply_text("Oops , Recheck My Admin Permissions & Try Again")
    
bughunter0.run()
