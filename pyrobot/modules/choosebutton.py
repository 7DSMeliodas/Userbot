from pyrobot import BOT
from pyrogram import Filters, Message


#Add Wolfbot(s) here
bots = [618096097]

#Add Group(s) to forward
groups = [-376143735]


@BOT.on_message(Filters.command("choose", ".") & Filters.me)
def choose_from_list(bot: BOT, message: Message):
    cmd = message.command

    if len(cmd) > 1:
        choose = " ".join(cmd[1:])
        #message.reply_to_message.click("Settings")
        bot.send_message(message.chat.id, choose)
        message.reply_to_message.click(choose) #need to get message id from bot
    else:
        bot.send_message(message.chat.id, "Something went wrong.")
