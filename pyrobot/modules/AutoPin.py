from pyrobot import BOT
from pyrogram import Filters, Message

#PinSilent
@BOT.on_message(Filters.regex("^#players: (\d+)") & Filters.chat(['Ethiowerewolf', '-1001280664204']) & ~Filters.edited)
def pin_on_start_Ethiowolf_Silent(bot: BOT,  message:Message):
    toPin = message.message_id
    bot.pin_chat_message(message.chat.id, toPin, disable_notification=True)

#PinWithNotification
@BOT.on_message(Filters.regex("^#players: (\d+)") & Filters.chat(['themightypack', 'lightwerewolf']) & ~Filters.edited)
def pin_on_start_Loud(bot: BOT,  message:Message):
    toPin = message.message_id
    bot.pin_chat_message(message.chat.id, toPin)
