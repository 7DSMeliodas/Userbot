from pyrobot import BOT
from pyrogram import Filters, Message

from random import randint


@BOT.on_message(Filters.command("d", '.'))
def dice(bot: BOT, message: Message):
    max = int(message.command[1])
    dice=randint(1,max)
    message.delete()
    #dice=str(wurf)
    max=str(max)
    dice=str(dice)
    bot.send_message(message.chat.id, "Deine Zahl aus 1 und "+ max + " beträgt: " + dice)
