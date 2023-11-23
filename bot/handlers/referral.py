import json

import requests
from aiogram import types
from aiogram.dispatcher.filters import Text

from bot.buttons.text import referral
from bot.dispatcher import dp


@dp.message_handler(Text(referral))
async def referral_function(msg: types.Message):
    user = json.loads(requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{msg.from_user.id}").content)
    await msg.answer(text=f"""
Sizning referal linkingiz👇\n<code>https://t.me/Wars_Of_Legends_Bot?start={msg.from_user.id}</code>
\n{len(user['added_users'])}-ta odam taklif qilgansiz👤""", parse_mode="HTML")
