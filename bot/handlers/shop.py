import json

import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from apps.donates.choices import DonatStatusChoice
from bot.buttons.inline_buttons import buy_hero_buttons, buy_gold_buttons, buy_diamond_buttons, check_donat_buttons
from bot.buttons.reply_buttons import shop_menu_buttons, back_main_menu_button, main_menu_buttons
from bot.buttons.text import shop, buy_hero, buy_gold, buy_diamond
from bot.dispatcher import dp, bot
from bot.handlers import save_photo
from main import admins


@dp.message_handler(Text(shop))
async def shop_menu_function(msg: types.Message):
    await msg.answer(text=f"Nima harid qilasiz", reply_markup=await shop_menu_buttons())


@dp.message_handler(Text(buy_hero))
async def buy_hero_function(msg: types.Message):
    await msg.answer(text=f"Qaysi qahramonni sotib olasiz 🦸", reply_markup=await buy_hero_buttons(msg.from_user.id))


@dp.callback_query_handler(Text(startswith='buy_hero_'))
async def buy_hero_function_2(call: types.CallbackQuery):
    user = json.loads(requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{call.from_user.id}/").content)
    hero = json.loads(requests.get(url=f"http://127.0.0.1:8000/heroes/detail/{call.data.split('_')[-1]}/").content)
    if user['gold'] >= hero['salary']:
        data = {
            "user": user['id'],
            "hero": hero['id']
        }
        requests.post(url=f"http://127.0.0.1:8000/user-heroes/create/", data=data)
        data = {
            "gold": user['gold'] - hero['salary']
        }
        requests.patch(url=f"http://127.0.0.1:8000/telegram-users/update/{user['id']}/", data=data)
        await call.answer(text=f"Qahramon sotib olindi ✅", show_alert=True)
        await call.message.delete()
        await call.message.answer(text=f"Nima harid qilasiz", reply_markup=await shop_menu_buttons())
    else:
        await call.message.edit_text(text=f"""
Qahramon narxi: {hero['salary']} tanga 🪙
Sizda: {user['gold']} tanga ❗️

Qaysi qahramonni sotib olasiz 🦸""", reply_markup=await buy_hero_buttons(call.from_user.id))


@dp.message_handler(Text(buy_gold))
async def buy_gold_function(msg: types.Message):
    await msg.answer(text=f"Qancha tanga sotib olasiz 🪙", reply_markup=await buy_gold_buttons())


@dp.callback_query_handler(Text(startswith='buy_gold_'))
async def buy_gold_function_2(call: types.CallbackQuery):
    salary = int(call.data.split("_")[-1])
    gold = int(call.data.split("_")[-2])
    user = json.loads(requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{call.from_user.id}/").content)
    if user['diamond'] >= salary:
        data = {
            "gold": user['gold'] + gold,
            "diamond": user['diamond'] - salary
        }
        json.loads(
            requests.patch(url=f"http://127.0.0.1:8000/telegram-users/update/{user['id']}/", data=data).content)
        await call.answer(text=f"{gold} 🪙 sotib olindi ✅", show_alert=True)
        await call.message.delete()
        await call.message.answer(text=f"Nima harid qilasiz", reply_markup=await shop_menu_buttons())
    else:
        await call.message.edit_text(text=f"""
{gold} 🪙 narxi: {salary} olmos 💎
Sizda: {user['diamond']} olmos ❗️

Qancha tanga sotib olasiz 🪙""", reply_markup=await buy_gold_buttons())


@dp.message_handler(Text(buy_diamond))
async def buy_diamond_function(msg: types.Message):
    await msg.answer(text=f"Qancha olmos sotib olasiz 💎", reply_markup=await buy_diamond_buttons())


@dp.callback_query_handler(Text(startswith='buy_diamond_'))
async def buy_diamond_function_2(call: types.CallbackQuery, state: FSMContext):
    salary = int(call.data.split('_')[-1])
    diamond = int(call.data.split("_")[-2])
    await state.set_state('buy_diamond')
    async with state.proxy() as data:
        data['salary'] = salary
        data['diamond'] = diamond
    await call.message.delete()
    await call.message.answer(text=f"""
{diamond} 💎 narxi: {salary} so'm

Pulni biror kartaga tashlang va chekni yuboring 📷

Kartalar:
💳UZKARD : 8600 1309 2432 6459
👆ISM : ISMATOV NIGMATILLA

💳MASTERCARD : 5477 3300 2118 7939
👆ISM : ISMATOV NIGMATILLA

💳CLICK: 8802811207651542
👆ISM : ISMATOV NIGMATILLA
""", reply_markup=await back_main_menu_button())


@dp.message_handler(content_types=types.ContentType.PHOTO, state="buy_diamond")
async def buy_diamond_function_3(msg: types.Message, state: FSMContext):
    await msg.answer(text="Adminga chek yuborildi✅\nTez orada javob qaytadi😊", reply_markup=await main_menu_buttons())
    async with state.proxy() as sdata:
        pass
    file_path = await save_photo(msg.photo[-1], "media/donates")
    user = json.loads(requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{msg.from_user.id}/").content)
    files = {'image': open(file_path, 'rb')}
    data = {
        "diamond": sdata['diamond'],
        'user_id': user['id']
    }
    donat = json.loads(requests.post(url="http://127.0.0.1:8000/donates/create/", data=data, files=files).content)
    for admin in admins:
        await bot.send_photo(chat_id=admin, photo=msg.photo[-1].file_id, caption=f"""
🆕 Donat: 

Olmos: {sdata['diamond']} 💎
Pul: {sdata['salary']} 💵

Chek to'g'rimi?
""", reply_markup=await check_donat_buttons(donat_id=donat['id'], chat_id=msg.from_user.id, diamond=sdata['diamond']))
    await state.finish()


@dp.callback_query_handler(Text(startswith="correct_donat_"))
async def check_buy_diamond_function_1(call: types.CallbackQuery):
    txt1, txt2, donat_id, chat_id, diamond = call.data.split('_')
    user = json.loads(requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{chat_id}/").content)
    await call.answer(text="Donat qabul qilindi✅", show_alert=True)
    await call.message.delete()
    await bot.send_message(chat_id=chat_id, text=f"Hisobingizga {diamond} 💎 tushirildi✅")
    data = {
        "status": DonatStatusChoice.CORRECT.value
    }
    requests.patch(url=f"http://127.0.0.1:8000/donates/update/{donat_id}/", data=data)
    data = {
        'diamond': user['diamond'] + int(diamond)
    }
    requests.patch(url=f"http://127.0.0.1:8000/telegram-users/update/{user['id']}/", data=data)


@dp.callback_query_handler(Text(startswith="incorrect_donat_"))
async def check_buy_diamond_function_2(call: types.CallbackQuery):
    txt1, txt2, donat_id, chat_id, diamond = call.data.split('_')
    await call.answer(text="Donat bekor qilindi❎", show_alert=True)
    await call.message.delete()
    await bot.send_message(chat_id=chat_id, text=f"Sizning {diamond} 💎 uchun yuborgan arizangiz bekor qilindi❎")
    data = {
        "status": DonatStatusChoice.INCORRECT.value
    }
    requests.patch(url=f"http://127.0.0.1:8000/donates/update/{donat_id}/", data=data)
