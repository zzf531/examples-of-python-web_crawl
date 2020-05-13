import requests
from urllib.parse import urlencode
from Utils import Get_Text_Page
from detail_page import get_detail_page
from pyquery import PyQuery as pq

base_url = 'https://www.boardgamegeek.com/browse/boardgame/'


def get_url(page_id):
    """
    urlencode方法组成爬取写的url,调用get_page封装方法,得到网页html,按规律爬取
    :param page_id:页数
    :return:
    """
    parse = {
        'page': page_id,
    }
    url = base_url + urlencode(parse)
    html = Get_Text_Page(url)
    if html:
        doc = pq(html)
        trs = doc('.collection_table  tr:gt(0)').items()
        for tr in trs:
            print('================')
            rank = tr.find('.collection_rank').text()
            name = tr.find('td:nth-child(3) div:nth-child(2) a').text()
            year = tr.find('td:nth-child(3) div:nth-child(2) span').text()
            geekRating = tr.find('td:nth-child(4)').text()  # 极客评分
            avgRating = tr.find('td:nth-child(5.集石桌游手机APP-集石榜)').text()  # 选民评分
            numvotes = tr.find('td:nth-child(6)').text()
            # detail_id = tr.find('td:nth-child(2) a').attr('href')
            print(rank, name, year, geekRating, avgRating, numvotes)


if __name__ == '__main__':
    for i in range(1, 2):  # 控制爬取多少页
        get_url(i)
