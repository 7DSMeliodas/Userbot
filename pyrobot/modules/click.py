from pyrobot import BOT
from pyrogram import Filters, Message

@BOT.on_message(Filters.command(["click"], ".") & Filters.me)
def clicking(bot: BOT, message: Message):
    if len(message.command) > 1:
        message.reply_to_message.click(int(message.command[1]) - 1)
    else:
        message.reply_to_message.click(0)
