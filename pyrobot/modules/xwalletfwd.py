from pyrobot import BOT
from pyrogram import Filters, Message
from googletrans import Translator

translator = Translator()

#Add source group(s) here
#bots = ['combotnews']

#Add Group(s) to forward
#groups = [-1001304519364]


@BOT.on_message(Filters.text & ~Filters.edited & Filters.chat('pundixoffical'), group=1)
def forward_from_bots(bot, message):
    orginal = message.text
    translated = translator.translate(orginal, src='en', dest='de')
    bot.send_message(-1001309961369, "[Diese Nachricht ist aus dem Combot News Channel weitergeleitet und übersetzt.]\n"+translated.text)