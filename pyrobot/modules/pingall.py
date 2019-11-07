from pyrobot import BOT
from pyrogram import Filters, Message
from time import sleep
import math

def create_link(x):
 if x.user.username:
  return f"@{x.user.username}"
 else:
  return f"[{x.user.first_name}](tg://user?id={x.user.id})"
@BOT.on_message(Filters.command("pinga", ".") & Filters.me)
def pingall(bot: BOT,  message:Message):
  chat_members = bot.iter_chat_members(message.chat.id)
  tagable = [create_link(x) for x in chat_members if not x.user.is_bot]
  for i in range (math.ceil(len(tagable)/10)):
    toTag = tagable[i*10: (i+1)*10]
    bot.send_message(message.chat.id, " ".join(map(str, toTag)))
    sleep(1)
