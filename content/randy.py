# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#
# Credits by : https://t.me/xtsea
# Don't remove credits

#  This is optional or you can add this
#  await client.send_message(message.chat.id, f"done your check saved messages\n\nClick : [Click Me](tg://openmessage?user_id={message.from_user.id})")

# ---------------- main import here ------------------------------------------------------------------

import os
from pyrogram import types
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

# ---------------- base64 brain ------------------------------------------------------------------

from base64 import b64decode as bacot
kepo_lu_goblok = bacot("aHR0cHM6Ly90Lm1lL1JlbmR5UHJvamVjdHM=").decode("utf-8")

# ---------------- main command using filters ------------------------------------------------------------------

command = filters.command
private = filters.private
admins = filters.user

# ---------------- auto join channels ------------------------------------------------------------------

async def auto_join_chat(user):
    await user.join_chat("pantekyks")

# ---------------- this makes the button  ------------------------------------------------------------------

def memekontol():
    return InlineKeyboardMarkup([[InlineKeyboardButton("CHANNEL", url=f"{kepo_lu_goblok}")]])

# ---------------- main async using await ------------------------------------------------------------------

async def documents(client, message, video_or_photo, caption):
    await client.send_document(message.chat.id, video_or_photo, caption=caption)

async def coding(client, message, chat_id, message_id):
    await client.copy_message(message.chat.id, from_chat_id=chat_id, message_id=message_id, caption=None)

async def bangsat_setan(client, message):
    tolol = f"hi {message.from_user.mention}\n\nExample: `https://t.me/example/1234`"
    keyboard = memekontol()
    await client.send_message(message.chat.id, text=tolol, reply_markup=keyboard)

# ---------------- public channel using bot only ------------------------------------------------------------------

import strings.english_strings as english_strings
async def bot_copy_link(client, message):
    if message.text:
        link = message.text
        if "https://t.me/" in link:
            link_target = link.split("/")
            try:
                chat_id = link_target[-2]
            except ValueError:
                await message.reply_text(f"{english_strings.ERROR}")
                return
            message_id = int(link_target[-1])
            try:
                await coding(client, message, chat_id, message_id)
            except Exception:
                pass
                return

# ---------------- private channel using account only ------------------------------------------------------------------

async def user_copy_link(client, user, message):
    if message.text:
        link = message.text
        if "https://t.me/c" in link:
            link_target = link.split("/")
            try:
                if len(link_target) >= 2 and link_target[-2]:
                    chat_id = int("-100" + link_target[-2])
                else:
                    chat_id = None
            except ValueError:
                await message.reply_text(f"{english_strings.ERROR}")
                return
            message_id = int(link_target[-1])
            try:
                original_message = await user.get_messages(chat_id, message_ids=message_id)
            except Exception as e:
                await message.reply_text(f"{english_strings.BUG} {e}")
                return
            try:
                video_or_photo = await original_message.download()
                caption = original_message.caption or f"Uploaded by {message.from_user.mention}"
                await documents(client, message, video_or_photo, caption)
            except Exception as e:
                await message.reply_text(f"{english_strings.BUG} {e}")
                return
            try:
                os.remove(video_or_photo)
            except Exception:
                pass
                return

# ---------------- this is the end by @xtsea ------------------------------------------------------------------
