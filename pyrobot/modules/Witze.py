# Imports
from pyrobot import BOT
from pyrogram import Filters, Message
import random

@BOT.on_message(Filters.command("witz", "."))
def witz(bot, message):
    l = ['"Am Abend ist mit Einbruch der Dunkelheit zu rechnen."', '"Treffen sich zwei Rühreier sagt das eine: „Man bin ich heute durcheinander.“"', '"Aus Spaß wurde ernst. Ernst ist jetzt 3 Jahre alt."']
    for x in random.sample(l, len(l)):
        bot.send_message(message.chat.id, x)
