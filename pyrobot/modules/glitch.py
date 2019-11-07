from shutil import rmtree
from time import sleep

import glitchart
from pyrogram import Filters, Message

from pyrobot import BOT

# -- Helpers -- #


def ReplyCheck(message: Message):
    reply_id = None

    if message.reply_to_message:
        reply_id = message.reply_to_message.message_id

    elif not message.from_user.is_self:
        reply_id = message.message_id

    return reply_id

# -- Helpers End -- #


# -- Constants -- #

# -- Constants End --#


@BOT.on_message(Filters.command('glitch', '.') & Filters.me)
def glitch_image(bot: BOT, message: Message):
    if not message.reply_to_message:
        message.edit("`.glitch` needs to be a reply.")
        sleep(2)

    elif message.reply_to_message:
        try:
            glitch_amount = int(message.command[1])
        except (IndexError, ValueError):
            glitch_amount = 1

        glitch_this = message.reply_to_message.download()
        glitch_ext = glitch_this.split(".")[-1].lower()

        if glitch_ext in ('jpg', 'jpeg'):
            for _ in range(glitch_amount):
                glitched = glitchart.jpeg(
                    photo=glitch_this,
                    inplace=True)
            bot.send_photo(
                chat_id=message.chat.id,
                photo=glitched,
                caption=f"{glitch_amount} iterations" if glitch_amount > 1 else "",
                reply_to_message_id=ReplyCheck(message))

    message.delete()
    rmtree('downloads')
