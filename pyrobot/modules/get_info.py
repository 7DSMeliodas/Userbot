from time import sleep, time

from pyrogram import Filters, Message

from pyrobot import BOT

from ..helpers import LogMessage

# -- Constants -- #

ADMINTITLE = "**Admins in \"{}\"**\n\n"
ADMINCREATOR = (
    '╔ **Creator**\n'
    '╚ `{} `[{}](tg://user?id={})\n\n')
ADMINLISTLASTBOT = '╚ `{} `[{}](tg://user?id={}) `ᴮᴼᵀ`\n'
ADMINLISTLAST = '╚ `{} `[{}](tg://user?id={})\n'
ADMINLISTBOT = '╠ `{} `[{}](tg://user?id={}) `ᴮᴼᵀ`\n'
ADMINLIST = '╠ `{} `[{}](tg://user?id={})\n'

MEMBER_INFO = (
    "╔═════════\n"
    "╠ **{}**\n"
    "╠ Member Count\n"
    "╠═════════\n"
    "╠ Total: `{}`\n"
    "╠═════════\n"
    "╠ Admins: `{}`\n"
    "╠ Members: `{}`\n"
    "╠ Bots: `{}`\n"
    "╠═════════\n"
    "╠ Deleted Accounts: `{}`\n"
    "╚═════════")

CHAT_INFO = (
    "╔═════════\n"
    "║ **Overview Chatlist**\n"
    "║ Total Chats: {}\n"
    "╠═════════\n"
    "║ Private Chats: {}\n"
    "║ Bots: {}\n"
    "║ Groups: {}\n"
    "║ Supergroups: {}\n"
    "║ Channels: {}\n"
    "╠═════════\n"
    "║ Time elapsed: {} seconds\n"
    "╚═════════")

UNREAD_INFO = (
    "╔═════════\n"
    "║ **Unread Messages**\n"
    "║ Total: `{total_msg}` in {total_chats} Chats\n"
    "╠═════════\n"
    "║ Messages from\n"
    "║ `{msg_private}` msg - {chat_private} Users\n"
    "║ `{msg_bots}` msg - {chat_bots} Bots\n"
    "║ `{msg_groups}` msg - {chat_groups} Groups\n"
    "║ `{msg_super}` msg - {chat_super} Supergroups\n"
    "║ `{msg_channel}` msg - {chat_channel} Channels\n"
    "╚═════════")

# -- Constants End -- #


@BOT.on_message(Filters.command("admins", "!") & Filters.me)
def get_admins(bot: BOT, message: Message):
    if message.chat.type == 'private':
        message.edit("There are no admins in private chats...")
        sleep(2)
        message.delete()

    else:
        all_admins = BOT.iter_chat_members(
            chat_id=message.chat.id,
            filter='administrators')
        creator = None
        admins = []

        for admin in all_admins:
            if admin.status == 'creator':
                creator = admin
            elif admin.status == 'administrator':
                admins.append(admin)
        sorted_admins = sorted(admins, key=lambda usid: usid.user.id)

        AdminList = ADMINTITLE.format(message.chat.title)

        if creator:
            AdminList += ADMINCREATOR.format(
                str(creator.user.id).rjust(10),
                creator.user.first_name,
                creator.user.id)

        AdminList += "╔ **Admins**\n"
        for admin in sorted_admins:
            if admin is sorted_admins[-1]:
                if admin.user.is_bot:
                    AdminList += ADMINLISTLASTBOT.format(
                        str(admin.user.id).rjust(10),
                        admin.user.first_name,
                        admin.user.id)
                else:
                    AdminList += ADMINLISTLAST.format(
                        str(admin.user.id).rjust(10),
                        admin.user.first_name,
                        admin.user.id)
            else:
                if admin.user.is_bot:
                    AdminList += ADMINLISTBOT.format(
                        str(admin.user.id).rjust(10),
                        admin.user.first_name,
                        admin.user.id)
                else:
                    AdminList += ADMINLIST.format(
                        str(admin.user.id).rjust(10),
                        admin.user.first_name,
                        admin.user.id)

        message.edit(AdminList)
        LogMessage(AdminList)


@BOT.on_message(Filters.command("members", "!") & Filters.me)
def get_members(bot: BOT, message: Message):
    if message.chat.type == 'private':
        message.delete()

    else:
        total = 0
        admins = 0
        members = 0
        bots = 0
        deleted = 0

        for member in BOT.iter_chat_members(message.chat.id):
            total += 1
            if member.user.is_bot:
                bots += 1
            elif member.user.is_deleted:
                deleted += 1
            elif member.status in ['creator', 'administrator']:
                admins += 1
            elif not member.user.is_deleted and not member.user.is_bot:
                members += 1

        member_count_text = MEMBER_INFO.format(
            message.chat.title,
            total,
            admins,
            members,
            bots,
            deleted
        )

        message.edit(member_count_text)
        LogMessage(member_count_text)


