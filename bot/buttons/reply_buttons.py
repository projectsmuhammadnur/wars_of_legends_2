from aiogram.types import ReplyKeyboardMarkup

from bot.buttons.text import referral, account, buy_hero, buy_diamond, buy_gold, back_main_menu, shop, heroes, \
    equipments, start_fight, buy_equipments, sell_equipments, attack, war_statistic, medals


async def main_menu_buttons():
    design = [
        [heroes, medals, equipments],
        [shop, start_fight],
        [account, referral]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


async def shop_menu_buttons():
    design = [[buy_hero, buy_diamond, buy_gold], [back_main_menu]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


async def back_main_menu_button():
    design = [[back_main_menu]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


async def in_war_menu_buttons():
    design = [
        [buy_equipments, sell_equipments],
        [attack, war_statistic]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
