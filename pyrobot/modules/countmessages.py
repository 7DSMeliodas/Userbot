from pyrobot import BOT
from pyrogram import Filters, Message

@BOT.on_message(Filters.command("cm", ".") & Filters.me)
def COUNTMESSAGES(bot: BOT, message: Message):
    counter = bot.get_history_count(message.chat.id)
    message.edit(f"{counter} Posts in this Group")
