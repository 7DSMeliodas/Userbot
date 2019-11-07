from pyrobot import BOT
from pyrogram import Filters, Message
@BOT.on_message(Filters.regex("^#players:") & Filters.chat(-1001030085238) & ~Filters.edited & Filters.user(618096097))
def pin_on_start_wworigin(bot: BOT,  message: Message):
    toPin = message.message_id
    #bot.pin_chat_message(message.chat.id, toPin)
    message.reply('/pinn')
