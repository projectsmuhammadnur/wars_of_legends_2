import json

import requests
from aiogram import types
from aiogram.dispatcher.filters import Text

from bot.buttons.inline_buttons import info_equipment_buttons
from bot.buttons.text import equipments
from bot.dispatcher import dp


@dp.message_handler(Text(equipments))
async def get_equipment_info_function_1(msg: types.Message):
    await msg.answer(text="Qaysi qahramon haqida ma'lumot kerak ℹ️", reply_markup=await info_equipment_buttons())


@dp.callback_query_handler(Text(startswith='info_equipment_'))
async def buy_equipment_function_2(call: types.CallbackQuery):
    equipment = json.loads(
        requests.get(url=f"http://127.0.0.1:8000/equipments/detail/{call.data.split('_')[-1]}").content)
    await call.message.delete()
    await call.message.answer_photo(photo=open(equipment['image'][22:], 'rb'), caption=f"""
🔨 Nomi: {equipment['name']}
🪙 Narxi: {equipment['salary']} tanga
❤️ Jon: {equipment['health']}
❤️‍🩹 Jon to'lishi: {equipment['restore_health']}
🧛 Vampirizm: {equipment['steal_health']}
🩸 Vampirizmdan himoya: {equipment['stealing_health_protection']}
🪄 Sehrli hujum: {equipment["magical_attack"]}
🛡 Sehrdan himoya: {equipment['magical_protection']}
⚔️Jismoniy hujum: {equipment["physical_attack"]}
🛡 Jismoniy himoya: {equipment['physical_protection']}
""", reply_markup=await info_equipment_buttons())
