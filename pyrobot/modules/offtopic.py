from pyrobot import BOT
from pyrogram import Filters, Message

@BOT.on_message(Filters.command("offtopic", "#") & ~Filters.chat('-1001098636923') & ~Filters.chat('-1001109500936'))
def send_ot_link(bot: BOT, message: Message):
    bot.send_message(message.chat.id, 'Hier geht es zur Offtopic Gruppe: \n\n https://t.me/joinchat/ApybhxaNEmsRQhBu6i3sLw')
