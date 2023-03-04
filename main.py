# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#
# Credits by : https://t.me/xtsea

import logging
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from config import API_ID, API_HASH, BOT_TOKEN, STRING, OWNER_ID
from content.randy import *
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton 

logging.basicConfig(level=logging.INFO)

randydev = Client(name="app", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
user = Client(name="app", api_id=API_ID, api_hash=API_HASH, session_string=STRING)
user.start()

# ----------------- account starting ------------------------------------------------

async def main():
    async with Client(name="app", api_id=API_ID, api_hash=API_HASH, session_string=STRING) as user:
        await auto_join_chat(user)
        print(f"{user.me.first_name} Bot Online Now")

if __name__ == '__main__':
    event_policy = asyncio.get_event_loop_policy()
    event_loop = event_policy.get_event_loop()
    asyncio.set_event_loop(event_loop)
    event_loop.run_until_complete(main())

# ----------------- this is bot only ------------------------------------------------

@randydev.on_message(command("start"))
async def start_welcome(client:  Client, message: Message):
    await bangsat_setan(client, message)

@randydev.on_message(private & admins(OWNER_ID))
async def public_or_private_channel(client: Client, message: Message):
    await user_copy_link(client, user, message)
    await bot_copy_link(client, message)

randydev.run()
