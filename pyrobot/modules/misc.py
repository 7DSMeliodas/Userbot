from datetime import datetime

from pyrogram import Filters, Message

from pyrobot import BOT, START_TIME

from random import randint

from pyzufall.person import Person

# -- Constants -- #

UPTIME = "Current Uptime\n{}"

# -- Constants End -- #

# Edit the sent message to display the current uptime.
@BOT.on_message(Filters.command(["up", "uptime"], ".") & Filters.me)
def uptime(bot: BOT, message: Message):
    now = datetime.now()
    uptime = now - START_TIME
    message.edit(UPTIME.format(str(uptime).split('.')[0]))

#Dice
@BOT.on_message(Filters.command("d", '.'))
def dice(bot: BOT, message: Message):
    max = int(message.command[1])
    dice=randint(1,max)
    message.delete()
    max=str(max)
    dice=str(dice)
    bot.send_message(message.chat.id, "Deine Zahl aus 1 und "+ max + " beträgt: " + dice)

@BOT.on_message(Filters.command("p", "."))
def person(bot: BOT, message: Message):
    person = Person()
    message.delete()
    bot.send_message(message.chat.id, person)
