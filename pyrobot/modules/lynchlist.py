from pyrobot import BOT
from pyrogram import Filters, Message


#Add Wolfbot(s) here
bots = [618096097, 198626752]

#Add Group to forward bot messages
group = -376143735


cond = None
@BOT.on_message(Filters.chat(bots) & Filters.inline_keyboard)
def reply_to_buttons(client, message):
 if message.reply_markup.inline_keyboard[0][0].text == 'Yes' or message.reply_markup.inline_keyboard[0][0].text == 'Ja':
  client.send_message(group, 'You got to choose Yes or No. reply 1 for yes or 2 for no')
