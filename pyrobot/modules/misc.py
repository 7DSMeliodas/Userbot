from datetime import datetime

from pyrogram import Filters, Message

from pyrobot import BOT, START_TIME

# -- Constants -- #

UPTIME = "Current Uptime\n{}"

# -- Constants End -- #

# Edit the sent message to display the current uptime.
@BOT.on_message(Filters.command(["up", "uptime"], ".") & Filters.me)
def uptime(bot: BOT, message: Message):
    now = datetime.now()
    uptime = now - START_TIME
    message.edit(UPTIME.format(str(uptime).split('.')[0]))
