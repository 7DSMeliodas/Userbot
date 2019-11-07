from pyrobot import BOT
from pyrogram import Filters, Message


#Add Channel here
channel = ['heilerschule']

@BOT.on_message(Filters.chat(channel))
def forward_from_bots(bot, message):
    message.forward(-396115447)
    message.forward(-324764162)
