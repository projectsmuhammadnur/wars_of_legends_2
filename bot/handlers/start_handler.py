import json
import uuid

import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart, Text

from bot.buttons.functions import start_buy_hero
from bot.buttons.reply_buttons import main_menu_buttons
from bot.buttons.text import back_main_menu
from bot.dispatcher import dp, bot
from main import admins


async def save_photo(photo: types.PhotoSize, file_path: str):
    file_id = photo.file_id
    file = await bot.get_file(file_id)
    file_path = f"{file_path}/{file_id}.jpg"
    await bot.download_file(file.file_path, file_path)
    return file_path


@dp.message_handler(Text(back_main_menu), state=['buy_diamond', 'select_hero', 'advert', 'send_forward'])
async def back_main_menu_function_1(msg: types.Message, state: FSMContext):
    await state.finish()
    await msg.answer(text=f"Asosiy menu🏠", reply_markup=await main_menu_buttons())


@dp.callback_query_handler(Text(back_main_menu), state=['buy_diamond', 'select_hero'])
async def back_main_menu_function_2(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()
    await call.message.answer(text=f"Asosiy menu🏠", reply_markup=await main_menu_buttons())


@dp.message_handler(Text(back_main_menu))
async def back_main_menu_function_1(msg: types.Message):
    await msg.answer(text=f"Asosiy menu🏠", reply_markup=await main_menu_buttons())


@dp.callback_query_handler(Text(back_main_menu))
async def back_main_menu_function_2(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=f"Asosiy menu🏠", reply_markup=await main_menu_buttons())


@dp.message_handler(CommandStart())
async def start_handler(msg: types.Message, state: FSMContext):
    user = json.loads(requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{msg.from_user.id}/").content)
    try:
        if user['detail']:
            await state.set_state("set_name")
            await msg.answer(text="✏️ Username yarating ")
            for admin in admins:
                await bot.send_message(chat_id=admin, text=f"""
Yangi user🆕
ID: <a href='tg://user?id={msg.from_user.id}'>{msg.from_user.id}</a>
Ism-Familiya: {msg.from_user.full_name}
Username: @{msg.from_user.username}\n""", parse_mode='HTML')
            data = {
                "chat_id": str(msg.from_user.id),
                "username": msg.from_user.username,
                "name": str(uuid.uuid4()),
                "full_name": msg.from_user.full_name
            }
            obj = json.loads(requests.post(url=f"http://127.0.0.1:8000/telegram-users/create/", data=data).content)
            if msg.get_args() != "":
                add_user = json.loads(
                    requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{msg.get_args()}/").content)
                if add_user['id']:
                    await bot.send_message(chat_id=int(msg.get_args()), text=f"""
Sizning yangi referal azoingiz🆕
ID: <a href='tg://user?id={msg.from_user.id}'>{msg.from_user.id}</a>
Ism-Familiya: {msg.from_user.full_name}""", parse_mode='HTML')
                    data = {
                        "adder": add_user['id'],
                        "added": obj['id']
                    }
                    requests.post(url=f"http://127.0.0.1:8000/user-to-users/create/", data=data)
                    data = {
                        "added_by": add_user['id']
                    }
                    requests.patch(url=f"http://127.0.0.1:8000/telegram-users/update/{obj['id']}/", data=data)
    except KeyError:
        await msg.answer(text="Bot yangilandi ♻️", reply_markup=await main_menu_buttons())


@dp.message_handler(state='set_name')
async def set_name_function(msg: types.Message, state: FSMContext):
    data = {
        "name": msg.text
    }
    user = json.loads(requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{msg.from_user.id}/").content)
    obj = json.loads(
        requests.patch(url=f"http://127.0.0.1:8000/telegram-users/update/{user['id']}/", data=data).content)
    try:
        if obj['detail']:
            await msg.answer(text="Bunday usernameli o'yinchi bor❗ ✏️ Username yarating")
    except KeyError:
        await start_buy_hero(tg_user_id=obj['id'])
        await msg.answer(text="O'zga olamga xush kelibsiz 🌐", reply_markup=await main_menu_buttons())
        await state.finish()
