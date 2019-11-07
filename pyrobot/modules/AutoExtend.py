# Imports
from pyrobot import BOT
from pyrogram import Filters, Message
from time import sleep
import re

# Vars for autoextend
messageid = 0
players = 0
idplayers = 0
match = 0

# Autoextend Part: get players
@BOT.on_message(Filters.regex("^#players: (\d+)") & Filters.chat('lightwerewolf'))
def get_players_lightwerewolf(bot: BOT,  message: Message):
    global messageid
    global players
    global idplayers
    global match
    idplayers = message.message_id
    players = message.text
    match = int(players.split()[1])

# Autoextend Part: Extend
@BOT.on_message(Filters.regex("Nur noch 30 Sekunden, um beizutreten.") & Filters.user(618096097) & Filters.chat('lightwerewolf'))
def extend_if_players_too_less_lightwerewolf(bot: BOT,  message: Message):
    global messageid
    global players
    global idplayers
    global match
    int(match)
    if match < 5:
        bot.send_message(message.chat.id, "/extend@blackwerewolfbot 60")

# Autoextend Part: get players
@BOT.on_message(Filters.regex("^#players: (\d+)") & Filters.chat('-1001280664204'))
def get_players_starlightwerewolf(bot: BOT,  message: Message):
    global messageid
    global players
    global idplayers
    global match
    idplayers = message.message_id
    players = message.text
    match = int(players.split()[1])

# Autoextend Part: Extend
@BOT.on_message(Filters.regex("30 seconds left to join") & Filters.user(618096097) & Filters.chat('starlightwerewolf'))
def extend_if_players_too_less_starlightwerewolf(bot: BOT,  message: Message):
    global messageid
    global players
    global idplayers
    global match
    int(match)
    if match < 5:
        bot.send_message(message.chat.id, "/extend@blackwerewolfbot 60")
