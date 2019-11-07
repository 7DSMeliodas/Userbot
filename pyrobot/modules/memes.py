from time import sleep

import requests
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


@BOT.on_message(Filters.command(["🐶", "🐕", "🐩", "dog"], "") & Filters.me)
def send_dog(bot: BOT, message: Message):
    doggo = requests.get('https://random.dog/woof.json?filter=webm,mp4').json()
    BOT.send_photo(
        chat_id=message.chat.id,
        photo=doggo['url'],
        caption="doggo",
        reply_to_message_id=ReplyCheck(message))
    if message.from_user.is_self:
        message.delete()


@BOT.on_message(Filters.command("mock", ".") & Filters.me)
def mock_people(bot: BOT, message: Message):
    cmd = message.command

    if len(cmd) > 1:
        mock_text = " ".join(cmd[1:])
    elif message.reply_to_message and len(cmd) == 1:
        mock_text = message.reply_to_message.text
    elif not message.reply_to_message and len(cmd) == 1:
        message.edit("I need something to mock")
        sleep(2)
        message.delete()
        return
    try:
        mock_results = BOT.get_inline_bot_results(
            "stickerizerbot",
            "#7" + mock_text)
        BOT.send_inline_bot_result(
            chat_id=message.chat.id,
            query_id=mock_results.query_id,
            result_id=mock_results.results[0].id,
            reply_to_message_id=ReplyCheck(message),
            hide_via=True)
    except TimeoutError:
        message.edit("@StickerizerBot didn't respond in time.")
        sleep(2)
    message.delete()


@BOT.on_message(Filters.command("ggl", ".") & Filters.me)
def google_sticker(bot: BOT, message: Message):
    cmd = message.command

    if len(cmd) > 1:
        ggl_text = " ".join(cmd[1:])
    elif message.reply_to_message and len(cmd) == 1:
        ggl_text = message.reply_to_message.text
    elif not message.reply_to_message and len(cmd) == 1:
        message.edit("I need something to google")
        sleep(2)
        message.delete()
        return

    try:
        ggl_result = BOT.get_inline_bot_results(
            "stickerizerbot",
            "#12" + ggl_text)
        BOT.send_inline_bot_result(
            chat_id=message.chat.id,
            query_id=ggl_result.query_id,
            result_id=ggl_result.results[0].id,
            reply_to_message_id=ReplyCheck(message),
            hide_via=False)
    except TimeoutError:
        message.edit("@StickerizerBot didn't respond in time.")
        sleep(2)
    message.delete()
