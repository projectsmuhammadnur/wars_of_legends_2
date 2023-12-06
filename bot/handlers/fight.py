import asyncio
import datetime
import json

import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.utils.exceptions import MessageNotModified
from bot.buttons.functions import check_day, check_attack, check_afk, check_winners
from bot.buttons.inline_buttons import get_my_heroes_button, attack_hero_buttons, \
    buy_equipments_buttons, sell_equipments_buttons
from bot.buttons.reply_buttons import back_main_menu_button, in_war_menu_buttons, main_menu_buttons
from bot.buttons.text import start_fight, attack, buy_equipments, sell_equipments, war_statistic
from bot.dispatcher import dp


@dp.message_handler(Text(start_fight))
async def start_fight_function_1(msg: types.Message, state: FSMContext):
    user = json.loads(requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{msg.from_user.id}").content)
    punishment_created_at = datetime.datetime.strptime(user['punishment_created_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
    now_time = datetime.datetime.now()
    if punishment_created_at > now_time:
        time_remaining = punishment_created_at - now_time
        hours, remainder = divmod(time_remaining.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        await msg.answer(
            text=f"Sizda jazo mavjud ❗\n\nJazo tugash vahti: {time_remaining.days} kun, {hours} soat, {minutes} daqiqa, {seconds} soniya")
    else:
        session = await msg.answer(text=f"O'yin boshlanish uchun tayyor ✅", reply_markup=await back_main_menu_button())
        await session.delete()
        war = json.loads(requests.get(url=f"http://127.0.0.1:8000/wars/filter/is_started/").content)
        if len(war['results']) == 0:
            war = json.loads(requests.post(url=f"http://127.0.0.1:8000/wars/create/", data={}).content)
            async with state.proxy() as data:
                data['war'] = war
            await state.set_state("select_hero")
            await msg.answer(text=f"Qaysi qahramonni tanlaysiz 🦸",
                             reply_markup=await get_my_heroes_button(chat_id=msg.from_user.id, war_id=war['id']))
        else:
            async with state.proxy() as data:
                data['war'] = war['results'][0]
            await state.set_state("select_hero")
            await msg.answer(text=f"Qaysi qahramonni tanlaysiz 🦸",
                             reply_markup=await get_my_heroes_button(chat_id=msg.from_user.id,
                                                                     war_id=war['results'][0]['id']))


@dp.callback_query_handler(Text(startswith='select_hero_'), state="select_hero")
async def start_fight_function_2(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    war = json.loads(requests.get(url=f"http://127.0.0.1:8000/wars/detail/{call.data.split('_')[-2]}/").content)
    session = await call.message.answer(
        text=f"O'yin boshlanishi uchun yana {4 - len(war['users'])} ta odam kerak❗\nBiroz kuting ⌛️")
    user = json.loads(requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{call.from_user.id}/").content)
    hero_id = call.data.split('_')[-1]
    hero = json.loads(requests.get(url=f"http://127.0.0.1:8000/heroes/detail/{hero_id}/").content)
    data = {
        "user_id": user['id'],
        "hero_id": hero_id,
        "health": hero['health'],
        "restore_health": hero['restore_health'],
        "steal_health": hero['steal_health'],
        "stealing_health_protection": hero['stealing_health_protection'],
        "magical_attack": hero['magical_attack'],
        "physical_attack": hero['physical_attack'],
        "magical_protection": hero['magical_protection'],
        "physical_protection": hero['physical_protection'],
        "line": 1,
    }
    war_user = json.loads(requests.post(url="http://127.0.0.1:8000/war-user/create/", data=data).content)
    data = {
        "war_id": war['id'],
        "user_id": war_user['id']
    }
    requests.post(url="http://127.0.0.1:8000/war-users/create/", data=data)
    started = False
    while not started:
        war = json.loads(requests.get(url=f"http://127.0.0.1:8000/wars/detail/{call.data.split('_')[-2]}").content)
        if len(war['users']) < 4:
            requests.patch(url=f"http://127.0.0.1:8000/war-user/update/{war_user['id']}/", data={"gold": 0})
            await state.set_state('just_state')
            try:
                await session.edit_text(
                    text=f"O'yin boshlanishi uchun yana {4 - len(war['users'])} ta odam kerak❗\nBiroz kuting ⌛️")
            except MessageNotModified:
                pass
            await asyncio.sleep(60)
        else:
            await session.delete()
            await call.message.answer(text=f"Jang maydoniga hush kelibsiz ☠", reply_markup=await in_war_menu_buttons())
            data = {
                'is_started': True
            }
            war = json.loads(requests.patch(url=f"http://127.0.0.1:8000/wars/update/{war['id']}/", data=data).content)
            async with state.proxy() as state_data:
                state_data['war_user'] = war_user
                state_data['war'] = war
            await state.set_state('war_menu')
            started = True


@dp.message_handler(Text(buy_equipments), state='war_menu')
async def buy_equipments_function_1(msg: types.Message, state: FSMContext):
    async with state.proxy() as state_data:
        pass
    afk_status, afk_id = await check_afk(war_id=state_data['war']['id'])
    if afk_status:
        await msg.answer(text=f"Bir o'yinchi AFK bo'lgani sabali o'yin tohtatildi 😔",
                         reply_markup=await main_menu_buttons())
        user = json.loads(requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{msg.from_user.id}/").content)
        data = {"gold": user['gold'] + 60}
        requests.patch(url=f"http://127.0.0.1:8000/telegram-users/update/{user['id']}/", data=data)
        await state.finish()
    else:
        bt, status = await buy_equipments_buttons(war_user_id=state_data['war_user']['id'])
        if not status:
            await msg.answer(text=f"Qaysi uskunani sotib olasiz 🔨",
                             reply_markup=bt)
        else:
            await msg.answer(text=f"Sizning sumkangiz tolgan 👝")


@dp.callback_query_handler(Text(startswith='buy_equipment_'), state='war_menu')
async def buy_equipments_function_2(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as state_data:
        pass
    afk_status, afk_id = await check_afk(war_id=state_data['war']['id'])
    if afk_status:
        await call.message.delete()
        await call.message.answer(text=f"Bir o'yinchi AFK bo'lgani sabali o'yin tohtatildi 😔",
                                  reply_markup=await main_menu_buttons())
        user = json.loads(
            requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{call.from_user.id}/").content)
        data = {"gold": user['gold'] + 60}
        requests.patch(url=f"http://127.0.0.1:8000/telegram-users/update/{user['id']}/", data=data)
        await state.finish()
    else:
        war_user = json.loads(
            requests.get(url=f"http://127.0.0.1:8000/war-user/detail/{state_data['war_user']['id']}/").content)
        equipment = json.loads(
            requests.get(url=f"http://127.0.0.1:8000/equipments/detail/{call.data.split('_')[-1]}/").content)
        await call.message.delete()
        if war_user['gold'] >= equipment['salary']:
            await state.set_state('war_menu')
            await call.message.answer(text=f"Uskuna sotib olindi ✅", reply_markup=await in_war_menu_buttons())
            data = {
                "user": war_user['id'],
                "equipment": equipment['id']
            }
            requests.post(url=f"http://127.0.0.1:8000/user-equipments/create/", data=data)
            data = {
                "gold": war_user['gold'] - equipment['salary'],
                "health": war_user['health'] + equipment['health'],
                "restore_health": war_user['restore_health'] + equipment['restore_health'],
                "steal_health": war_user['steal_health'] + equipment['steal_health'],
                "stealing_health_protection": war_user['stealing_health_protection'] + equipment[
                    'stealing_health_protection'],
                "magical_attack": war_user['magical_attack'] + equipment['magical_attack'],
                "physical_attack": war_user['physical_attack'] + equipment['physical_attack'],
                "magical_protection": war_user['magical_protection'] + equipment['magical_protection'],
                "physical_protection": war_user['physical_protection'] + equipment['physical_protection']
            }
            requests.patch(url=f"http://127.0.0.1:8000/war-user/update/{war_user['id']}/", data=data)
        else:
            await call.message.answer(text=f"""
Uskuna narxi: {equipment['salary']} tanga 🪙
Sizda: {war_user['gold']} tanga ❗️""", reply_markup=await in_war_menu_buttons())


@dp.message_handler(Text(sell_equipments), state='war_menu')
async def sell_equipments_function_1(msg: types.Message, state: FSMContext):
    async with state.proxy() as state_data:
        pass
    afk_status, afk_id = await check_afk(war_id=state_data['war']['id'])
    if afk_status:
        await msg.answer(text=f"Bir o'yinchi AFK bo'lgani sabali o'yin tohtatildi 😔",
                         reply_markup=await main_menu_buttons())
        user = json.loads(requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{msg.from_user.id}/").content)
        data = {"gold": user['gold'] + 60}
        requests.patch(url=f"http://127.0.0.1:8000/telegram-users/update/{user['id']}/", data=data)
        await state.finish()
    else:
        bt, num = await sell_equipments_buttons(war_user_id=state_data['war_user']['id'])
        if num > 0:
            await msg.answer(text=f"Qaysi uskunani sotasiz 🔨",
                             reply_markup=bt)
        else:
            await msg.answer(text=f"Siz hali uskuna sotib olmagansiz 🔨")


@dp.callback_query_handler(Text(startswith='sell_equipment_'), state='war_menu')
async def sell_equipments_function_2(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as state_data:
        pass
    afk_status, afk_id = await check_afk(war_id=state_data['war']['id'])
    if afk_status:
        await call.message.delete()
        await call.message.answer(text=f"Bir o'yinchi AFK bo'lgani sabali o'yin tohtatildi 😔",
                                  reply_markup=await main_menu_buttons())
        user = json.loads(
            requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{call.from_user.id}/").content)
        data = {"gold": user['gold'] + 60}
        requests.patch(url=f"http://127.0.0.1:8000/telegram-users/update/{user['id']}/", data=data)
        await state.finish()
    else:
        war_user = json.loads(
            requests.get(url=f"http://127.0.0.1:8000/war-user/detail/{state_data['war_user']['id']}/").content)
        equipment = json.loads(
            requests.get(url=f"http://127.0.0.1:8000/equipments/detail/{call.data.split('_')[-1]}/").content)
        await call.message.delete()
        await call.message.answer(text=f"Uskuna sotildi ✅", reply_markup=await in_war_menu_buttons())
        data = {
            "gold": war_user['gold'] + (equipment['salary'] - (equipment['salary'] * 0.4)),
            "health": war_user['health'] - equipment['health'],
            "restore_health": war_user['restore_health'] - equipment['restore_health'],
            "steal_health": war_user['steal_health'] - equipment['steal_health'],
            "stealing_health_protection": war_user['stealing_health_protection'] - equipment[
                'stealing_health_protection'],
            "magical_attack": war_user['magical_attack'] - equipment['magical_attack'],
            "physical_attack": war_user['physical_attack'] - equipment['physical_attack'],
            "magical_protection": war_user['magical_protection'] - equipment['magical_protection'],
            "physical_protection": war_user['physical_protection'] - equipment['physical_protection']
        }
        requests.patch(url=f"http://127.0.0.1:8000/war-user/update/{war_user['id']}/", data=data)


@dp.message_handler(Text(war_statistic), state='war_menu')
async def get_statistic_function_1(msg: types.Message, state: FSMContext):
    async with state.proxy() as state_data:
        pass
    reply = f"{msg.text}\n\n🔵 Koklar:\n"
    war = json.loads(requests.get(url=f"http://127.0.0.1:8000/wars/detail/{state_data['war']['id']}/").content)
    war_users = sorted(war['users'])
    for user in [war_users[0], war_users[1]]:
        war_user = json.loads(requests.get(url=f"http://127.0.0.1:8000/war-user/detail/{user}/").content)
        hero = json.loads(requests.get(url=f"http://127.0.0.1:8000/heroes/detail/{war_user['hero_id']}/").content)
        tg_user = json.loads(
            requests.get(url=f"http://127.0.0.1:8000/telegram-users/detail/{war_user['user_id']}/").content)
        if not war_user['is_dead']:
            reply += f"""
👤 Ismi: {tg_user['name']}
🥷 Qahramon: {hero['name']}
🪙 Tanga: {war_user['gold']}
❤️ Jon: {war_user['health']}
❤️‍🩹 Jon to'lishi: {war_user['restore_health']}
🧛 Vampirizm: {war_user['steal_health']}
🩸 Vampirizmdan himoya: {war_user['stealing_health_protection']}
🪄 Sehrli hujum: {war_user["magical_attack"]}
🛡 Sehrdan himoya: {war_user['magical_protection']}
⚔️ Jismoniy hujum: {war_user["physical_attack"]}
🛡 Jismoniy himoya: {war_user['physical_protection']}\n
"""
    reply += "\n🔴 Qizillar:\n"
    for user in [war_users[2], war_users[3]]:
        war_user = json.loads(requests.get(url=f"http://127.0.0.1:8000/war-user/detail/{user}/").content)
        hero = json.loads(requests.get(url=f"http://127.0.0.1:8000/heroes/detail/{war_user['hero_id']}/").content)
        tg_user = json.loads(
            requests.get(url=f"http://127.0.0.1:8000/telegram-users/detail/{war_user['user_id']}/").content)
        if not war_user['is_dead']:
            reply += f"""
👤 Ismi: {tg_user['name']}
🥷 Qahramon: {hero['name']}
🪙 Tanga: {war_user['gold']}
❤️ Jon: {war_user['health']}
❤️‍🩹 Jon to'lishi: {war_user['restore_health']}
🧛 Vampirizm: {war_user['steal_health']}
🩸 Vampirizmdan himoya: {war_user['stealing_health_protection']}
🪄 Sehrli hujum: {war_user["magical_attack"]}
🛡 Sehrdan himoya: {war_user['magical_protection']}
⚔️ Jismoniy hujum: {war_user["physical_attack"]}
🛡 Jismoniy himoya: {war_user['physical_protection']}\n
"""
    await msg.answer(text=reply)


@dp.message_handler(Text(attack), state='war_menu')
async def fight_function_1(msg: types.Message, state: FSMContext):
    async with state.proxy() as state_data:
        pass
    afk_status, afk_id = await check_afk(war_id=state_data['war']['id'])
    if afk_status:
        await msg.answer(text=f"Bir o'yinchi AFK bo'lgani sabali o'yin tohtatildi 😔",
                         reply_markup=await main_menu_buttons())
        user = json.loads(requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{msg.from_user.id}/").content)
        data = {"gold": user['gold'] + 60}
        requests.patch(url=f"http://127.0.0.1:8000/telegram-users/update/{user['id']}/", data=data)
        await state.finish()
    else:
        status, dead_status = await check_attack(user_id=state_data['war_user']['id'])
        war_status, user_status = await check_winners(state_data['war']['id'], state_data['war_user']['id'])
        if war_status:
            await state.finish()
            if user_status:
                await msg.answer(text=f"G'alaba🥳\n\n+70 🪙 oldingiz", reply_markup=await main_menu_buttons())
            else:
                await msg.answer(text=f"Mag'lubiyat😔\n\n+50 🪙 oldingiz", reply_markup=await main_menu_buttons())
        elif status:
            await msg.answer(text=f"Boshqalar hali hujum qilmoqda sabirli bo'ling ⌛")
        elif dead_status:
            await msg.answer(text=f"Siz olgansiz ☠️")
        else:
            await state.set_state("attack_hero")
            await msg.answer(text=f"Qaysi dushmanga hujum qilasiz?",
                             reply_markup=await attack_hero_buttons(war_id=state_data['war']['id'],
                                                                    war_user_id=state_data['war_user']['id']))


@dp.callback_query_handler(Text(startswith="attack_hero_"), state='attack_hero')
async def fight_function_1(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as state_data:
        pass
    afk_status, afk_id = await check_afk(war_id=state_data['war']['id'])
    if afk_status:
        await call.message.delete()
        await call.message.answer(text=f"Bir o'yinchi AFK bo'lgani sabali o'yin tohtatildi 😔",
                                  reply_markup=await main_menu_buttons())
        user = json.loads(
            requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{call.from_user.id}/").content)
        data = {"gold": user['gold'] + 60}
        requests.patch(url=f"http://127.0.0.1:8000/telegram-users/update/{user['id']}/", data=data)
        await state.finish()
    else:
        txt1, txt2, user_id, a_user_id = call.data.split('_')
        user = json.loads(requests.get(url=f"http://127.0.0.1:8000/war-user/detail/{user_id}/").content)
        a_user = json.loads(requests.get(url=f"http://127.0.0.1:8000/war-user/detail/{a_user_id}/").content)
        health = user["steal_health"] - a_user['stealing_health_protection']
        a_health = a_user['health'] - ((user['magical_attack'] + user["physical_attack"]) - (
                a_user['magical_protection'] + a_user['physical_protection']))
        is_dead = False
        if a_health <= 0:
            is_dead = True
        data = {
            "health": a_health,
            "is_dead": is_dead
        }
        requests.patch(url=f"http://127.0.0.1:8000/war-user/update/{a_user['id']}/", data=data)
        data = {
            "health": user['health'] + health,
            "is_attack": True
        }
        user = json.loads(requests.patch(url=f"http://127.0.0.1:8000/war-user/update/{user['id']}/", data=data).content)
        status, day = await check_day(state_data['war']['id'])
        await call.message.delete()
        await state.set_state('war_menu')
        if user['is_dead'] is True:
            await call.message.answer(text=f"Siz oldingiz❗", reply_markup=await in_war_menu_buttons())
        else:
            await call.message.answer(text=f"{day} - kun tugadi", reply_markup=await in_war_menu_buttons())
