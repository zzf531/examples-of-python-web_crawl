import requests
import json
from pymongo import MongoClient


def detail_get_page(game_id):
    url = 'https://www.gstonegames.com/app/game_get/'
    a = {
        "game_id": game_id
    }
    response = requests.post(url=url, json=a)
    print(response.status_code)
    if response.status_code == 200:
        return response.json()


def detail_parse_page(jsons):
    items = jsons.get('data').get('game')
    top = {}
    top["category"] = get_theme(items['category'])  # 分类
    top["mode"] = items['mode'].get('sch_domain_value')
    top['theme'] = get_theme(items['theme'])  # 主题
    top['mechanic'] = get_theme(items['mechanic'])  # 机制
    top['difficulty'] = items['difficulty']  # 游戏难度
    top['average_time'] = items['average_time_per_player']  # 平均时长
    top['minimum_age'] = items['minimum_age']  # 最小年龄
    # top['sch_description'] = items['sch_description']

    yield top


def get_theme(theme):
    theme_len = len(theme)
    l = []
    for i in range(0, theme_len):
        l.append(theme[i].get('sch_domain_value'))
    return l


if __name__ == '__main__':
    game_id = 16127
    data = detail_get_page(game_id)
    results = detail_parse_page(data)
    for i in results:
        print(i)



