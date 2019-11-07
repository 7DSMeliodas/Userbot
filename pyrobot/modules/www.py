from datetime import datetime

import speedtest
from pyrogram import Filters, Message
from pyrogram.api import functions

from pyrobot import BOT

from ..helpers import LogMessage

# -- Constants -- #

SpeedTest = (
    "Speedtest started at `{start}`\n\n"
    "Ping:\n{ping} ms\n\n"
    "Download:\n{download}\n\n"
    "Upload:\n{upload}\n\n"
    "ISP:\n__{isp}__")

NearestDC = (
    "Country: `{}`\n"
    "Nearest Datacenter: `{}`\n"
    "This Datacenter: `{}`")

# -- Constants End -- #

# -- Helpers -- #


def SpeedConvert(size):
    power = 2**10
    zero = 0
    units = {
        0: '',
        1: 'Kbit/s',
        2: 'Mbit/s',
        3: 'Gbit/s',
        4: 'Tbit/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"

# -- Helpers End -- #


@BOT.on_message(Filters.command("speed", ".") & Filters.me)
def speed_test(bot: BOT, message: Message):
    new_msg = message.edit(
        "`Running speed test . . .`")
    spd = speedtest.Speedtest()

    new_msg = message.edit(
        f"`{new_msg.text}`\n"
        "`Getting best server based on ping . . .`")
    spd.get_best_server()

    new_msg = message.edit(
        f"`{new_msg.text}`\n"
        "`Testing download speed . . .`")
    spd.download()

    new_msg = message.edit(
        f"`{new_msg.text}`\n"
        "`Testing upload speed . . .`")
    spd.upload()

    new_msg = new_msg.edit(
        f"`{new_msg.text}`\n"
        "`Getting results and preparing formatting . . .`")
    results = spd.results.dict()

    SpeedMsg = SpeedTest.format(
        start=results['timestamp'],
        ping=results['ping'],
        download=SpeedConvert(results['download']),
        upload=SpeedConvert(results['upload']),
        isp=results['client']['isp'])
    message.edit(SpeedMsg)
    LogMessage(SpeedMsg)


@BOT.on_message(Filters.command("dc", ".") & Filters.me)
def neardc(bot: BOT, message: Message):
    dc = BOT.send(
        functions.help.GetNearestDc())
    message.edit(
        NearestDC.format(
            dc.country,
            dc.nearest_dc,
            dc.this_dc))


@BOT.on_message(Filters.command("ping", ".") & Filters.me)
def pingme(bot: BOT, message: Message):
    start = datetime.now()
    message.edit('`Pong!`')
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    message.edit(f"**Pong!**\n`{ms} ms`")
