import os
import re

import cloudconvert
from pyrogram import Filters, Message, errors

from pyrobot import BOT, CC_API

# -- Constants -- #
CC_Convert = (
    r"""-i {INPUTFILE} -vf 'scale=if(gte(iw\,ih)\,min(1280\,iw)\,-2):if(lt"""
    r"""(iw\,ih)\,min(1280\,ih)\,-2)' -an -pix_fmt yuv420p {OUTPUTFILE}""")

ccapi = cloudconvert.Api(CC_API)


@BOT.on_message(Filters.command("conv", "!") & Filters.me)
def cc_gif(bot: BOT, message: Message):
    try:  # delete if file still exists
        os.remove("animation.mp4")
        os.remove("animation.1.mp4")
    except FileNotFoundError:
        pass

    try:
        conv_url = message.command[1]
    except IndexError:
        message.edit("No URL to convert")
        return
    conv_ext = re.findall(r"\w+$", conv_url)

    try:
        message.edit("`Converting . . .`")
        process = ccapi.convert({
            'inputformat': conv_ext[0],
            'outputformat': 'mp4',
            'input': 'download',
            'file': conv_url,
            'filename': f'animation.{conv_ext[0]}',
            'converteroptions': {
                'command': CC_Convert
            }
        })
        process.wait()
        message.edit("`Downloading . . .`")
        process.download()
    except cloudconvert.exceptions.APIError as e:
        message.edit(
            f"Error: {e}\n{conv_url}",
            disable_web_page_preview=True)
        return

    message.edit("`Uploading . . .`")

    try:
        BOT.send_animation(
            chat_id=message.chat.id,
            animation="animation.mp4")
    except errors.FileIdInvalid:
        BOT.send_animation(
            chat_id=message.chat.id,
            animation="animation.1.mp4")
    message.delete()
    try:
        os.remove("animation.mp4")
        os.remove("animation.1.mp4")
    except FileNotFoundError:
        pass
