import json

import requests
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.buttons.text import back_main_menu, correct, incorrect
from bot.dispatcher import bot
from main import admins


async def buy_hero_buttons(chat_id: int):
    user = json.loads(requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{chat_id}").content)
    heroes = json.loads(requests.get(url=f"http://127.0.0.1:8000/heroes/").content)
    design = []
    row = []

    for index, hero in enumerate(heroes['results'], start=1):
        if hero['id'] not in user['heroes']:
            row.append(InlineKeyboardButton(hero['name'], callback_data=f"buy_hero_{hero['id']}"))
        if index % 3 == 0 or index == len(heroes['results']):
            design.append(row)
            row = []

    design.append([InlineKeyboardButton(text=back_main_menu, callback_data=back_main_menu)])
    return InlineKeyboardMarkup(inline_keyboard=design)


async def info_hero_buttons():
    heroes = json.loads(requests.get(url=f"http://127.0.0.1:8000/heroes/").content)
    design = []
    row = []
    for index, hero in enumerate(heroes['results'], start=1):
        row.append(InlineKeyboardButton(hero['name'], callback_data=f"info_hero_{hero['id']}"))
        if index % 3 == 0 or index == len(heroes['results']):
            design.append(row)
            row = []

    design.append([InlineKeyboardButton(text=back_main_menu, callback_data=back_main_menu)])
    return InlineKeyboardMarkup(inline_keyboard=design)


async def info_medal_buttons():
    heroes = json.loads(requests.get(url=f"http://127.0.0.1:8000/medals/").content)
    design = []
    row = []
    for index, medal in enumerate(heroes['results'], start=1):
        row.append(InlineKeyboardButton(medal['name'], callback_data=f"info_medal_{medal['id']}"))
        if index % 3 == 0 or index == len(heroes['results']):
            design.append(row)
            row = []

    design.append([InlineKeyboardButton(text=back_main_menu, callback_data=back_main_menu)])
    return InlineKeyboardMarkup(inline_keyboard=design)


async def info_equipment_buttons():
    heroes = json.loads(requests.get(url=f"http://127.0.0.1:8000/equipments/").content)
    design = []
    row = []
    for index, equipment in enumerate(heroes['results'], start=1):
        row.append(InlineKeyboardButton(equipment['name'], callback_data=f"info_equipment_{equipment['id']}"))
        if index % 3 == 0 or index == len(heroes['results']):
            design.append(row)
            row = []

    design.append([InlineKeyboardButton(text=back_main_menu, callback_data=back_main_menu)])
    return InlineKeyboardMarkup(inline_keyboard=design)


async def buy_gold_buttons():
    design = [
        [InlineKeyboardButton(text="1000 🪙", callback_data="buy_gold_1000_50"),
         InlineKeyboardButton(text="5000 🪙", callback_data="buy_gold_5000_200"),
         InlineKeyboardButton(text="10000 🪙", callback_data="buy_gold_10000_350")],
        [InlineKeyboardButton(text="20000 🪙", callback_data="buy_gold_20000_650"),
         InlineKeyboardButton(text="30000 🪙", callback_data="buy_gold_30000_950"),
         InlineKeyboardButton(text="50000 🪙", callback_data="buy_gold_50000_1500")],
        [InlineKeyboardButton(text=back_main_menu, callback_data=back_main_menu)]
    ]
    return InlineKeyboardMarkup(inline_keyboard=design)


async def buy_diamond_buttons():
    design = [
        [InlineKeyboardButton(text="50 💎", callback_data="buy_diamond_60_1000"),
         InlineKeyboardButton(text="100 💎", callback_data="buy_diamond_100_2000"),
         InlineKeyboardButton(text="180 💎", callback_data="buy_diamond_180_2500")],
        [InlineKeyboardButton(text="220 💎", callback_data="buy_diamond_220_3000"),
         InlineKeyboardButton(text="300 💎", callback_data="buy_diamond_300_5000"),
         InlineKeyboardButton(text="500 💎", callback_data="buy_diamond_500_8000")],
        [InlineKeyboardButton(text=back_main_menu, callback_data=back_main_menu)]
    ]
    return InlineKeyboardMarkup(inline_keyboard=design)


async def check_donat_buttons(chat_id, diamond: int, donat_id: int):
    design = [
        [InlineKeyboardButton(text=correct, callback_data=f"correct_donat_{donat_id}_{chat_id}_{diamond}"),
         InlineKeyboardButton(text=incorrect, callback_data=f"incorrect_donat_{donat_id}_{chat_id}_{diamond}")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=design)


async def get_my_heroes_button(chat_id: int, war_id):
    war = json.loads(requests.get(url=f"http://127.0.0.1:8000/wars/detail/{war_id}").content)
    user = json.loads(requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{chat_id}").content)
    heroes = json.loads(requests.get(url=f"http://127.0.0.1:8000/heroes/").content)
    design = []
    row = []
    users_heroes = []
    for i in war_users:
        war_user = json.loads(requests.get(url=f"http://127.0.0.1:8000/war-user/detail/{i}").content)
        users_heroes.append(war_user['hero_id'])
    for index, hero in enumerate(heroes['results'], start=1):
        if hero['id'] in user['heroes'] and hero['id'] not in users_heroes:
            row.append(InlineKeyboardButton(hero['name'], callback_data=f"select_hero_{war_id}_{hero['id']}"))
        if index % 3 == 0 or index == len(heroes['results']):
            design.append(row)
            row = []

    design.append([InlineKeyboardButton(text=back_main_menu, callback_data=back_main_menu)])
    return InlineKeyboardMarkup(inline_keyboard=design)


async def select_line_buttons():
    design = [
        [InlineKeyboardButton(text="1", callback_data="select_line_1")],
        [InlineKeyboardButton(text="2", callback_data="select_line_2")],
        [InlineKeyboardButton(text="3", callback_data="select_line_3")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=design)


async def attack_hero_buttons(war_id, war_user_id):
    design = []
    war = json.loads(requests.get(url=f"http://127.0.0.1:8000/wars/detail/{war_id}").content)
    war_users = sorted(war['users'])
    blues = [war_users[0], war_users[1]]
    reads = [war_users[2], war_users[3]]
    await bot.send_message(chat_id=admins[0], text=f"{blues}\n{reads}")
    if war_user_id in blues:
        for user in reads:
            war_user = json.loads(requests.get(url=f"http://127.0.0.1:8000/war-user/detail/{user}").content)
            hero = json.loads(requests.get(url=f"http://127.0.0.1:8000/heroes/detail/{war_user['hero_id']}").content)
            design.append(
                [InlineKeyboardButton(text=hero['name'], callback_data=f"attack_hero_{war_user_id}_{war_user['id']}")])
    else:
        for user in blues:
            war_user = json.loads(requests.get(url=f"http://127.0.0.1:8000/war-user/detail/{user}").content)
            hero = json.loads(requests.get(url=f"http://127.0.0.1:8000/heroes/detail/{war_user['hero_id']}").content)
            design.append(
                [InlineKeyboardButton(text=hero['name'], callback_data=f"attack_hero_{war_user_id}_{war_user['id']}")])
    return InlineKeyboardMarkup(inline_keyboard=design)


async def buy_equipments_buttons(war_user_id):
    war_user = json.loads(requests.get(url=f"http://127.0.0.1:8000/war-user/detail/{war_user_id}").content)
    equipments = json.loads(requests.get(url=f"http://127.0.0.1:8000/equipments/").content)
    design = []
    row = []
    for index, equipment in enumerate(equipments['results'], start=1):
        if equipment['id'] not in war_user['equipments']:
            row.append(InlineKeyboardButton(equipment['name'], callback_data=f"buy_equipment_{equipment['id']}"))
        if index % 3 == 0 or index == len(equipments['results']):
            design.append(row)
            row = []

    return InlineKeyboardMarkup(inline_keyboard=design), war_user['equipments'] == 6


async def sell_equipments_buttons(war_user_id):
    war_user = json.loads(requests.get(url=f"http://127.0.0.1:8000/war-user/detail/{war_user_id}").content)
    equipments = json.loads(requests.get(url=f"http://127.0.0.1:8000/equipments/").content)
    design = []
    row = []

    for index, equipment in enumerate(equipments['results'], start=1):
        if equipment['id'] in war_user['equipments']:
            row.append(InlineKeyboardButton(equipment['name'], callback_data=f"sell_equipment_{equipment['id']}"))
        if index % 3 == 0 or index == len(equipments['results']):
            design.append(row)
            row = []

    return InlineKeyboardMarkup(inline_keyboard=design), len(design[0])
