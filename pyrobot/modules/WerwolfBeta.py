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
@BOT.on_message(Filters.regex("^#players:") & Filters.chat('lightwerewolf') & ~Filters.edited & Filters.user(618096097))
def pin_on_start(bot: BOT,  message: Message):
    toPin = message.message_id
    bot.pin_chat_message(message.chat.id, toPin)

# Autoextend Part: get players
@BOT.on_message(Filters.regex("^#players: (\d+)") & Filters.chat('lightwerewolf'))
def get_players(bot: BOT,  message: Message):
    global messageid
    global players
    global idplayers
    global match
    idplayers = message.message_id
    players = message.text
    match = int(players.split()[1])

# Autoextend Part: Extend
@BOT.on_message(Filters.regex("Nur noch 30 Sekunden, um beizutreten.") & Filters.user(618096097) & Filters.chat('lightwerewolf'))
def extend_if_players_too_less(bot: BOT,  message: Message):
    global messageid
    global players
    global idplayers
    global match
    int(match)
    if match < 5:
        bot.send_message(message.chat.id, "/extend@blackwerewolfbot 60")

# Pingtime info
@BOT.on_message(Filters.regex('haben eine Benachrichtigung erhalten, da sie den'))
def notify_when_pingtime_ready(bot: BOT, message: Message):
    sleep(600)
    bot.send_message(message.chat.id, "Pingtime kann wieder verwendet werden!")

# Get link to offtopic group
@BOT.on_message(Filters.command("offtopic", "#") & Filters.chat('lightwerewolf'))
def send_ot_link(bot: BOT, message: Message):
    bot.send_message(
        message.chat.id, 'Hier geht es zur Offtopic Gruppe: \n\n https://t.me/joinchat/ApybhxaNEmsRQhBu6i3sLw')

# Get Stealrate
@BOT.on_message(Filters.command("steal", "#") & Filters.chat('lightwerewolf'))
def send_ot_link(bot: BOT, message: Message):
    bot.send_message(message.chat.id, "**Dieb-Stealrate:**\n\n100% Chance:\nWolfsmensch\nDorfbewohner\nUnglücksrabe\n\n75% Chance:\nMonarch\nAlchemist\nVerfluchter\nFreimaurer\nBetrunkener\nBürgermeister\nSchütze\nBeobachter\nVerräter\nAmor\nPrinz\nNarr\n\n50% Chance:\nSchutzengel\nKultist\nSchmied\nSandmann\nWerwolf\nZauberer\nLykan\Alibiwolf\nMärtyrer\nMagier\nEule\nDorfältester\nDetektiv\nSeherlehrling\nHure\nKultbeobachter\nPazifist\nOrakle\nLucifer\nWetterbendiger\nBetawolf\nPyromane\n\n25% Chance:\nKultjäger\nAlphawolf\nSerienmörder\nMarionettenmeister\n\n0% Chance:\nDoppelgänger\nLeichenschänder")
