from pyrobot import BOT
from pyrogram import Filters, Message
import time
from pyrogram import ChatPermissions

@BOT.on_message(Filters.chat('ErotikSexKontakte'))
def mute(bot: BOT,  message:Message):
    #user=message.from_user.id
    #bot.restrict_chat_member(message.chat.id, message.from_user.id, ChatPermissions(), int(time.time() + 86400))
    bot.restrict_chat_member(message.chat.id, message.from_user.id, can_send_messages = False, until_date = int(time.time() + 86400))
    #bot.restrict_chat_member(message.chat.id, message.from_user.id, ChatPermissions(can_send_messages = False), until_date = int(time.time() + 86400))
    #bot.restrict_chat_member(message.chat.id, message.from_user.id, permissions = ChatPermissions(can_send_messages = False), until_date = int(time.time() + 86400))
