from pyrobot import BOT, LOGGER, LOGGER_GROUP


def LogMessage(logmsg):
    if LOGGER:
        BOT.send_message(
            chat_id=LOGGER_GROUP,
            text=logmsg)
