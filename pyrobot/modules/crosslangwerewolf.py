from pyrobot import BOT
from pyrogram import Filters, Message
from googletrans import Translator

translator = Translator()

#Add source group(s) here
bots = ['beowc']

#Add Group(s) to forward
groups = ['beowc']


@BOT.on_message(Filters.text & ~Filters.edited & Filters.chat('nnono'), group=1)
def crosstranslation(bot, message):
    original = message.text
    language = translator.detect(original)
    if language.lang == 'de':
        translated = translator.translate(original, src='de', dest='en')
        message.reply("This is the translated version: \n" + translated.text)
    elif language.lang == 'en':
        translated = translator.translate(original, src='en', dest='de')
        message.reply("Dies ist die Übersetzung: \n" + translated.text)
    else:
        message.reply("Diese Sprache (" + language.lang + ") wird aktuell nicht unterstützt.\nThis language (" + language.lang + ") isn't supported yet")
