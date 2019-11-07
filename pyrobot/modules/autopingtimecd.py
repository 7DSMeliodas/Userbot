from pyrobot import BOT
from pyrogram import Filters, Message
from time import sleep

@BOT.on_message(Filters.regex('haben eine Benachrichtigung erhalten, da sie den'))
def pingtime_deutsch(bot: BOT, message: Message):
    sleep(600)
    bot.send_message(message.chat.id, "Pingtime kann wieder verwendet werden!")

@BOT.on_message(Filters.regex('have all been called, because they have used'))
def pingtime_englisch(bot: BOT, message: Message):
    sleep(600)
    bot.send_message(message.chat.id, "You can use /pingtime again!")
