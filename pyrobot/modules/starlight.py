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

# Autopin every players message
@BOT.on_message(Filters.regex("^#players:") & Filters.chat('starlightwerewolf') & ~Filters.edited & Filters.user(618096097))
def pin_on_start(bot: BOT,  message: Message):
    toPin = message.message_id
    #bot.pin_chat_message(message.chat.id, toPin, disable_notification=True)

# Autoextend Part: get players
@BOT.on_message(Filters.regex("^#players: (\d+)") & Filters.chat('starlightwerewolf'))
def get_players(bot: BOT,  message: Message):
    global messageid
    global players
    global idplayers
    global match
    idplayers = message.message_id
    players = message.text
    match = int(players.split()[1])

# Autoextend Part: Extend
@BOT.on_message(Filters.regex("30 seconds left to join") & Filters.user(618096097) & Filters.chat('starlightwerewolf'))
def extend_if_players_too_less(bot: BOT,  message: Message):
    global messageid
    global players
    global idplayers
    global match
    int(match)
    if match < 5:
        bot.send_message(message.chat.id, "/extend@blackwerewolfbot 60")
