from pyrobot import BOT
from pyrogram import Filters, Message

@BOT.on_message(Filters.regex("@werewolf2_0"))
def anti_ww_20_spam(bot: BOT,  message:Message):
    message.delete()
