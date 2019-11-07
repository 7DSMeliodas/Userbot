import os
from time import sleep

import gtts
from pyrogram import Filters, Message, errors

from pyrobot import BOT

# -- Helpers -- #

gtts_langs = gtts.lang.tts_langs()


def ReplyCheck(message: Message):
    reply_id = None

    if message.reply_to_message:
        reply_id = message.reply_to_message.message_id

    elif not message.from_user.is_self:
        reply_id = message.message_id

    return reply_id


# -- Helpers End -- #

@BOT.on_message(Filters.command("v", '.') & Filters.me)
def text_to_speech(bot: BOT, message: Message):
    if not len(message.command) > 1:
        message.edit("I need words to say...")
        sleep(2)
        message.delete()
        return

    if message.command[-1] not in gtts_langs:
        language = 'en'
        words_to_say = " ".join(message.command[1:])
    else:
        language = ''.join(message.command[-1])
        words_to_say = " ".join(message.command[1:-1])

    speech = gtts.gTTS(words_to_say, language)
    speech.save('text_to_speech.oog')
    try:
        BOT.send_voice(
            chat_id=message.chat.id,
            voice='text_to_speech.oog',
            reply_to_message_id=ReplyCheck(message))
    except errors.UnknownError as e:
        if e.x.error_message == 'CHAT_SEND_MEDIA_FORBIDDEN':
            message.edit("Voice Messages aren't allowed here.\nCopy sent to Saved Messages.")
        else:
            message.edit("Text-To-Speech couldn't be sent.\nCopy sent to Saved Messages.")
        BOT.send_message('me', ' '.join(message.command[1:]))
        BOT.send_voice('me', 'text_to_speech.oog')
        sleep(2)
    try:
        os.remove('text_to_speech.oog')
    except FileNotFoundError:
        pass
    message.delete()
