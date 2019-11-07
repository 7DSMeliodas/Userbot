from pyrobot import BOT
from pyrogram import Filters, Message
from time import sleep

@BOT.on_message(Filters.command("mention", ".") & Filters.me)
def person(bot: BOT, message: Message):
    for x in bot.iter_chat_members(message.chat.id):
        bot.send_message(message.chat.id, "[\u200E](tg://user?id={})".format(x.user.id)).delete()
        message.delete()
        sleep(1)
