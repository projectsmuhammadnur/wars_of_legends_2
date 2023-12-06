import json

import requests
from aiogram import types
from aiogram.dispatcher.filters import Text

from bot.buttons.text import account
from bot.dispatcher import dp


@dp.message_handler(Text(account))
async def get_me_function(msg: types.Message):
    user = json.loads(requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{msg.from_user.id}").content)
    await msg.answer(text=f"""
🆔 ID: <b>{user['chat_id']}</b>
🐶 Username: <b>{user['name']}</b>
🏆 Kubok: <b>{user['cup']}</b>
🪙 Tanga: <b>{user['gold']}</b>
💎 Olmos: <b>{user['diamond']}</b>
🦸 Qahramonlar: <b>{len(user['heroes'])}</b>
🎖 Medallar: <b>{len(user['medals'])}</b>
💬 AFK shikoyatlari: <b>{user['afk_count']}</b>
""", parse_mode="HTML", )
