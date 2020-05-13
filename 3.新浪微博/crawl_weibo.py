from urllib.parse import urlencode
from pymongo import MongoClient
import requests
from pyquery import PyQuery as pq

from Utils import Get_Json_Page

base_url = 'https://m.weibo.cn/api/container/getIndex?'


def get_page(since_id):
    """
    通过url,请求json
    :param since_id: url的since_id字段
    :return: 请求的json
    """
    params = {
        'uid': '2674042787',
        'type': 'uid',
        'value': '2674042787',
        'containerid': '1076032674042787',
    }
    if since_id != 0:
        params['since_id'] = since_id  # 字典运算
    url = base_url + urlencode(params)
    return Get_Json_Page(url)


def parse_page(json):
    """
    json中提取想要的字段
    :param json: json
    :return: 微博数据
    """
    if json:
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            if item == None:
                continue
            else:
                weibo = {}
                # weibo['id'] = item.get('id')
                weibo['text'] = pq(item.get('text')).text()
                weibo['created_at'] = item.get('created_at')
                # weibo['attitudes'] = item.get('attitudes_count')
                # # weibo['comments'] = item.get('comments_count')
                # # weibo['reposts'] = item.get('reposts_count')
                yield weibo


client = MongoClient()
db = client['weibo']
collection = db['weibo']


def save_to_mongo(result):
    if collection.insert(result):
        print('Saved to Mongo')


if __name__ == '__main__':
    since_id = 0  # 前十条微博没有since_id字段
    for page in range(1, 99):
        json = get_page(since_id)
        since_id = json.get('data').get('cardlistInfo').get('since_id')  # 下一个十条微博的since_id
        results = parse_page(json)
        for result in results:
            # save_to_mongo(result)
            with open('test.txt', 'a', encoding='utf-8') as f:
                f.write('时间 :' + result['created_at'] + '  内容 :' + result['text'] + '\n')
