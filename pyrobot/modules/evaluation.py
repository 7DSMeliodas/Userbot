import os
from time import sleep

from pyrogram import Filters, Message
from pyrogram.api import functions, types

from pyrobot import BOT

from ..helpers import LogMessage

# -- Constants -- #

RUNNING = "**Expression:**\n```{}```\n\n**Running...**"
ERROR = "**Expression:**\n```{}```\n\n**Error:**\n```{}```"
SUCCESS = "**Expression:**\n```{}```\n\n**Success** | `None`"
RESULT = "**Expression:**\n```{}```\n\n**Result:**\n```{}```"
RESULT_FILE = "**Expression:**\n```{}```\n\n**Result:**\nView `output.txt` below ⤵"

ERROR_LOG = (
    "**Evaluation Query**\n"
    "```{}```\n"
    "erred in chat \"[{}](t.me/c/{}/{})\" with error\n"
    "```{}```")

SUCCESS_LOG = (
    "Evaluation Query\n"
    "```{}```\n"
    "succeeded in \"[{}](t.me/c/{}/{})\"")

RESULT_LOG = (
    "Evaluation Query\n"
    "```{}```\n"
    "executed in chat \"[{}](t.me/c/{}/{})\".")

# -- Constants End -- #
# -- Helpers -- #


def ReplyCheck(message: Message):
    reply_id = None

    if message.reply_to_message:
        reply_id = message.reply_to_message.message_id

    elif not message.from_user.is_self:
        reply_id = message.message_id

    return reply_id


def SendLong(expr: Message, cmdstr: str, result):
    with open("output.txt", 'w+', encoding='utf8') as f:
        f.write(str(result))
    BOT.send_document(
        chat_id=expr.chat.id,
        document="output.txt",
        caption="`Output too long, sent as file.`",
        reply_to_message_id=expr.message_id)
    os.remove("output.txt")

# -- Helpers End -- #


@BOT.on_message(Filters.command("eval", ".") & Filters.me)
def evaluation(bot: BOT, message: Message):
    try:
        cmdstr = " ".join(message.command[1:])
    except IndexError:
        message.edit("__I can't evaluate nothing...__")
        sleep(2)
        message.delete()
        return

    if cmdstr:
        expr = message.reply(RUNNING.format(cmdstr))

        try:
            result = eval(cmdstr)
        except Exception as err:
            expr.edit(ERROR.format(cmdstr, err))
            LogMessage(ERROR_LOG.format(
                cmdstr,
                message.chat.title or message.chat.first_name,
                str(message.chat.id).replace("-100", ""),
                str(expr.message_id),
                err))

        else:

            if result is None:
                expr.edit(SUCCESS.format(cmdstr))
                LogMessage(SUCCESS_LOG.format(
                    cmdstr,
                    message.chat.title or message.chat.first_name,
                    str(message.chat.id).replace("-100", ""),
                    str(expr.message_id)))

            elif len(RESULT.format(cmdstr, result)) > 4096:
                expr.edit(RESULT_FILE.format(cmdstr))
                BOT.send_chat_action(message.chat.id, "upload_document")
                SendLong(expr, cmdstr, result)

            else:
                expr.edit(RESULT.format(cmdstr, result))

            LogMessage(RESULT_LOG.format(
                cmdstr,
                message.chat.title or message.chat.first_name,
                str(message.chat.id).replace("-100", ""),
                str(expr.message_id)))


@BOT.on_message(Filters.command("exec", ".") & Filters.me)
def execution(bot: BOT, message: Message):
    try:
        cmdstr = message.text[6:]
    except IndexError:
        message.edit("__I can't execute nothing...__")
        sleep(2)
        message.delete()
        return

    if cmdstr:
        expr = message.reply(RUNNING.format(cmdstr))

        try:
            exec(
                'def __ex(bot, message): '
                + ''.join(
                    '\n '
                    + l for l in cmdstr.split('\n')))
            result = locals()['__ex'](bot, message)

        except Exception as err:
            expr.edit(ERROR.format(cmdstr, err))
            LogMessage(ERROR_LOG.format(
                cmdstr,
                message.chat.title or message.chat.first_name,
                str(message.chat.id).replace("-100", ""),
                str(expr.message_id),
                err))

        else:
            if result:
                expr.edit(RESULT.format(cmdstr, result))
                LogMessage(RESULT.format(
                    cmdstr,
                    message.chat.title or message.chat.first_name,
                    str(message.chat.id).replace("-100", ""),
                    str(expr.message_id)))
            else:
                expr.edit(SUCCESS.format(cmdstr))
                LogMessage(SUCCESS_LOG.format(
                    cmdstr,
                    message.chat.title or message.chat.first_name,
                    str(message.chat.id).replace("-100", ""),
                    str(expr.message_id)))
