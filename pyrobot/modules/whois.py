"""Get info about the replied user/user id/or in privat chat
Syntax: .whois"""

from time import sleep
from datetime import datetime

from pyrogram import Filters, Message, User
from pyrogram.errors import PeerIdInvalid
from pyrogram.api import functions
from pyrobot import BOT, NO_PICTURE_PATH

from pyrogram import Client, Filters

import os

#Get User Information
@BOT.on_message(Filters.command("whois", ".")  & Filters.me)

def who_is(client, message):
    from_user = None
    if " " in message.text:
        recvd_command, user_id = message.text.split(" ")
        try:
            user_id = int(user_id)
            from_user = client.get_users(user_id)
        except Exception as e:
            message.edit(str(e))
            return
    elif message.reply_to_message:
        from_user = message.reply_to_message.from_user
    elif message.chat.type == 'private':
        from_user = client.get_users(message.chat.id)
    else:
        message.edit("no valid user_id / message specified")
        return

    if from_user is not None:
        #Get ID
        cmd = message.command
        if not message.reply_to_message and len(cmd) == 1:
            get_user = message.chat.id
        elif message.reply_to_message and len(cmd) == 1:
            get_user = message.reply_to_message.from_user.id
        elif len(cmd) > 1:
            get_user = cmd[1]
            try:
                get_user = int(cmd[1])
            except ValueError:
                pass

    #Online Status
#        onlinestatus = client.get_users(user_id)
        onlinestatus=from_user.status
        if from_user.status=="recently":
            onlinestatus="Recently"
        elif from_user.status=="within_week":
            onlinestatus="Within the last week"
        elif from_user.status=="within_month":
            onlinestatus="Within the last month"
        elif from_user.status=="long_time_ago":
            onlinestatus="A long time ago :("
        elif from_user.status=="online":
            onlinestatus="Currently Online"
        elif from_user.status=="offline":
            onlinestatus="Offline"
        else:
            onlinestatus="Error: Unkown Online Status!"
            
        #Userpics count
        pic_count = client.get_profile_photos_count(from_user.id)

			
		#Common Chats
        common = client.get_common_chats(from_user.id)
        sendcommon = len(common)
		
        #Get Profile Picture
        chat_photo = from_user.photo
		
        #Calculate Last Online Time
        time=None
        if from_user.last_online_date:
            timeunix = from_user.last_online_date
            time = datetime.fromtimestamp(timeunix).strftime("%a, %d %b %Y, %H:%M:%S")
		
        #Variable for BIO
        bio = client.get_chat(get_user).description

        #Message with Picture
        message_out_str = ""
        message_out_str += f"Profile Pictures: {pic_count}\n"
        message_out_str += f"\n"
        message_out_str += f"ID: <a href='tg://user?id={from_user.id}'>{from_user.id}</a>\n"
        message_out_str += f"\n"
        message_out_str += f"First Name: <a href='tg://user?id={from_user.id}'>{from_user.first_name}</a>\n"
        message_out_str += f"Last Name: {from_user.last_name}\n"
        message_out_str += f"Username: @{from_user.username}\n"
        message_out_str += f"Common Groups: {sendcommon}\n"
        message_out_str += f"\n"
        message_out_str += f"Is self: {from_user.is_self}\n"
        message_out_str += f"Is Bot: {from_user.is_bot}\n"
        message_out_str += f"Is Scam: {from_user.is_scam}\n"
        message_out_str += f"Is Support: {from_user.is_support}\n"
        message_out_str += f"Is Contact: {from_user.is_contact}\n"
        message_out_str += f"Is mutual Contact: {from_user.is_mutual_contact}\n"
        message_out_str += f"Is Deleted: {from_user.is_deleted}\n"
        message_out_str += f"Is Verified: {from_user.is_verified}\n"
        message_out_str += f"Is Restricted: {from_user.is_restricted}\n"
        message_out_str += f"\n"
        message_out_str += f"Last online: {onlinestatus}\n"
#        message_out_str += f"Last online: {from_user.status}\n"
        message_out_str += f"DC ID: {from_user.dc_id}\n"
#        message_out_str += f"\n"
        if not time == None:
            message_out_str += f"Last online: {time}\n"
#        message_out_str += f"Last offline: {from_user.next_offline_date}\n"
#        message_out_str += f"Language: {from_user.language_code}\n"
#        message_out_str += f"Restrictions: {from_user.restrictions}\n"
        message_out_str += f"\n"
        message_out_str += f"Bio: \n{bio}\n"

    if from_user.photo is not None:
        local_user_photo = client.download_media(
            message=chat_photo.big_file_id
        )
        message.reply_photo(
            photo=local_user_photo,
            quote=True,
            caption=message_out_str,
            parse_mode="html",
            disable_notification=True
        )
        os.remove(local_user_photo)
        message.delete()
        # If User without Picture
    else:
        local_user_photo=NO_PICTURE_PATH
        message.reply_photo(
            photo=local_user_photo,
            quote=True,
            caption=message_out_str,
            parse_mode="html",
            disable_notification=True
        )
        message.delete()
