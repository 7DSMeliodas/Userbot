from pyrobot import BOT
from pyrogram import Filters, Message


#Add Wolfbot(s) here
bots = [618096097]

#Add Group(s) to forward
groups = [-376143735]


@BOT.on_message(Filters.chat(bots), group=1)
def forward_from_bots(bot, message):
    message.forward(-376143735)
