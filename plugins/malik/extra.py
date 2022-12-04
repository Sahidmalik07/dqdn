#sahid malik
from __future__ import unicode_literals
import math
import wget
import time
import re
import os
import json
import asyncio
import asyncio
import aiohttp
import aiofiles
import pyrogram
import requests
from os import environ
from typing import List
from Script import script
from telegraph import upload_file
from info import PHT, ADMINS, AUTH_USERS
from pyrogram.errors import FloodWait
from pyrogram.errors import FloodWait, MessageNotModified
from youtubesearchpython import SearchVideos
from pyrogram.errors.exceptions.forbidden_403 import ChatWriteForbidden
from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired, UserAdminInvalid
from pyrogram.types.messages_and_media import message
from pyrogram.types import Message, ChatPermissions, InlineKeyboardButton
from database.users_chats_db import db
from database.ia_filterdb import Media
from pyrogram import Client, filters, enums 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from utils import temp, get_size
from collections import defaultdict
from typing import Dict, List, Union
from time import time, sleep


# Commands Botinfo

@Client.on_message(filters.command("BOTINFO") & filters.incoming)
async def botinfo(client, message):
    if len(message.command):
        buttons = [[
            InlineKeyboardButton('❇️ Add Me To Your Groups ❇️', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=(GHHMO),
            caption=(GHHMM.format(message.from_user.mention)),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

# Commands stats

@Client.on_message(filters.command('malik') & filters.incoming)
async def get_ststs(bot, message):
    malik = await message.reply('Wait..')
    total_users = await db.total_users_count()
    await malik.edit(
               text=(GHHMT.format(total_users)),
               reply_markup=InlineKeyboardMarkup(
                                      [[
                                        InlineKeyboardButton('🌐 Add Me To Your Groups 🌐', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
                                      ]]
               ),
               parse_mode=enums.ParseMode.HTML
)

# Commands Owner Details 

@Client.on_message(filters.command("OWNER") & filters.incoming)
async def owner(client, message):
    if len(message.command):
        buttons = [[
            InlineKeyboardButton('💢 close 💢', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=(GHHMN),
            caption=(MY_DETALS.format(message.from_user.mention)),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        return

# Commands Rules

@Client.on_message(filters.command("RULES") & filters.incoming)
async def rules(client, message):
    if len(message.command):
        buttons = [[
            InlineKeyboardButton('💢 close 💢', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=(G_R),
            caption=(GROUP_Rules),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        return


#telegra.ph 

@Client.on_message(filters.command(["tel", "tg", "telegraph"]))
async def telegraph(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply("Reply to a supported media file")
        return
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (
            replied.video
            and replied.video.file_name.endswith(".mp4")
            and replied.video.file_size <= 5242880
        )
        or (
            replied.document
            and replied.document.file_name.endswith(
                (".jpg", ".jpeg", ".png", ".gif", ".mp4"),
            )
            and replied.document.file_size <= 5242880
        )
    ):
        s = await message.reply_photo(
        photo=(MQTK),
        caption=(MMALL.format(message.from_user.mention)),
        reply_markup=InlineKeyboardMarkup(
                      [[
                        InlineKeyboardButton('Try again ', callback_data="close_data")
                      ]]
        ),
        parse_mode=enums.ParseMode.HTML
)
        await asyncio.sleep(10)
        await s.delete()
        return    
    download_location = await client.download_media(
        message=message.reply_to_message,
        file_name="root/downloads/",
    )
    mkn=await message.reply_text(
        text="<code>Trying to processing please weit.....</code>",
        disable_web_page_preview=True
    )
    await asyncio.sleep(1)
    await mkn.delete()
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply(message, text=document)
    else:
        await message.reply_photo(
            photo=f"https://telegra.ph{response[0]}",
            caption=f"<b>𝗅𝗂𝗇𝗄:-</b> <code>https://telegra.ph{response[0]}</code>\n\n Powerd By: @m_house786 ",
            quote=True,
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("⚡️ Open Link⚡️", url=f"https://telegra.ph{response[0]}"),
               InlineKeyboardButton("♻️ Shere Link ♻️", url=f"https://telegram.me/share/url?url=https://telegra.ph{response[0]}")
               ],[
               InlineKeyboardButton("💢 Close 💢", callback_data="close_data")
               ]]
            ),
            parse_mode=enums.ParseMode.HTML
)
    finally:
        os.remove(download_location)

# sticker py

@Client.on_message(filters.command(["stickerid", "sticker", "st"]))
async def stickerid(bot, message):   
    if message.reply_to_message.sticker:
       await message.reply(f"**Sticker ID is**  \n `{message.reply_to_message.sticker.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.sticker.file_unique_id}`", quote=True)
    else: 
       n = await message.reply_photo(
       photo=(MQTK),
       caption=(MMAL.format(message.from_user.mention)),
       reply_markup=InlineKeyboardMarkup(
                      [[
                        InlineKeyboardButton('Try again ', callback_data="close_data")
                      ]]
       ),
       parse_mode=enums.ParseMode.HTML
)
       await asyncio.sleep(12)
       await n.delete()


SS_ALERT = """

🔹ᴍʏ ɴᴀᴍᴇ ᴍᴏᴠɪᴇs ʜᴏᴜsᴇ  🏠 Bᴏᴛ
🔹I ᴀᴍ Aᴜᴛᴏ Fɪʟᴛᴇʀ Bᴏᴛ.😎
🔹Jᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀs ᴀᴅᴍɪɴ
🔹ɪᴛ ᴡɪʟ ᴘʀᴏᴠɪᴅᴇ ᴀʟʟ ᴍᴏᴠɪᴇs ʏᴏᴜʀ  ɢʀᴏᴜᴘ.😎

🔹ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟs ᴛʏᴘᴇ  👉 /ʙᴏᴛɪɴғᴏ 
🔹Oᴠɴᴇʀ ᴅᴇᴛᴀɪʟs ᴛɪᴘᴇ  👉  /ᴏᴡɴᴇʀ"""

RULES_ALERT = """
🔹ᴍᴏᴠɪᴇ sᴇᴀʀᴄʜ Ex:
 1 ᴀᴠᴇɴɢᴇʀs ✅
 2 ᴀᴠᴇɴɢᴇʀs ʜɪɴᴅɪ ✅
 3 ᴀᴠᴇɴɢᴇʀs ʜɪɴᴅɪ ᴍᴏᴠɪᴇ ❌

🔹 Wᴇʙ Sᴇʀɪᴇs Exʟ:
 1 ᴠɪᴋɪɴɢs S01 ✅
 2 ᴠɪᴋɪɴɢs S01E01 ✅
 3 ᴠɪᴋɪɴɢs sᴇᴀsᴏɴ 1 ❌

🔹Mᴏʀᴇ ᴅᴇᴛᴀɪʟᴇs ᴛɪᴘᴇ 👉 /ʀᴜʟᴇs"""

REPORT = """➤ 𝐇𝐞𝐥𝐩: Report ⚠️

𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚛𝚎𝚙𝚘𝚛𝚝 𝚊 𝚖𝚎𝚜𝚜𝚊𝚐𝚎 𝚘𝚛 𝚊 𝚞𝚜𝚎𝚛 𝚝𝚘 𝚝𝚑𝚎 𝚊𝚍𝚖𝚒𝚗𝚜 𝚘𝚏 𝚝𝚑𝚎 𝚛𝚎𝚜𝚙𝚎𝚌𝚝𝚒𝚟𝚎 𝚐𝚛𝚘𝚞𝚙. 𝙳𝚘𝚗'𝚝 𝚖𝚒𝚜𝚞𝚜𝚎 𝚝𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍.

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪/report 𝗈𝗋 @admins - 𝖳𝗈 𝗋𝖾𝗉𝗈𝗋𝗍 𝖺 𝗎𝗌𝖾𝗋 𝗍𝗈 𝗍𝗁𝖾 𝖺𝖽𝗆𝗂𝗇𝗌 (𝗋𝖾𝗉𝗅𝗒 𝗍𝗈 𝖺 𝗆𝖾𝗌𝗌𝖺𝗀𝖾)."""


PURGE = """<b>Purge</b>
    
Delete A Lot Of Messages From Groups! 
    
 <b>ADMIN</b> 

◉ /purge :- Delete All Messages From The Replied To Message, To The Current Message"""

MUTE = """➤ <b>𝐇𝐞𝐥𝐩: Mute 🚫

𝚃𝚑𝚎𝚜𝚎 𝚊𝚛𝚎 𝚝𝚑𝚎 𝚌𝚘𝚖𝚖𝚊𝚗𝚍𝚜 𝚊 𝚐𝚛𝚘𝚞𝚙 𝚊𝚍𝚖𝚒𝚗 𝚌𝚊𝚗 𝚞𝚜𝚎 𝚝𝚘 𝚖𝚊𝚗𝚊𝚐𝚎 𝚝𝚑𝚎𝚒𝚛 𝚐𝚛𝚘𝚞𝚙 𝚖𝚘𝚛𝚎 𝚎𝚏𝚏𝚒𝚌𝚒𝚎𝚗𝚝𝚕𝚢.

➪/ban: 𝖳𝗈 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝖿𝗋𝗈𝗆 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/unban: 𝖳𝗈 𝗎𝗇𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/tban: 𝖳𝗈 𝗍𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋.
➪/mute: 𝖳𝗈 𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/unmute: 𝖳𝗈 𝗎𝗇𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/tmute: 𝖳𝗈 𝗍𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋.

➤ 𝖭𝗈𝗍𝖾:
𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tmute 𝗈𝗋 /tban 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗍𝗂𝗆𝖾 𝗅𝗂𝗆𝗂𝗍.

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝖻𝖺𝗇 2𝖽 𝗈𝗋 /𝗍𝗆𝗎𝗍𝖾 2𝖽.
𝖸𝗈𝗎 𝖼𝖺𝗇 𝗎𝗌𝖾 𝗏𝖺𝗅𝗎𝖾𝗌: 𝗆/𝗁/𝖽. 
 • 𝗆 = 𝗆𝗂𝗇𝗎𝗍𝖾𝗌
 • 𝗁 = 𝗁𝗈𝗎𝗋𝗌
 • 𝖽 = 𝖽𝖺𝗒𝗌</b>"""

MQTT = """<b>⚠️ 𝐇𝐞𝐲, {}!..</b> 

<b>𝐘𝐨𝐮𝐫 𝐰𝐨𝐫𝐝</b> 👉 <s>{}</s> ...
<b>𝐢𝐬 𝐍𝐨 𝐌𝐨𝐯𝐢𝐞/𝐒𝐞𝐫𝐢𝐞𝐬 𝐑𝐞𝐥𝐚𝐭𝐞𝐝 𝐭𝐨 𝐭𝐡𝐞 𝐆𝐢𝐯𝐞𝐧 𝐖𝐨𝐫𝐝 𝐖𝐚𝐬 𝐅𝐨𝐮𝐧𝐝 🥺
𝐏𝐥𝐞𝐚𝐬𝐞 𝐆𝐨 𝐭𝐨 𝐆𝐨𝐨𝐠𝐥𝐞 𝐚𝐧𝐝 𝐂𝐨𝐧𝐟𝐢𝐫𝐦 𝐭𝐡𝐞 𝐂𝐨𝐫𝐫𝐞𝐜𝐭 𝐒𝐩𝐞𝐥𝐥𝐢𝐧𝐠 🥺</b> <b><a href=https://www.google.com>𝐆𝐨𝐨𝐠𝐥𝐞</a></b>"""



WCM = """<b>𝗛𝗲𝘆 {} .!   

🔹 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴏᴜʀ ɢʀᴏᴜᴘ.. <s>{}</s>

🔹 ᴛʜɪs ɪs ᴀ ᴍᴏᴠɪᴇ ɢʀᴏᴜᴘ

🔹 ᴀʟʟ ᴄᴀᴛᴇɢᴏʀɪᴇs ᴏғ ᴍᴏᴠɪᴇs
      ᴀᴠᴀɪʟʟᴀʙᴀʟᴇ ʜᴇʀᴇ..

🔹 ᴊᴜsᴛ ᴛɪᴘᴇ ᴛʜᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ

🔹 ᴏᴜʀ ᴡɪʟʟ sᴇɴᴅ ʏᴏᴜʀ ᴍᴏᴠɪᴇ ..

🔹 ᴘʟᴇᴀsᴇ ʀᴇᴀᴅ ɢʀᴏᴜᴘ ʀᴜʟᴇs

🔹 ©ᴍᴀɴᴛᴀɪɴᴇᴅ ʙʏ: sᴀʜɪᴅ ᴍᴀʟɪᴋ</b>"""

STTS = """<b>🗂𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
👨‍👩‍👧‍👧 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
🤿 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
⏳ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
⌛️ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱</b> """

# kick opinion 

CREATOR_REQUIRED = """❗<b>You have To Be The Group Creator To Do That.</b>"""
      
INPUT_REQUIRED = "❗ **Arguments Required**"
      
KICKED = """✔️ Successfully Kicked {} Members According To The Arguments Provided."""
      
START_KICK = """🚮 Removing Inactive Members This May Take A While..."""
      
ADMIN_REQUIRED = """❗<b>I will not go to the place where I am not made Admin.. Add Me Again with all admin rights.</b>"""
      
DKICK = """✔️ Kicked {} Deleted Accounts Successfully."""
      
FETCHING_INFO = """<b>wait...</b>"""
      
STATUS = """{}\n<b>Chat Member Status</b>**\n\n```<i>Recently``` - {}\n```Within Week``` - {}\n```Within Month``` - {}\n```Long Time Ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}</i>
"""

TEL = """<b>⚙ HELP: Telegraph 🏞

Do as you wish with telegra.ph module!

USAGE:

📲 /telegraph, /tel. - Send me Picture or Vide Under (5MB)

NOTE:

• This Command Is Available in goups and pms
• This Command Can be used by everyone</b>"""



GHHMT = """<b>𝗧𝗵𝗮𝗻𝗸𝘀 𝗙𝗼𝗿 👨‍👧‍👧 {}.𝗨𝘀𝗲𝗿... 💖 

🔹 ᴛʜᴀɴᴋs ғᴏʀ ʏᴏᴜʀ sᴜᴘᴘᴏʀᴛ...

🔹 ᴊᴜsᴛ ᴀᴅᴅ ᴏᴜʀ ʙᴏᴛ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀs ᴀᴅᴍɪɴ, ɪᴛ ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇs ᴛʜᴇʀᴇ... 😎


     ♋️ 𝗙𝗲𝗮𝘁𝘂𝗿𝗲𝘀 ♋️

🔹 Aᴜᴛᴏғɪʟᴛᴇʀ, Mᴀɴᴜᴀʟ Fɪʟᴛᴇʀ
🔹 ɪᴍᴅʙ ʜᴅ ᴘᴏsᴛᴇʀs
🔹 ɪᴍᴅʙ Rᴇᴀʟ Dᴇᴛᴀɪʟs
🔹 ᴛᴡᴏ Bᴜᴛᴛᴏɴs Mᴀᴅᴇ
🔹 Fᴏʀᴄᴇ Sᴜʙsᴄʀɪʙᴇ
🔹 Fɪʟᴇ-Sᴛᴏʀᴇ
🔹 Exᴛʀᴀ Fᴇᴀᴛᴜʀᴇs: ᴅᴏᴡɴʟᴏᴀᴅ
       sᴏɴɢᴇs,
🔹 ᴅᴏᴡɴʟᴏᴀᴅ ʏᴏᴜ ᴛᴜʙᴇ ᴠɪᴅᴇᴏ, 
🔹 ᴜʀʟ Sʜᴏʀᴛɴᴇʀ, ᴍᴜᴛᴇ ᴜsᴇʀ,
🔹 ᴜɴᴍᴜᴛᴇ ʏsᴇʀ. Pᴜʀɢᴇ,
🔹 ᴀᴅᴍɪɴ ʀᴇᴘᴏʀᴛ. 
🔹 ᴘʜᴏᴛᴏ ᴄᴏɴᴠᴇʀᴛᴏʀ ᴛᴇʟᴇɢʀᴀғᴇ
       ʟɪɴᴋ...

🔹 Xᴛʀᴀ Cʜᴇᴄᴋ sᴘᴇʟʟɪɴɢ. Bᴜᴛᴛᴏɴs..
🔹 ᴄʜᴇᴄᴋ ᴍᴏᴠɪᴇ ʀᴇʟᴇᴀsᴇ ᴅᴀᴛᴇ 📅. 
🔹 ᴏᴛᴛ ʀᴇʟᴇᴀsᴇ ᴅᴀᴛᴇ ᴀɴᴅ ᴍᴏʀᴇ..

⚙ ᴍᴏʀᴇ Fᴇᴀᴛᴜʀᴇs ᴀᴅᴅɪɴɢ sᴏᴏɴ...</b>😎"""


GHHMM = """<b>Hey {}.. ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ʙᴏᴛ ɪɴғᴏ ❤️.

🔹 ᴍʏ ɴᴀᴍᴇ ᴍᴏᴠɪᴇs 🏠 ʙᴏᴛ..
🔹 I ᴀᴍ ᴀᴜᴛᴏғɪʟᴛᴇʀ ʙᴏᴛ.. 

🔹 ᴊᴜsᴛ ᴀᴅᴅ Oᴜʀ ʙᴏᴛ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ 
       ɪs ᴀᴅᴍɪɴ,  
🔹 ɪᴛ ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇs ᴛʜᴇʀᴇ 
       ғʀᴇᴇ...

        ♋️ 𝗙𝗲𝗮𝘁𝘂𝗿𝗲𝘀 ♋️

🔹 Aᴜᴛᴏғɪʟᴛᴇʀ, Mᴀɴᴜᴀʟ Fɪʟᴛᴇʀ
🔹 ɪᴍᴅʙ ʜᴅ ᴘᴏsᴛᴇʀs
🔹 ɪᴍᴅʙ Rᴇᴀʟ Dᴇᴛᴀɪʟs
🔹 ᴛᴡᴏ Bᴜᴛᴛᴏɴs Mᴀᴅᴇ
🔹 Fᴏʀᴄᴇ Sᴜʙsᴄʀɪʙᴇ
🔹 Fɪʟᴇ-Sᴛᴏʀᴇ
🔹 Exᴛʀᴀ Fᴇᴀᴛᴜʀᴇs: ᴅᴏᴡɴʟᴏᴀᴅ
       sᴏɴɢᴇs,
🔹 ᴅᴏᴡɴʟᴏᴀᴅ ʏᴏᴜ ᴛᴜʙᴇ ᴠɪᴅᴇᴏ, 
🔹 ᴜʀʟ Sʜᴏʀᴛɴᴇʀ, ᴍᴜᴛᴇ ᴜsᴇʀ,
🔹 ᴜɴᴍᴜᴛᴇ ʏsᴇʀ. Pᴜʀɢᴇ,
🔹 ᴀᴅᴍɪɴ ʀᴇᴘᴏʀᴛ. 
🔹 ᴘʜᴏᴛᴏ ᴄᴏɴᴠᴇʀᴛᴏʀ ᴛᴇʟᴇɢʀᴀғᴇ
       ʟɪɴᴋ...

🔹 Xᴛʀᴀ Cʜᴇᴄᴋ sᴘᴇʟʟɪɴɢ. Bᴜᴛᴛᴏɴs..
🔹 ᴄʜᴇᴄᴋ ᴍᴏᴠɪᴇ ʀᴇʟᴇᴀsᴇ ᴅᴀᴛᴇ 📅. 
🔹 ᴏᴛᴛ ʀᴇʟᴇᴀsᴇ ᴅᴀᴛᴇ ᴀɴᴅ ᴍᴏʀᴇ..
🔹 4ɢʙ sᴜᴘᴘᴏʀᴛ
🔹 ғᴏɴᴛs sᴛʏʟɪsʜ ᴛᴇx
⚙ ᴍᴏʀᴇ Fᴇᴀᴛᴜʀᴇs ᴀᴅᴅɪɴɢ sᴏᴏɴ...</b>😎"""

GROUP_Rules = """<b>
     🔹 𝗚𝗥𝗢𝗨𝗣 𝗥𝗨𝗟𝗘𝗦 🔹

🔹 sᴇᴀʀᴄʜ ᴡɪᴛʜ ᴄᴏʀʀᴇᴄᴛ sᴘᴇʟʟɪɴɢ..
🔹 ᴛʀʏ ᴛᴏ sᴇᴀʀᴄʜ ᴍᴏᴠɪᴇ ᴡɪᴛʜ ʏᴇᴀʀ ɪғ ᴛʜᴇ ʙᴏᴛɪs ɴᴏᴛ sᴇɴᴅɪɴɢ ʏᴏᴜ ᴀᴄᴄᴜʀᴀᴛᴇ ʀᴇsᴜʟᴛ...

🔹 𝘀𝗲𝗮𝗿𝗰𝗵 𝗺𝗼𝘃𝗶𝗲 𝗶𝗻 𝗧𝗵𝗲 𝗚𝗶𝘃𝗲𝗻 𝗙𝗿𝗼𝗺 𝗘𝘅𝗹:   
🔹 (1) ᴀᴠᴇɴɢᴇʀs ✅
🔹 (2) ᴀᴠᴇɴɢᴇʀs ʜɪɴᴅɪ ✅
🔹 (3) ᴀᴠᴇɴɢᴇʀs ᴍᴏᴠɪᴇ ❌
🔹 (4) ᴀᴠᴇɴɢᴇʀs ʜɪɴᴅɪ ᴅᴜʙʙᴇᴅ..❌

🔹 𝘀𝗲𝗮𝗿𝗰𝗵 𝘄𝗲𝗯 𝘀𝗲𝗿𝗶𝗲𝘀 𝗶𝗻 𝗧𝗵𝗲 𝗚𝗶𝘃𝗲𝗻 𝗙𝗿𝗼𝗺 𝗘𝘅𝗹:
🔹 (1) ᴠɪᴋɪɴɢs S01 ✅
🔹 (2) ᴠɪᴋɪɴɢs S01E01 ✅
🔹 (3) ᴠɪᴋɪɴɢs S01E10 ✅
🔹 (4) ᴠɪᴋɪɴɢs S01 ʜɪɴᴅɪ ✅
🔹 (5) ᴠɪᴋɪɴɢs S01 ʜɪɴᴅɪ ᴅᴜʙʙ. ❌
🔹 (6) ᴠɪᴋɪɴɢs sᴇᴀsᴏɴ 1 ❌
🔹 (7) ᴠɪᴋɪɴɢs sᴇᴀsᴏɴ 1 ᴇᴘɪsᴏᴅᴇ 1 ❌
🔹 (8) ᴠɪᴋɪɴɢs ᴡᴇʙ sᴇʀɪᴇs ❌

🔹 Dᴏɴ'ᴛ Dᴏ ᴀɴʏ sᴇʟғ ᴘʀᴏᴍᴏᴛɪᴏɴ.

🔹 ᴅᴏɴ'ᴛ sᴇɴᴅ ᴀɴʏ ᴋɪɴᴅ ᴏғ ᴘʜᴏᴛᴏ, ᴠɪᴅᴇᴏ ᴅᴏᴄᴜᴍᴇɴᴛs 𝗨𝗥𝗟 𝗘𝗧𝗖.

🔹 sᴇɴᴅɪɴɢ ᴛʜᴇ ᴀʙᴏᴠᴇ ᴍᴀɴᴛᴀɪɴᴇᴅ, ᴛʜɪɴɢs ᴡɪʟʟ ʟᴇᴀᴅ ᴛᴏ ᴘᴇʀᴍᴀɴᴇɴᴛ ʙᴀɴ.

🔹 ᴅᴏɴ'ᴛ ʀᴇǫᴜᴇsᴛ ᴀɴʏ ᴛʜɪɴɢs ᴏᴛʜᴇʀ ᴛʜᴀɴ ᴍᴏᴠɪᴇ sᴇʀɪᴇs ᴀɴɪᴍᴇs..

🔹 ᴅᴏɴ'ᴛ ᴅɪsᴛᴜʀʙ ᴀɴʏᴏɴᴇ ᴏɴ ᴛʜᴇ ɢʀᴏᴜᴘ..

🔹 ɢɪᴠᴇ ᴀɴᴅ ᴛᴀᴋᴇ ʀᴇsᴘᴇᴄᴛ</b>"""


MY_DETALS = """<b>Hey {}. Welcome ❤️

🔹 ᴍʏ ɴᴀᴍᴇ : sᴀʜɪᴅ ᴍᴀʟɪᴋ
🔹 ᴜsᴇʀɴᴀᴍᴇ: @sahid_malik
🔹 ᴘᴍᴛ. ᴅᴍ ʟɪɴᴋ: <a href=https://t.me/sahid_malik>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>
🔹 ᴘʟᴀᴄᴇ: sᴀʜᴀʀᴀɴᴘᴜʀ | ᴜᴘ | ɪɴᴅɪᴀ
🔹 ᴋɴᴏᴡ ʟᴀɴɢᴜᴀɢᴇ: ʜɪɴᴅɪ, ᴇɴɢʟɪsʜ,
      ᴍᴀʟʏᴀʟᴀᴍ
🔹 ʀᴇʟɪɢɪᴏɴ ᴄᴀsᴛ: ᴍᴜsʟɪᴍ
🔹 ᴅᴏʙ: 00 | 09 | 2005
🔹 Aɢᴇ: ᴊᴜsᴛ ᴄᴀʟᴄᴜʟᴀᴛᴇ
🔹 ʟᴇᴠᴇʟ: ғʀɪsᴛ ʏᴇᴀʀ ʙᴛᴇᴄ ᴇᴄᴇ
🔹 ғᴀᴠ ᴄᴏʟᴏᴜʀ: ʀᴇᴅ, ɢʀᴇᴇɴ, ʙʟᴜᴇ..</b>"""


GOOGL = """🔹𝗛𝗲𝗹𝗽 𝗚𝗼𝗼𝗴𝗹𝗲 𝗧𝗿𝗮𝗻𝘀𝗹𝗮𝘁𝗲🔹

🔸ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴛʀᴀɴsʟᴀᴛᴇ ᴀ ᴛᴇxᴛ ᴄᴏᴍᴍᴀɴᴅ ᴡᴏʀᴋs ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ..

🔹𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗮𝗻𝗱 𝗨𝘀𝗮𝗴𝗲🔹

🔸 /tr - ᴛᴏ ᴛʀᴀɴsʟᴀᴛᴇ ᴛᴇxᴛs ᴛᴏ ᴀ sᴘᴇᴄɪғɪᴄ ʟᴀɴɢᴜᴀɢᴇ..

🔹 𝗡𝗼𝘁𝗲 🔹

🔸ᴡʜɪʟᴇ ᴜsɪɴɢ /tr ʏᴏᴜ sʜᴏᴜʟᴅ sᴘᴇᴄɪғʏ ᴛʜᴇ ʟᴀɴɢᴜᴀɢᴇ ᴄᴏᴅᴇ.

🔹 𝗘𝘅𝗹: /tr hi
🔸 ᴇɴ = Eɴɢʟɪꜱʜ 
🔸 ᴍʟ = ᴍᴀʟᴀʏᴀʟᴀᴍ 
🔸 ʜɪ = Hɪɴᴅɪ"""

SHARETXT = """🔹 ʜᴇʟᴘ ғᴏʀ  ᴄᴀʀɪᴛᴇ ꜱʜᴀʀᴇ  ᴛᴇxᴛ ʟɪɴᴋ🔹

sʜᴀʀᴇ ᴛᴇxᴛ  ɪꜱ ᴀ ᴍᴏᴅᴜʟᴇ ғᴏʀ ᴍᴀᴋᴇ ʏᴏᴜʀ sʜᴀʀᴇ ᴛᴇxᴛ ʟɪɴᴋ..

ғᴏʀ ᴜꜱᴇ ᴛʜᴀᴛ ғᴇᴜᴛᴜʀᴇ ᴛʏᴘᴇ ..

/share ᴀɴᴅ /Sharetxt [ʏᴏᴜʀ ᴛᴇxᴛ] ᴛʜᴇɴ ʏᴏᴜʀ ᴛᴇxᴛ ɪꜱ ʀᴇᴅʏ.."""

WALL = """sorry not working"""

MMALL = """<b>Hey {}.👋\n\n⚠️Oops !! Not supported media file\n\nReply to a supported media file</b>"""
MMAL = """<b>Hey {}.👋\n\n⚠️Oops !! Not a sticker file\n\nplease Reply Valid sticker file</b>"""

STKR = """ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴍᴏᴅᴜʟᴇs ᴛᴏ ғɪɴᴅ ᴀɴʏ sᴛɪᴄᴋᴇʀ ɪᴅ.
 
 ᴛᴏ ɢᴇᴛ sᴛɪᴄᴋᴇʀ ɪᴅ 

🔹 <b>ʜᴏᴡ ᴛᴏ ᴜsᴇ</b> 🔹


ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ sᴛɪᴄᴋᴇʀ /STICKER  ᴀɴᴅ /ST"""

FONTS = """🔹 <b>ʜᴇʟᴘ ғᴏʀ ғᴏɴᴛs</b> 🔹

ғᴏɴᴛ ɪs ᴀ ᴍᴏᴅᴜʟᴇ ғᴏʀ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴛᴇxᴛ sᴛʏʟᴇs.

ғᴏʀ ᴜsᴇ ᴛʜᴀᴛ ғᴇᴜᴛᴜʀᴇ ᴛʏᴘᴇ ..

/FONTS,  [ʏᴏᴜʀ ᴛᴇxᴛ] ᴛʜᴇɴ ʏᴏᴜʀ ᴛᴇxᴛ ɪs ʀᴇᴅʏ."""

WRITE = """» ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ ꜰᴏʀ​​ WʀɪᴛᴇTᴏᴏʟ :


 Wʀɪᴛᴇꜱ ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ ᴏɴ ᴡʜɪᴛᴇ ᴘᴀɢᴇ ᴡɪᴛʜ ᴀ ᴘᴇɴ 🖊

❍ /ᴡʀɪᴛᴇ <ᴛᴇxᴛ> : Wʀɪᴛᴇꜱ ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ."""

SONGS = """sᴏɴɢ ᴅᴏᴡɴʟᴏᴀᴅ ᴍᴏᴅᴜʟᴇ...

sᴏɴɢ ᴅᴏᴡɴʟᴏᴀᴅ ᴍᴏᴅᴜʟᴇ. ғᴏʀ...
ᴛʜᴏsᴇ ᴡʜᴏ ʟᴏᴠᴇ ᴍᴜsɪᴄ. ʏᴏᴜ ᴄᴀɴ ʏsᴇ ᴛʜɪs ғᴇᴀᴛᴜʀᴇ ғᴏʀ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ sᴏɴɢ ᴡɪᴛʜ sᴜᴘᴇʀ ғᴀsᴛ sᴘᴇᴇᴅ ᴡᴏᴋs ᴏɴʟʏ ᴏɴ ɢʀᴏᴜᴘs...

🔹 ᴄᴏᴍᴍᴀɴᴅs 🔹

/song sᴏɴɢ ɴᴀᴍᴇ
ᴡᴏʀᴋs ᴏɴʟʏ ᴏɴ ɢʀᴏᴜᴘ"""

MALIKK = """<b>ʜᴇʏ {}.👋\n\n⚠️Oops !! ʏᴏᴜʀ ʀᴏɴɢ\n\nᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ\n\nғʀɪsᴛ ✍ ᴛɪᴘᴇ ʏᴏᴜʀ ᴛᴇxᴛ ᴀɴᴅ ʀᴇᴘʟʏ /tr hi
ʜɪ = ʜɪɴᴅɪ 
ᴇɴ = ᴇɴɢʟɪsʜ 
ᴍʟ = ᴍᴀʟᴀʏᴀʟᴀᴍ </b>"""
MALK = environ.get("MALk", "https://telegra.ph/file/66278d019899141f4b028.jpg")



MQTK = environ.get("MQTK", "https://telegra.ph/file/66278d019899141f4b028.jpg")
TMP_DOWNLOAD_DIRECTORY = environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")
PPC = environ.get("PPC", "https://telegra.ph/file/3b6afd6c6fcd09606ea9f.jpg")
MQTTP = environ.get("MQTTP", "https://telegra.ph/file/f8a3c7a57376427646f39.jpg")
TG_MAX_SELECT_LEN = environ.get("TG_MAX_SELECT_LEN", "100")
WCM_P = environ.get("WCM_P", "https://telegra.ph/file/bdaa63ddf255fd3506f0a.jpg")
SMART_PIC = environ.get("SMART_PIC", "https://telegra.ph/file/fd6f54fabecefbef8976a.jpg")
GHHMN = environ.get("GHHMN", "https://telegra.ph/file/4265c6e3428cd2b060ede.jpg")
GHHMO = environ.get("GHHMNO", "https://telegra.ph/file/605f4c8b2461c1e4f8123.jpg")
G_R = environ.get("G_R", "https://telegra.ph/file/0dd95cec0179cb3721d71.jpg")
COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")
PPI = environ.get("PPI", "https://telegra.ph/file/fd6f54fabecefbef8976a.jpg")

IYGL = environ.get("IYGL", "https://youtu.be/R0Fhv079dhQ")

REQUEST_ADMIN = environ.get("REQUEST_ADMIN", "https://t.me/m_admins")
YTILK = environ.get("YTILK", "https://youtube.com/channel/UCPaHDqWf3D3w2nxb8p3sr4A")
GRP_IT_LK = environ.get("GRP_IT_LK", "https://t.me/+FAgX05kGByNkZjJl")
DP_YRS = environ.get("DL_YRS", "https://youtu.be/v7Vbu3u_VrE")


