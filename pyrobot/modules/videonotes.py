import os
import sqlite3
from time import sleep

from pyrogram import Filters, Message

from pyrobot import BOT, PYRO_DB

# DB_PATH = str(Path(__file__).parent.parent.parent / 'pyrobot.db')

# -- Constants -- #

SAVE_NOTE = "INSERT OR FAIL INTO video_notes VALUES ('{}', '{}')"
GET_NOTE = "SELECT file_id FROM video_notes WHERE name='{}'"
REMOVE_NOTE = "DELETE FROM video_notes WHERE EXISTS (VALUES (name='{}'))"
LIST_NOTES = "SELECT name FROM video_notes"

# -- Constants End -- #

# -- Helpers -- #


def ReplyCheck(message: Message):
    reply_id = None

    if message.reply_to_message:
        reply_id = message.reply_to_message.message_id

    elif not message.from_user.is_self:
        reply_id = message.message_id

    return reply_id

# -- Helpers End -- #


@BOT.on_message(Filters.command("notes", ".") & Filters.me)
def list_vids(bot: BOT, message: Message):
    db = sqlite3.connect(PYRO_DB)
    c = db.cursor()
    c.execute(LIST_NOTES)
    result = c.fetchall()
    res = [i[0] for i in result]
    notes = "**List of available Videnotes:**\n`.note [name]`\n"
    for note in sorted(res):
        notes += f"→ `{note}`\n"
    BOT.send_message("me", notes)
    message.edit("List of available Videonotes sent in Saved Mesages")
    sleep(2)
    message.delete()


@BOT.on_message(Filters.command("savenote", ".") & Filters.me)
def save_note(bot: BOT, message: Message):
    cmd = message.command
    try:
        cmd[1]
    except IndexError:
        message.edit("I need a name to save to...")
        sleep(2)
        message.delete()
        return

    note = BOT.send_video_note(
        chat_id='me',
        video_note=message.reply_to_message.download('./note.mp4'))
    note.delete()
    os.remove('./note.mp4')
    db = sqlite3.connect(PYRO_DB)
    c = db.cursor()
    try:
        c.execute(SAVE_NOTE.format(cmd[1], note.video_note.file_id))
    except sqlite3.IntegrityError:
        message.edit(f'Videonote "`{cmd[1]}`" already saved.')
        return
    except AttributeError:
        message.edit(f"The video needs an aspect:ratio of 1:1, otherwise it can't be a videonote.")
        sleep(3)
        message.delete()
        return
    db.commit()
    db.close()
    message.edit(f'Videnote saved as `{cmd[1]}`.')
    sleep(2)
    message.delete()


@BOT.on_message(Filters.command("rmnote", ".") & Filters.me)
def remove_note(bot: BOT, message: Message):
    cmd = message.command
    try:
        cmd[1]
    except IndexError:
        message.edit("I can't delete nothing.")
        sleep(2)
        message.delete()
        return
    db = sqlite3.connect(PYRO_DB)
    c = db.cursor()
    c.execute(GET_NOTE.format(cmd[1]))
    result = c.fetchone()
    if result:
        c.execute(REMOVE_NOTE.format(cmd[1]))
        db.commit()
        message.edit(f"Videnote `{cmd[1]}` deleted.")
    else:
        message.edit(f"Videonote `{cmd[1]}` didn't exist.")
    sleep(2)
    message.delete()


@BOT.on_message(Filters.command("note", ".") & Filters.me)
def send_note(bot: BOT, message: Message):
    cmd = message.command
    try:
        cmd[1]
    except IndexError:
        message.edit(f"I need a name to look for.")
        sleep(2)
        message.delete()
        return
    db = sqlite3.connect(PYRO_DB)
    c = db.cursor()
    c.execute(GET_NOTE.format(cmd[1]))
    result = c.fetchone()
    if result:
        BOT.send_video_note(
            chat_id=message.chat.id,
            video_note=result[0],
            reply_to_message_id=ReplyCheck(message))
    else:
        message.edit(f'Videonote `{cmd[1]}` not found.')
        sleep(2)
    message.delete()
    db.close()
