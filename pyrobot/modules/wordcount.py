from pyrogram import Filters, Message

from pyrobot import BOT, LOGGER_GROUP

COMMAND = "wc"

class custom(dict):
    def __missing__(self, key):
        return 0

@BOT.on_message(Filters.command(COMMAND, ".") & Filters.me)
def word_count(bot: BOT, message: Message):
    chat = message.chat.id
    check1 = str(message.command[0])
    check2 = str(message.command[-1])
    if message.chat.type == 'supergroup':
        channelname = str(message.chat.id)
        messageid = str(message.message_id)
        linkid = channelname.replace("-100", "")
        linkd = "https://t.me/c/" + linkid + "/" + messageid
        link = f"<a href='{linkd}'>{message.chat.title}</a>\n"
    elif message.chat.type == 'private':
        username = message.chat.id
        title = message.chat.first_name

        linkd = "tg://user?id=" + str(username)
        link = f"<a href='{linkd}'>{title}</a>\n"


    #Debug
#    bot.send_message(chat, check1)
#    bot.send_message(chat, check2)

    if check2 == COMMAND:
        bot.send_message(LOGGER_GROUP, "<b>Wrong input!</b>\nCorrect Syntax:\n.wc 100 20\nOut of <b>100</b> Posts back the Top<b>20</b>" )
        message.delete()
        return
    else:
        limit = int(message.command[1])
        message.delete()

    toplist = int(message.command[-1])
    words = custom()
    progress = bot.send_message(LOGGER_GROUP, "`processed 0 messages...`")
    total = 0

    for msg in bot.iter_history(chat, limit):
        total += 1
        if total % 200 == 0:
            progress.edit_text(f"`processed {total} messages...`")
        if msg.text:
            for word in msg.text.split():
                words[word.lower()] += 1
        if msg.caption:
            for word in msg.caption.split():
                words[word.lower()] += 1

    freq = sorted(words, key=words.get, reverse=True)
    out = f"Word counter from ({link}).\nOut of {limit} Posts the Top{toplist}:\n"

    for i in range(toplist):
        out += f"{i+1}. {words[freq[i]]}: {freq[i]}\n"

    progress.edit_text(out)
