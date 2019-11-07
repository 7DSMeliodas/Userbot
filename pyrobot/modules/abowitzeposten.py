from pyrobot import BOT
from pyrogram import Filters, Message


#Add Channel here
channel = ['witzeposten', 'witzeposten_pictures']

@BOT.on_message(Filters.chat(channel) & Filters.user(43817863))
def aboMeliodas(bot, message):
    channelname = str(message.chat.id)
    messageid = str(message.message_id)
    linkid = channelname.replace("-100", "")
    link = "https://t.me/c/" + linkid + "/" + messageid
    #Elias
    bot.send_message(559181265, "[Witze Abo]\nMeliodas hat einen Beitrag gepostet! Schau ihn dir an:\n" + link)
    #Timo
    bot.send_message(664780101, "[Witze Abo]\nMeliodas hat einen Beitrag gepostet! Schau ihn dir an:\n" + link)
    #Glumanda
    bot.send_message(701147500, "[Witze Abo]\nMeliodas hat einen Beitrag gepostet! Schau ihn dir an:\n" + link)
    #Eric
    bot.send_message(617318636, "[Witze Abo]\nMeliodas hat einen Beitrag gepostet! Schau ihn dir an:\n" + link)

@BOT.on_message(Filters.chat(channel) & Filters.user(559181265))
def aboElias(bot, message):
    channelname = str(message.chat.id)
    messageid = str(message.message_id)
    linkid = channelname.replace("-100", "")
    link = "https://t.me/c/" + linkid + "/" + messageid
    #Timo
    bot.send_message(664780101, "[Witze Abo]\nElias hat einen Beitrag gepostet! Schau ihn dir an:\n" + link)

@BOT.on_message(Filters.chat(channel) & Filters.user(615653533))
def aboNougatschnitte(bot, message):
    channelname = str(message.chat.id)
    messageid = str(message.message_id)
    linkid = channelname.replace("-100", "")
    link = "https://t.me/c/" + linkid + "/" + messageid
    #Timo
    bot.send_message(664780101, "[Witze Abo]\nNougatschnitte hat einen Beitrag gepostet! Schau ihn dir an:\n" + link)
    #Merlin
    bot.send_message(369684267, "[Witze Abo]\nNougatschnitte hat einen Beitrag gepostet! Schau ihn dir an:\n" + link)
    #Elias
    bot.send_message(559181265, "[Witze Abo]\nNougatschnitte hat einen Beitrag gepostet! Schau ihn dir an:\n" + link)

@BOT.on_message(Filters.chat(channel) & Filters.user(369684267))
def aboMerlinEinstein(bot, message):
    channelname = str(message.chat.id)
    messageid = str(message.message_id)
    linkid = channelname.replace("-100", "")
    link = "https://t.me/c/" + linkid + "/" + messageid
    #Nougat
    bot.send_message(615653533, "[Witze Abo]\nMerlin Einstein hat einen Beitrag gepostet! Schau ihn dir an:\n" + link)

@BOT.on_message(Filters.chat(channel) & Filters.user(701147500))
def aboGlumanda(bot, message):
    channelname = str(message.chat.id)
    messageid = str(message.message_id)
    linkid = channelname.replace("-100", "")
    link = "https://t.me/c/" + linkid + "/" + messageid
    #Elias
    bot.send_message(559181265, "[Witze Abo]\nGlumanda hat einen Beitrag gepostet! Schau ihn dir an:\n" + link)

@BOT.on_message(Filters.chat(channel) & Filters.user(275670491))
def aboBen(bot, message):
    channelname = str(message.chat.id)
    messageid = str(message.message_id)
    linkid = channelname.replace("-100", "")
    link = "https://t.me/c/" + linkid + "/" + messageid
    #Elias
    bot.send_message(559181265, "[Witze Abo]\nBen hat einen Beitrag gepostet! Schau ihn dir an:\n" + link)

@BOT.on_message(Filters.chat(channel) & Filters.user(24678795))
def aboPsycher(bot, message):
    channelname = str(message.chat.id)
    messageid = str(message.message_id)
    linkid = channelname.replace("-100", "")
    link = "https://t.me/c/" + linkid + "/" + messageid
    #Elias
    bot.send_message(664780101, "[Witze Abo]\nPsycher hat einen Beitrag gepostet! Schau ihn dir an:\n" + link)
