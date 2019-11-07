import sqlite3
from html import escape, unescape
from time import sleep

from pyrogram import Filters, Message

from pyrobot import BOT, PYRO_DB

from ..helpers import LogMessage

# -- Constants -- #

SET_WELCOME = """INSERT OR FAIL INTO welcome VALUES ('{}', "{}", "{}")"""
GET_WELCOME = "SELECT greet FROM welcome WHERE chat_id='{}'"
ALL_WELCOME = "SELECT chat_title, greet FROM welcome"
REMOVE_WELCOME = "DELETE FROM welcome WHERE chat_id='{}'"

# -- Constants End -- #

# -- Helpers -- #


def PrivateCheck(message: Message):
    if message.chat.type == 'private':
        message.edit("Welcome messages are not supported in Private Chats.")
        sleep(2)
        message.delete()
        return None
    return True

# -- Helpers End -- #


@BOT.on_message(Filters.command("setwelcome", ".") & Filters.me)
def set_welcome(bot: BOT, message: Message):
    if PrivateCheck(message):
        cmd = message.command
        if len(cmd) == 1:
            if not message.reply_to_message:
                message.edit("I can't set a welcome message without a message.")
            elif message.reply_to_message:
                welcome_text = message.reply_to_message.text
        elif len(cmd) > 1:
            welcome_text = message.text.markdown[12:]
        db = sqlite3.connect(PYRO_DB)
        c = db.cursor()
        try:
            c.execute(SET_WELCOME.format(message.chat.id, escape(
                welcome_text), escape(message.chat.title)))
            message.edit(
                "__Welcome message set:__\n\n" + welcome_text,
                disable_web_page_preview=True)
        except sqlite3.IntegrityError:
            c.execute(GET_WELCOME.format(message.chat.id))
            res = c.fetchone()
            c.execute(REMOVE_WELCOME.format(message.chat.id))
            c.execute(SET_WELCOME.format(message.chat.id, escape(
                welcome_text), escape(message.chat.title)))
            message.edit(
                "__Replaced old welcome message:__\n\n"
                + unescape(res[0])
                + "\n\n__with new welcome message:__\n\n"
                + welcome_text,
                disable_web_page_preview=True)
        db.commit()


@BOT.on_message(Filters.command("rmwelcome", ".") & Filters.me)
def remove_welcome(bot: BOT, message: Message):
    if PrivateCheck(message):
        db = sqlite3.connect(PYRO_DB)
        c = db.cursor()
        c.execute(GET_WELCOME.format(message.chat.id))
        res = c.fetchone()
        if res:
            c.execute(REMOVE_WELCOME.format(message.chat.id))
            db.commit()
            message.edit(
                "__Removed welcome message:__\n\n" + unescape(res[0]),
                disable_web_page_preview=True)
        else:
            message.edit("There was no welcome message.")
        sleep(3)
        message.delete()


@BOT.on_message(Filters.command("welcome", ".") & Filters.me)
def get_welcome(bot: BOT, message: Message):
    if PrivateCheck(message):
        db = sqlite3.connect(PYRO_DB)
        c = db.cursor()
        c.execute(GET_WELCOME.format(message.chat.id))
        res = c.fetchone()
        if res:
            message.edit(
                "__This chats welcome message:__\n\n" + unescape(res[0]),
                disable_web_page_preview=True)
        else:
            message.edit("__There is no welcome message for this chat.__")
        sleep(3)
        message.delete()


@BOT.on_message(Filters.command("welcome", "!") & Filters.me)
def all_welcome(bot: BOT, message: Message):
    db = sqlite3.connect(PYRO_DB)
    c = db.cursor()
    c.execute(ALL_WELCOME)
    res = c.fetchall()
    if res:
        welcome_messages = "**All Welcome Messages:**\n"
        for welcome in res:
            welcome_messages += f"\n👉 **{unescape(welcome[0])}**\n{unescape(welcome[1])}\n"
        BOT.send_message('me', welcome_messages, disable_web_page_preview=True)
        message.edit("Welcome messages sent in Saved Messages.")
        sleep(2)
        message.delete()


# Actually greet new people
@BOT.on_message(Filters.new_chat_members)
def greet_new_users(bot: BOT, message: Message):
    new = message.new_chat_members
    db = sqlite3.connect(PYRO_DB)
    c = db.cursor()
    c.execute(GET_WELCOME.format(message.chat.id))
    res = c.fetchone()
    if res:
        welcome_text = res[0].replace(
            "{name}",
            ", ".join("{}".format(
                usr.first_name) for usr in new)
        ).replace(
            "{namelink}",
            ", ".join("[{}](tg://user?id={})".format(
                usr.first_name, usr.id) for usr in new)
        ).replace(
            "{title}",
            f"{message.chat.title}"
        )
        greet = message.reply(
            unescape(welcome_text),
            disable_web_page_preview=True,
            disable_notification=True)
        LogMessage(
            "Greeted new users in \"[{}](t.me/c/{}/{})\":\n{}".format(
                message.chat.title,
                str(greet.chat.id).replace("-100", ""),
                str(greet.message_id),
                ", ".join(usr.first_name for usr in new)))
