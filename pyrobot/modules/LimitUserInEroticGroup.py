from pyrobot import BOT
from pyrogram import Filters, Message
import time
from pyrogram import ChatPermissions

@BOT.on_message(Filters.chat('ErotikSexKontakte'))
def mute(bot: BOT,  message:Message):
    bot.restrict_chat_member(message.chat.id, message.from_user.id, ChatPermissions(), int(time.time() + 86400))
