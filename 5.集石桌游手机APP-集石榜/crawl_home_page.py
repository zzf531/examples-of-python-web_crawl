import json
import requests
from pymongo import MongoClient
from .crawl_detail_page import detail_get_page, detail_parse_page


def get_page(page_number):
    url = 'https://www.gstonegames.com/app/hot_ranking/'
    a = {
        "category_type": "gs",
        "game_page": page_number
    }
    response = requests.post(url=url, json=a)
    print(response.status_code)
    if response.status_code == 200:
        return response.json()


def parse_page(jsons):
    items = jsons.get('data')
    for item in items:
        top = {}
        top['rank'] = item.get('rank_index')
        top['id'] = item.get('id')
        top['name'] = item.get('sch_name')
        if not top['name']:
            top['name'] = item.get('eng_name')
        top['rating'] = item.get('gstone_rating')
        top['year'] = item.get('publish_year')
        detail_data = detail_get_page(top['id'])
        aa = detail_parse_page(detail_data)
        for a in aa:
            top['detail'] = a
        yield top


client = MongoClient()
db = client['gs']
collection = db['gs500']


def save_to_mongo(result):
    if collection.insert(result):
        print('Saved to Mongo')


if __name__ == '__main__':
    for page in range(1, 26):
        data = get_page(page)
        results = parse_page(data)
        for result in results:
            with open('test.txt', 'a', encoding='utf-8') as f:
                f.write('名字:' + result['name'] + '评分:' + str(result['rating']) + '\n')
            save_to_mongo(result)
