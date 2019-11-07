from pyrobot import BOT
from pyrogram import Filters, Message

@BOT.on_message(Filters.command("d", "?") & Filters.me)
def delete(bot: BOT, message: Message):
    message.delete()
    BOT.delete_messages(message.chat.id, message.reply_to_message.message_id)
