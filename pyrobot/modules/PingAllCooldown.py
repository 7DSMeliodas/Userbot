# Imports
from pyrobot import BOT
from pyrogram import Filters, Message

@BOT.on_message(Filters.regex('have all been called as they used')) & Filter.users(218011713) & Filters.users(349084097)
def notify_when_pingall_ready(bot: BOT, message: Message):
    sleep(600)
    bot.send_message(message.chat.id, "Pingall kann wieder verwendet werden!\nPingall can be used again!")
