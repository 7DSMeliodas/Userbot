from pyrobot import BOT
from pyrogram import Filters, Message
from random import randint

@BOT.on_message(Filters.command("gay", ".") & ~Filters.user('xxmeliodas') & ~Filters.user(617318636))
def gay_expect_me_and_geric(bot: BOT,  message:Message):
    userid=str(message.from_user.id)
    username=message.from_user.first_name
    gaypercent=randint(0,100)
    percent=str(gaypercent)
    message.reply('['+username+'](tg://user?id='+userid+'), du bist ' +percent +'% Schwul!')

@BOT.on_message(Filters.command("gay", ".") & Filters.user('xxmeliodas'))
def gay_me(bot: BOT,  message:Message):
    username=message.from_user.first_name
    userid=str(message.from_user.id)
    message.reply('['+username+'](tg://user?id='+userid+'), du bist 0% Schwul!')

@BOT.on_message(Filters.command("gay", ".") & Filters.user(617318636))
def gay_eric(bot: BOT,  message:Message):
    username=message.from_user.first_name
    userid=str(message.from_user.id)
    message.reply('['+username+'](tg://user?id='+userid+'), du bist 100% Schwul!')
