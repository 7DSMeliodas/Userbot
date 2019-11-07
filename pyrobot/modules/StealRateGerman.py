# Imports
from pyrobot import BOT
from pyrogram import Filters, Message

# Get Stealrate
@BOT.on_message(Filters.command("steal", "#") & Filters.chat('lightwerewolf'))
def send_ot_link(bot: BOT, message: Message):
    bot.send_message(message.chat.id, "**Dieb-Stealrate:**\n\n100% Chance:\nWolfsmensch\nDorfbewohner\nUnglücksrabe\n\n75% Chance:\nMonarch\nAlchemist\nVerfluchter\nFreimaurer\nBetrunkener\nBürgermeister\nSchütze\nBeobachter\nVerräter\nAmor\nPrinz\nNarr\n\n50% Chance:\nSchutzengel\nKultist\nSchmied\nSandmann\nWerwolf\nZauberer\nLykan\Alibiwolf\nMärtyrer\nMagier\nEule\nDorfältester\nDetektiv\nSeherlehrling\nHure\nKultbeobachter\nPazifist\nOrakle\nLucifer\nWetterbendiger\nBetawolf\nPyromane\n\n25% Chance:\nKultjäger\nAlphawolf\nSerienmörder\nMarionettenmeister\n\n0% Chance:\nDoppelgänger\nLeichenschänder")
