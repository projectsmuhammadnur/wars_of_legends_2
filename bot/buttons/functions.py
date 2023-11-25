import datetime
import json

import requests


async def start_buy_hero(tg_user_id):
    for hero in range(1, 9):
        data = {
            "user": tg_user_id,
            "hero": hero
        }
        requests.post(url=f"http://127.0.0.1:8000/user-heroes/create/", data=data)
    return True


async def check_day(war_id):
    war = json.loads(requests.get(url=f"http://127.0.0.1:8000/wars/detail/{war_id}").content)
    for user in war['users']:
        user = json.loads(requests.get(url=f"http://127.0.0.1:8000/war-user/detail/{user}").content)
        if not user['is_dead'] and not user['is_attack']:
            return False, war['day']
    for user in war['users']:
        w_user = json.loads(requests.get(url=f"http://127.0.0.1:8000/war-user/detail/{user}").content)
        data = {
            "is_attack": False,
            "health": w_user['health'] + w_user['restore_health'],
            "gold": w_user['gold'] + 10
        }
        requests.patch(url=f"http://127.0.0.1:8000/war-user/update/{user}", data=data)
    data = {"day": war['day'] + 1}
    requests.patch(url=f"http://127.0.0.1:8000/wars/update/{war_id}", data=data)
    return True, war['day']


async def check_attack(user_id):
    user = json.loads(requests.get(url=f"http://127.0.0.1:8000/war-user/detail/{user_id}").content)
    return user['is_attack'], user['is_control']


async def check_afk(war_id):
    war = json.loads(requests.get(url=f"http://127.0.0.1:8000/wars/detail/{war_id}").content)
    for user in war['users']:
        user = json.loads(requests.get(url=f"http://127.0.0.1:8000/war-user/detail/{user}").content)
        updated_at = datetime.datetime.strptime(user['updated_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
        if updated_at > (datetime.datetime.now() + datetime.timedelta(minutes=5)):
            tg_user = json.loads(
                requests.get(url=f"http://127.0.0.1:8000/telegram-users/detail/{user['user_id']}").content)
            data = {
                "afk_count": tg_user['afk_count'] + 1,
                "punishment_count": tg_user['punishment_count'] + 1,
                "punishment_created_at": datetime.datetime.now() + datetime.timedelta(
                    seconds=100 * tg_user['punishment_count'])
            }
            requests.patch(url=f"http://127.0.0.1:8000/telegram-users/update/{tg_user['id']}", data=data)
            return True, user['id']
    return False, None


async def check_winners(war_id, war_user_id):
    blues = []
    reds = []
    war = json.loads(requests.get(url=f"http://127.0.0.1:8000/wars/detail/{war_id}").content)
    for user in war['users'][4:]:
        user = json.loads(requests.get(url=f"http://127.0.0.1:8000/war-user/detail/{user}").content)
        if user['is_dead'] is True:
            blues.append(user['id'])
    for user in war['users'][:4]:
        user = json.loads(requests.get(url=f"http://127.0.0.1:8000/war-user/detail/{user}").content)
        if user['is_dead'] is True:
            reds.append(user['id'])
    if len(blues) != 4 and len(reds) != 4:
        return False, None
    else:
        user = json.loads(requests.get(url=f"http://127.0.0.1:8000/war-user/detail/{war_user_id}/").content)
        winners = max(blues, reds, key=len)
        if war_user_id in winners:
            tg_user = json.loads(
                requests.get(url=f"http://127.0.0.1:8000/telegram-users/detail/{user['user_id']}/").content)
            data = {"gold": tg_user['gold'] + 70}
            requests.patch(url=f"http://127.0.0.1:8000/telegram-users/update/{tg_user['id']}/", data=data)
            return True, True
        else:
            tg_user = json.loads(
                requests.get(url=f"http://127.0.0.1:8000/telegram-users/detail/{user['user_id']}/").content)
            data = {"gold": tg_user['gold'] + 50}
            requests.patch(url=f"http://127.0.0.1:8000/telegram-users/update/{tg_user['id']}/", data=data)
            return True, True
