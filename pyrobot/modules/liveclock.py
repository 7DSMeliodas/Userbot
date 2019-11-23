import time
from time import sleep
from pyrogram import Filters, Message
from pyrobot import BOT, LOGGER_GROUP

@BOT.on_message(Filters.command("time", ".") & Filters.me)
def delete(bot: BOT, message: Message):

    if not len(message.command) > 1:
        message.edit("<b>Wrong input!</b>\nCorrect Syntax:\n.time 20\nShow the current time for 20 seconds")
        sleep(3)
        message.delete()
        return

    i=0

    if len(message.command) > 1 and int(message.command[1]):
        endtimestr = message.command[1]
        endtime = int(endtimestr)

    while i < endtime:
        currenttime = time.localtime()
        clock = time.strftime("Current local time: %H:%M:%S", currenttime)
        bot.edit_message_text(message.chat.id, message.message_id, clock)
        i=i+1
        time.sleep(1)

@BOT.on_message(Filters.command("timedate", ".") & Filters.me)
def delete(bot: BOT, message: Message):

    if not len(message.command) > 1:
        message.edit("<b>Wrong input!</b>\nCorrect Syntax:\n.timedate 20\nShow the current time for 20 seconds")
        sleep(3)
        message.delete()
        return

    i=0

    if len(message.command) > 1 and int(message.command[1]):
        endtimestr = message.command[1]
        endtime = int(endtimestr)

    while i < endtime:
        currenttime = time.localtime()
        clock = time.strftime("Current local time/date:\n %H:%M:%S, %d.%m.%Y", currenttime)
        bot.edit_message_text(message.chat.id, message.message_id, clock)
        i=i+1
        time.sleep(1)
