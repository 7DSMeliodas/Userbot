from pyrobot import BOT
from pyrogram import Filters, Message
from googletrans import Translator
from time import sleep

translator = Translator()


@BOT.on_message(Filters.command("tl", "."))#, group=1)
def translate(bot, message):
    if len(message.command) <= 1:
        m = message.reply("No language defined. Example: /tl en for english.")
        message.delete(m.message_id)
        sleep(3)
        m.delete()
    else:
        lang = ''.join(message.command[-1])
        replyid = message.reply_to_message.message_id
        original = message.reply_to_message.text
        detect = translator.detect(original)
        #print(detect)
        translated = translator.translate(original, src=detect.lang, dest=lang)
        message.reply_to_message.reply("The original message (" + detect.lang + ") is translated to " + lang + ".\nThe translated version is:\n \n" + translated.text)
        message.delete()
