import os
import re
from time import sleep

from pyrogram import Filters, Message
from saucenao import SauceNao

from pyrobot import BOT, SAUCE_API

saucenao = SauceNao(
    directory="./downloads/",
    api_key=SAUCE_API,
    output_type=SauceNao.API_JSON_TYPE)


@BOT.on_message(Filters.command("sauce", "!") & Filters.me)
def getsauce(bot: BOT, message: Message):
    if not message.reply_to_message:
        message.edit("`!sauce` needs to be a reply")
        sleep(2)
        message.delete()
        return
    get_sauce = message.reply_to_message.download()

    results = saucenao.check_file(get_sauce)
    if results:
        msg = ""
        msg += "**Possible Matches:**\n" + msg
        for result in results:
            url = ", ".join(result["data"]["ext_urls"])
            url = re.sub(r"^(https?://)?(www.)?", "", url)
            msg += "{}\n".format(url)
        message.edit(msg, disable_web_page_preview=True)

    else:
        message.edit("No matches.")
        sleep(3)
        message.delete()

    os.remove(get_sauce)
