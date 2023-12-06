import json

import requests
from aiogram import types
from aiogram.dispatcher.filters import Text

from bot.buttons.inline_buttons import info_hero_buttons
from bot.buttons.text import heroes
from bot.dispatcher import dp


@dp.message_handler(Text(heroes))
async def get_hero_info_function_1(msg: types.Message):
    await msg.answer(text="Qaysi qahramon haqida ma'lumot kerak ℹ️", reply_markup=await info_hero_buttons())


@dp.callback_query_handler(Text(startswith='info_hero_'))
async def buy_hero_function_2(call: types.CallbackQuery):
    hero = json.loads(requests.get(url=f"http://127.0.0.1:8000/heroes/detail/{call.data.split('_')[-1]}").content)
    await call.message.delete()
    await call.message.answer_photo(photo=open(hero['image'][22:], 'rb'), caption=f"""
👤 Ismi: {hero['name']}
🥷 Vazifa: {hero['role']}
🪙 Narxi: {hero['salary']} tanga
❤️ Jon: {hero['health']}
❤️‍🩹 Jon to'lishi: {hero['restore_health']}
🧛 Vampirizm: {hero['steal_health']}
🩸 Vampirizmdan himoya: {hero['stealing_health_protection']}
🪄 Sehrli hujum: {hero["magical_attack"]}
🛡 Sehrdan himoya: {hero['magical_protection']}
⚔️Jismoniy hujum: {hero["physical_attack"]}
🛡 Jismoniy himoya: {hero['physical_protection']}
🧊 Boshqaruv: {hero['control']}
⛔ Boshqaruvdan himoya: {hero['control_protection']}\n
""", reply_markup=await info_hero_buttons())
