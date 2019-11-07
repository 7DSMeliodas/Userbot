from pyrogram import Filters, Message

from pyrobot import BOT

# -- Helpers -- #


def GetOwnMessages(message):
    all_msgs = BOT.get_history(
        chat_id=message.chat.id)

    to_delete = []
    for msg in all_msgs:
        if (
            msg.message_id
            >= (
                message.reply_to_message.message_id
                if message.reply_to_message
                else 0
            )
        ) and message.from_user.is_self:
            to_delete.append(msg.message_id)

    return to_delete

# -- Helpers End -- #


@BOT.on_message(Filters.command("purgeall", "?") & Filters.me)
def purge_all(bot: BOT, message: Message):

    # If command argument contains an Integer
    if len(message.command) > 1 and message.command[1].isdigit():
        n = int(message.command[1])

        if message.reply_to_message:
            all_msg = BOT.get_history(
                chat_id=message.chat.id,
                limit=n,
                offset_id=message.reply_to_message.message_id,
                reverse=True)

        else:
            all_msg = BOT.get_history(
                chat_id=message.chat.id,
                limit=n + 1)
    # Otherwise do this instead
    else:
        if not message.reply_to_message:
            return

        all_msg = BOT.get_history(
            chat_id=message.chat.id,
            offset_id=message.reply_to_message.message_id)

    # finally delete
    BOT.delete_messages(
        chat_id=message.chat.id,
        message_ids=[x.message_id for x in all_msg.messages])


@BOT.on_message(Filters.command("purgeme", "?") & Filters.me)
def purge_me(bot: BOT, message: Message):

    # If command argument contains an Integer
    if len(message.command) > 1 and message.command[1].isdigit():
        n = int(message.command[1])

        if message.reply_to_message:
            all_msg = BOT.get_history(
                chat_id=message.chat.id,
                limit=n,
                offset_id=message.reply_to_message.message_id,
                reverse=True)

        else:
            all_msg = BOT.get_history(
                chat_id=message.chat.id,
                limit=n + 1)
    # Otherwise do this instead
    else:
        if not message.reply_to_message:
            return

        all_msg = BOT.get_history(
            chat_id=message.chat.id,
            offset_id=message.reply_to_message.message_id)
    # Check if messages are from self
    to_delete = []
    for msg in all_msg.messages:
        if msg.from_user.is_self:
            to_delete.append(msg.message_id)

    # finally delete
    BOT.delete_messages(
        chat_id=message.chat.id,
        message_ids=to_delete)
