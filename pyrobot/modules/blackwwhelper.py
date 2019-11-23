from pyrobot import BOT
from pyrogram import Filters, Message
from time import sleep

controllers = [172623926, 43817863, 690115613]

#Start Games

@BOT.on_message(Filters.command("sg", ".") & Filters.user(controllers))
def game(bot: BOT, message: Message):
    print('Trigger')
    delmsg = asyncio.create_task(message.delete())
    print('Del messaged')
    send_start = asyncio.create_task(
        bot.send_message(message.chat.id, "/startgame@blackwerewolfbot"))
    print('send startgame')
    delmsg
    print('delmsg')
    send_start
    print('start')

@BOT.on_message(Filters.command("sc", ".") & Filters.user(controllers))
def chaos(bot: BOT, message: Message):
        message.delete()
        bot.send_message(message.chat.id, "/startchaos@blackwerewolfbot")

@BOT.on_message(Filters.command("sf", ".") & Filters.user(controllers))
def foolish(bot: BOT, message: Message):
        message.delete()
        bot.send_message(message.chat.id, "/startfoolish@blackwerewolfbot")

@BOT.on_message(Filters.command("sr", ".") & Filters.user(controllers))
def foolish(bot: BOT, message: Message):
        message.delete()
        bot.send_message(message.chat.id, "/startromance@blackwerewolfbot")

@BOT.on_message(Filters.command("sm", ".") & Filters.user(controllers))
def mighty(bot: BOT, message: Message):
        message.delete()
        bot.send_message(message.chat.id, "/startmighty@blackwerewolfbot")

@BOT.on_message(Filters.command("scl", ".") & Filters.user(controllers))
def classic(bot: BOT, message: Message):
        message.delete()
        bot.send_message(message.chat.id, "/startclassic@blackwerewolfbot")

@BOT.on_message(Filters.command("scu", ".") & Filters.user(controllers))
def cultus(bot: BOT, message: Message):
        message.delete()
        bot.send_message(message.chat.id, "/startcultus@blackwerewolfbot")

#Extend / UserBefehle

@BOT.on_message(Filters.command("e", ".") & Filters.user(controllers))
def extend(bot: BOT, message: Message):
    if len(message.command) > 1 and int(message.command[1]):
        etime = message.command[1]
        bot.send_message(message.chat.id, "/extend@blackwerewolfbot " + etime)
    else:
        bot.send_message(message.chat.id, "/extend@blackwerewolfbot")
    message.delete()

@BOT.on_message(Filters.command("join", ".") & Filters.user(controllers))
def joining(bot: BOT, message: Message):
    result = message.reply_to_message.click(0)
    message.delete()
    code = result.replace("https://t.me/blackwerewolfbot?start=", "")
    bot.send_message(message.reply_to_message.from_user.id, "/start " + code)

@BOT.on_message(Filters.command("wait", ".") & Filters.user(controllers))
def nextgame(bot: BOT, message: Message):
    message.delete()
    bot.send_message(message.chat.id, "/nextgame@blackwerewolfbot")

@BOT.on_message(Filters.command("flee", ".") & Filters.user(controllers))
def flee(bot: BOT, message: Message):
        message.delete()
        bot.send_message(message.chat.id, "/flee@blackwerewolfbot")

@BOT.on_message(Filters.command("pa", ".") & Filters.me)
def pingall(bot: BOT, message: Message):
    message.delete()
    bot.send_message(message.chat.id, "/pingall")
    sleep(600)
    bot.send_message(message.chat.id, "Pingall kann wieder verwendet werden!")

@BOT.on_message(Filters.command("pt", ".") & Filters.me)
def pingtime(bot: BOT, message: Message):
    message.delete()
    bot.send_message(message.chat.id, "/pingtime")
    #Moved to autopingtimecd.py
    #sleep(600)
    #bot.send_message(message.chat.id, "Pingtime kann wieder verwendet werden!")

@BOT.on_message(Filters.command("pl", ".") & Filters.me)
def players(bot: BOT, message: Message):
    message.delete()
    bot.send_message(message.chat.id, "/players@blackwerewolfbot")


#Admin Befehle

@BOT.on_message(Filters.command("kg", ".") & Filters.user(controllers))
def killgame(bot: BOT, message: Message):
        message.delete()
        bot.send_message(message.chat.id, "/killgame@blackwerewolfbot")

@BOT.on_message(Filters.command("fs", ".") & Filters.user(controllers))
def forcestart(bot: BOT, message: Message):
        message.delete()
        bot.send_message(message.chat.id, "/forcestart@blackwerewolfbot")

@BOT.on_message(Filters.command("kill", ".") & Filters.user(controllers))
def smiten(bot: BOT, message: Message):
    bot.send_message(
        chat_id=message.chat.id,
        text="/smite@blackwerewolfbot",
        reply_to_message_id=message.reply_to_message.message_id)
    message.delete()
