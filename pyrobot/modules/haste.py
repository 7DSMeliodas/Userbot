import requests

from pyrobot import BOT
from pyrogram import Client, Filters

BASE = "https://haste.thevillage.chat"


@BOT.on_message(Filters.command("haste", ".") & Filters.reply & ~Filters.chat('-1001098636923'))
def haste(client, message):
    reply = message.reply_to_message

    if reply.text is None:
        return

    message.delete()

    result = requests.post(
        "{}/documents".format(BASE),
        data=reply.text.encode("UTF-8")
    ).json()

    message.reply(
        "{}/{}.py".format(BASE, result["key"]),
        reply_to_message_id=reply.message_id
    )
