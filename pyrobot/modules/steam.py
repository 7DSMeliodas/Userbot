from time import sleep

import requests
from pyrogram import Filters, Message

from pyrobot import ACCGEN_API, BOT

# -- Constants -- #

if ACCGEN_API:
    API = "https://accgen.cathook.club/api/v1/account/" + ACCGEN_API

ACC_MSG = (
    "╔═════\n"
    "║ **Steam Account**\n"
    "╠═════\n"
    "║ Login\n"
    "║ `{login}`\n"
    "╠═════\n"
    "║ Password\n"
    "║ `{password}`\n"
    "╠═════\n"
    "║ SteamID\n"
    "║ `{steamid}`\n"
    "╠═════\n"
    "║ URL\n"
    "║ steam.pm/{steamid}\n"
    "╚═════")

# -- Constants End -- #


@BOT.on_message(Filters.command("acc", "?") & Filters.me)
def steam_accgen(bot: BOT, message: Message):
    if ACCGEN_API is None or "":
        message.edit("You need to set an API Key.\n"
                     "Get one from @sag_stats_bot")
        sleep(3)
        message.delete()
        return
    acc = requests.get(API)
    if 'error' in acc.json():
        message.edit(f"Notice from the API:\n`{acc.json()['error']}`")
        sleep(5)
        message.delete()
    else:
        try:
            acc.raise_for_status()
            acc.json()
        except Exception as e:
            message.edit(f"`{e}`".replace(ACCGEN_API, "<key>"))
            sleep(5)
            message.delete()
            return

        message.edit(
            ACC_MSG.format(
                login=acc['login'],
                password=acc['password'],
                steamid=acc['steamid']),
            disable_web_page_preview=True)
