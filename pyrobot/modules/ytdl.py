from pyrobot import BOT
from pyrogram import Filters, Message
from pytube import YouTube

@BOT.on_message(Filters.me & Filters.command('dl', '/'))
def youtubedl(bot: BOT, message: Message):
    link = " ".join(message.command[1:])
    YouTube('link').streams.first().download()
    BOT.download_media(
        message=message.document,
        file_name='video.mp4')
