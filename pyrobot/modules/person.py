from pyrobot import BOT
from pyrogram import Filters, Message
from pyzufall.person import Person

@BOT.on_message(Filters.command("p", "."))
def person(bot: BOT, message: Message):
    person = Person()
    message.delete()
    bot.send_message(message.chat.id, person)