@BOT.on_message(Filters.command("id", ".") & Filters.me)
def get_file(bot: BOT, message: Message):
    file_id = None

    if message.reply_to_message:
        rep = message.reply_to_message
        if rep.audio:
            file_id = rep.audio.file_id
        elif rep.document:
            file_id = rep.document.file_id
        elif rep.photo:
            file_id = rep.photo.sizes[-1].file_id
        elif rep.sticker:
            file_id = rep.sticker.file_id
        elif rep.video:
            file_id = rep.video.file_id
        elif rep.animation:
            file_id = rep.animation.file_id
        elif rep.voice:
            file_id = rep.voice.file_id
        elif rep.video_note:
            file_id = rep.video_note.file_id
        elif rep.contact:
            file_id = rep.contact.file_id
        elif rep.location:
            file_id = rep.location.file_id
        elif rep.venue:
            file_id = rep.venue.file_id

    if not file_id:
        message.edit("This chat's ID:\n`{}`".format(message.chat.id))
    else:
        message.edit("File_ID:\n`{}`".format(file_id))


@BOT.on_message(Filters.command("chats", "!") & Filters.me)
def get_chats(bot: BOT, message: Message):
    total = 0
    private = 0
    channel = 0
    group = 0
    supergroup = 0
    bots = 0
    private_bots = []

    start = int(time())
    message.edit("Getting Chatlist...")
    for dialog in BOT.iter_dialogs():
        total += 1
        if dialog.chat.type == 'private':
            private_bots.append(dialog.chat.id)  # Save for later parsing.
        elif dialog.chat.type == 'channel':
            channel += 1
        elif dialog.chat.type == 'group':
            group += 1
        elif dialog.chat.type == 'supergroup':
            supergroup += 1

    message.edit("Checking for bots...")
    chunk_size = 200
    for i in range(0, len(private_bots), chunk_size):
        for priv in BOT.get_users(private_bots[i:i + chunk_size]):
            if priv.is_bot:
                bots += 1
            else:
                private += 1

    message.edit(CHAT_INFO.format(
        total,
        private,
        bots,
        group,
        supergroup,
        channel,
        int(time()) - start))


@BOT.on_message(Filters.command("unread", "!") & Filters.me)
def get_unreads(bot: BOT, message: Message):
    total_messages_unread = 0
    total_chats_unread = 0
    unread_msg_priv = 0
    unread_chat_priv = 0
    unread_msg_bot = 0
    unread_chat_bot = 0
    unread_msg_group = 0
    unread_chat_group = 0
    unread_msg_super = 0
    unread_chat_super = 0
    unread_msg_channel = 0
    unread_chat_channel = 0
    # A fuckton of variables (:
    chunk_size = 200
    could_be_bot = []

    message.edit("Getting dialogs...")
    all_dialogs = BOT.iter_dialogs()
    message.edit("Formatting...")
    for dialog in all_dialogs:
        if dialog.unread_messages_count:
            total_messages_unread += dialog.unread_messages_count
            if dialog.chat.type == 'private':
                could_be_bot.append(dialog)
                total_chats_unread += 1
            elif dialog.chat.type == 'group':
                unread_msg_group += dialog.unread_messages_count
                unread_chat_group += 1
                total_chats_unread += 1
            elif dialog.chat.type == 'supergroup':
                unread_msg_super += dialog.unread_messages_count
                unread_chat_super += 1
                total_chats_unread += 1
            elif dialog.chat.type == 'channel':
                unread_msg_channel += dialog.unread_messages_count
                unread_chat_channel += 1
                total_chats_unread += 1

    for i in range(0, len(could_be_bot), chunk_size):
        for priv in BOT.get_users([x.chat.id for x in could_be_bot[i:i + chunk_size]]):
            if priv.is_bot:
                unread_msg_bot += could_be_bot[i].unread_messages_count
                unread_chat_bot += 1
            elif not priv.is_bot:
                unread_msg_priv += could_be_bot[i].unread_messages_count
                unread_chat_priv += 1

    message.edit(UNREAD_INFO.format(
        total_msg=total_messages_unread,
        total_chats=total_chats_unread,
        msg_private=str(unread_msg_priv).rjust(6, " "),
        chat_private=unread_chat_priv,
        msg_bots=str(unread_msg_bot).rjust(6, " "),
        chat_bots=unread_chat_bot,
        msg_groups=str(unread_msg_group).rjust(6, " "),
        chat_groups=unread_chat_group,
        msg_super=str(unread_msg_super).rjust(6, " "),
        chat_super=unread_chat_super,
        msg_channel=str(unread_msg_channel).rjust(6, " "),
        chat_channel=unread_chat_channel))
