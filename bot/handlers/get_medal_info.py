import json

import requests
from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.utils.exceptions import MessageNotModified

from bot.buttons.inline_buttons import info_medal_buttons
from bot.buttons.text import medals
from bot.dispatcher import dp


@dp.message_handler(Text(medals))
async def get_hero_info_function_1(msg: types.Message):
    await msg.answer(text="Qaysi medal haqida ma'lumot kerak ℹ️", reply_markup=await info_medal_buttons())


@dp.callback_query_handler(Text(startswith='info_medal_'))
async def buy_hero_function_2(call: types.CallbackQuery):
    medal = json.loads(requests.get(url=f"http://127.0.0.1:8000/medals/detail/{call.data.split('_')[-1]}").content)
    try:
        await call.message.edit_text(text=f"""
📝 Nomi: {medal['name']}
🪙 Mukofot: {medal['gold']} tanga
💬 Qo'shimcha: {medal['description']}
""", reply_markup=await info_medal_buttons())
    except MessageNotModified:
        pass
