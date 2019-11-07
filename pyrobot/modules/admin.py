from time import sleep, time

from pyrogram import Filters, Message
from pyrogram.errors import FloodWait, UserAdminInvalid

from pyrobot import BOT

from ..helpers import LogMessage
from ..interval import IntervalHelper

# -- Constants -- #

admin = 'administrator'
creator = 'creator'
ranks = [admin, creator]

BANNED = "{0.reply_to_message.from_user.first_name} has been banned."
BANNED_TIME = (
    "{0.reply_to_message.from_user.first_name} has been banned for {1}.")
BANNED_LOG = (
    "[{0.reply_to_message.from_user.first_name}](tg://user?id={0.reply_to_message.from_user.id}) "
    "has been banned from \"[{0.chat.title}](t.me/c/{1}/{0.message_id})\".")

UNBANNED = "{0.message.reply_to_message.from_user.first_name} has been unbanned"
UNBANNED_LOG = (
    "[{0.reply_to_message.from_user.first_name}](tg://user?id="
    "{0.reply_to_message.from_user.id}) has been unbanned in \"["
    "{0.chat.title}](t.me/c/{1}/{0.message_id})\".")

MUTED = "{0.reply_to_message.from_user.first_name} has been muted."
MUTED_TIME = "{0.reply_to_message.from_user.first_name} has been muted for {1}."
MUTED_LOG = (
    "[{0.reply_to_message.from_user.first_name}](tg://user?id={0.reply_to_message.from_user.id}) "
    "has been muted in \"[{0.chat.title}](t.me/c/{1}/{0.message_id})\".")

UNMUTED = "{0.reply_to_message.from_user.first_name} has been unmuted."
UNMUTED_LOG = (
    "[{0.reply_to_message.from_user.first_name}](tg://user?id={0.reply_to_message.from_user.id}) "
    "has been unmuted in \"[{0.chat.title}](t.me/c/{1}/{0.message_id})\".")

KICKED = "{0.reply_to_message.from_user.first_name} has been kicked."
KICKED_LOG = (
    "[{0.reply_to_message.from_user.first_name}](tg://user?id={0.reply_to_message.from_user.id}) "
    "has been kicked from \"[{0.chat.title}](t.me/c/{1}/{0.message_id})\".")

# -- Constants End -- #

# -- Helpers -- #


def ReplyCheck(message):
    if not message.reply_to_message:
        message.edit(f"`{message.command[0]}` needs to be a reply.")
        sleep(2)
        message.delete()
    elif message.reply_to_message.from_user.is_self:
        message.edit(f"I can't {message.command[0]} myself.")
        sleep(2)
        message.delete()
    else:
        return True


def AdminCheck(message):
    SELF = BOT.get_chat_member(
        chat_id=message.chat.id,
        user_id=message.from_user.id)

    if SELF.status not in ranks:
        message.edit("__I'm not Admin!__")
        sleep(2)
        message.delete()

    else:
        if SELF.status is not admin:
            return True
        elif SELF.can_restrict_members:
            return True
        else:
            message.edit("__No permissions to restrict Members__")


def RestrictFailed(message):
    message.edit(f"I can't {message.command[0]} this user.")
    sleep(2)
    message.delete()


def Timer(message: Message):
    if len(message.command) > 1:
        secs = IntervalHelper(message.command[1])
        return int(str(time()).split(".")[0]) + secs.to_secs()[0]
    else:
        return 0


def TimerString(message: Message):
    secs = IntervalHelper(message.command[1])
    return f"{secs.to_secs()[1]} {secs.to_secs()[2]}"

# -- Helpers End -- #


@BOT.on_message(Filters.command("ban", "?") & Filters.me)
def ban_hammer(bot: BOT, message: Message):
    if ReplyCheck(message) is True and AdminCheck(message) is True:
        try:
            BOT.kick_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id,
                until_date=Timer(message))
            if len(message.command) > 1:
                message.edit(BANNED_TIME.format(
                    message,
                    TimerString(message)))
            else:
                message.edit(BANNED.format(message))
            LogMessage(BANNED_LOG.format(
                message,
                str(message.chat.id).replace("-100", "")))
        except UserAdminInvalid:
            RestrictFailed(message)


@BOT.on_message(Filters.command("unban", "?") & Filters.me)
def unban(bot: BOT, message: Message):
    if ReplyCheck(message) is True and AdminCheck(message) is True:
        try:
            BOT.unban_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id)
            message.edit(UNBANNED.format(message))
            LogMessage(UNBANNED_LOG.format(
                message,
                str(message.chat.id).replace("-100", "")))
        except UserAdminInvalid:
            message.edit("I can't unban this user")


@BOT.on_message(Filters.command("mute", "?") & Filters.me)
def mute_hammer(bot: BOT, message: Message):
    if ReplyCheck(message) is True and AdminCheck(message) is True:
        try:
            BOT.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id,
                until_date=Timer(message),
                can_send_messages=False,)
            if len(message.command) > 1:
                message.edit(MUTED_TIME.format(
                    message,
                    TimerString(message)))
            else:
                message.edit(MUTED.format(message))
            LogMessage(MUTED_LOG.format(
                message,
                str(message.chat.id).replace("-100", "")))
        except UserAdminInvalid:
            RestrictFailed(message)


@BOT.on_message(Filters.command("unmute", "?") & Filters.me)
def unmute(bot: BOT, message: Message):
    if ReplyCheck(message) is True and AdminCheck(message) is True:
        try:
            BOT.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id,
                until_date=0,
                can_send_messages=True,
                can_send_media_messages=True,
                can_send_other_messages=True,
                can_add_web_page_previews=True,
                can_send_polls=True,
                can_change_info=True,
                can_invite_users=True,
                can_pin_messages=True)
            message.edit(UNMUTED.format(message))
            LogMessage(UNMUTED_LOG.format(
                message,
                str(message.chat.id).replace("-100", "")))
        except UserAdminInvalid:
            RestrictFailed(message)


@BOT.on_message(Filters.command("kick", "?") & Filters.me)
def kick_user(bot: BOT, message: Message):
    if ReplyCheck(message) is True and AdminCheck(message) is True:
        try:
            BOT.kick_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id,
                until_date=0)
            BOT.unban_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id)
            message.edit(KICKED.format(message))
            LogMessage(KICKED_LOG.format(
                message,
                str(message.chat.id).replace("-100", "")))
        except UserAdminInvalid:
            RestrictFailed(message)


@BOT.on_message(Filters.command("cclean", "!") & Filters.me)
def clean_deleted(bot: BOT, message: Message):
    if AdminCheck(message) is True:
        message.edit("`Iterating through memberlist...`")
        all_members = BOT.iter_chat_members(message.chat.id)
        to_remove = []
        removed = []

        for member in all_members:
            if member.user.is_deleted:
                to_remove.append(member.user.id)

        message.edit(f"`{len(to_remove)} deleted accounts found.`")

        for usr in to_remove:
            try:
                BOT.kick_chat_member(
                    chat_id=message.chat.id,
                    user_id=usr)
                removed.append(usr)
            except UserAdminInvalid:
                pass
            except FloodWait as e:
                sleep(e.x)

        message.edit(f"Removed {len(removed)} deleted accounts.")
