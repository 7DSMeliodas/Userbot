from pyrogram import Filters, Message

from pyrobot import BOT

# -- Constants -- #

ALIVE = "`I'm alive, Master :3`"
HELP = ("Elaborate help available on Gitea.\n"
        "s.neht.xyz/PyroBotHelp")
REPO = ("Userbot is available on Gitea:\n"
        "s.neht.xyz/PyroBot")

# -- Constants End -- #


@BOT.on_message(Filters.command("alive", ".") & Filters.me)
def _alive(bot: BOT, message: Message):
    message.edit(ALIVE)


@BOT.on_message(Filters.command("help", ".") & Filters.me)
def _help(bot: BOT, message: Message):
    message.edit(HELP)


@BOT.on_message(Filters.command("repo", ".") & Filters.me)
def _repo(bot: BOT, message: Message):
    message.edit(REPO)
