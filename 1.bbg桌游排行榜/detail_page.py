import requests
from utils import get_page
from pyquery import PyQuery as pq

"""
得到详细界面的url,就行爬取详细界面的数据
"""
base_url = 'https://www.boardgamegeek.com'


def get_detail_page(detail_url):
    """
    基础url+详细url
    :param detail_url:详细界面的url
    :return:
    """
    url = base_url + detail_url
    print(url)
    html = get_page(url)
    doc = pq(html)


get_detail_page('/boardgame/147020/star-realms')
