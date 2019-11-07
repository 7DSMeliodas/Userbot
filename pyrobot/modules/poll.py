from time import sleep

from pyrogram import Filters, Message

from pyrobot import BOT

from ..helpers import LogMessage

# -- Constants -- #

POLL_LOG = "Poll \"{0.poll.question}\" sent to \"[{0.chat.title}](t.me/c/{1}/{0.message_id})\"."

# -- Helpers -- #


def ReplyCheck(message: Message):
    reply_id = None

    if message.reply_to_message:
        reply_id = message.reply_to_message.message_id

    elif not message.from_user.is_self:
        reply_id = message.message_id

    return reply_id

# -- Helpers End -- #


@BOT.on_message(Filters.command("poll", ".") & Filters.me)
def make_poll(bot: BOT, message: Message):
    cmd = message.command
    if message.chat.type == 'private':
        message.edit("Polls are not supported in private chats")
        sleep(2)
        message.delete()
        return
    if len(cmd) == 1:
        message.edit("I need a question")
        sleep(2)
        message.delete()
    elif len(cmd) > 1:
        poll = message.text[6:].split('\n')
        if len(poll[1:]) < 2:
            message.edit("I need at least two answers")
        elif len(poll[1:]) > 10:
            message.edit("A poll can only have 10 answers")
        else:
            sent_poll = BOT.send_poll(
                chat_id=message.chat.id,
                question=poll[0],
                options=poll[1:],
                reply_to_message_id=ReplyCheck(message))
            message.edit("Poll created")
            LogMessage(
                POLL_LOG.format(
                    sent_poll,
                    str(sent_poll.chat.id).replace("-100", "")))
            message.delete()
