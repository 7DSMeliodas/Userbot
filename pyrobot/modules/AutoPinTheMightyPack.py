from pyrobot import BOT
from pyrogram import Filters, Message

@BOT.on_message(Filters.regex("^#players: (\d+)") & Filters.chat('themightypack') & ~Filters.edited)
def pin_on_start(bot: BOT,  message:Message):
    toPin = message.message_id
    bot.pin_chat_message(message.chat.id, toPin)
