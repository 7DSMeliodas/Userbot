from pyrobot import BOT
from pyrogram import Filters, Message
from time import sleep
import re



messageid = 0
players = 0
idplayers = 0
match = 0

@BOT.on_message(Filters.regex("^#players: (\d+)") & Filters.chat('beowc'))
def get_players(bot: BOT,  message:Message):
    global messageid
    global players
    global idplayers
    global match
    idplayers = message.message_id
    players = message.text
    match = int(players.split()[1])

@BOT.on_message(Filters.regex("Nur noch 30 Sekunden, um beizutreten.") & Filters.user(618096097) & Filters.chat('beowc'))
def extend_if_players_too_less(bot: BOT,  message:Message):
    global messageid
    global players
    global idplayers
    global match
    int(match)
    if match < 4:
        bot.send_message(message.chat.id, "/extend@blackwerewolfbot 60")
    else:
        pass