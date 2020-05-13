import re
import time
import json
import requests
from requests.exceptions import RequestException

from Utils import Get_Text_Page


def parse_one_page(html):
    """
    正则式根据爬取的html进行匹配,和网页上显示的有差异
    :param html: 猫眼页面html内容
    :return: 字典
    """
    pattern = re.compile('board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
    + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
    + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {'排名': item[0],
            # '图片': item[1],
            '电影名': item[2],
            '演员': item[3].strip()[3:],
            '时长': item[4].strip()[5:],
            '评分': item[5] + item[6]
        }


def write_to_file(content):
    with open('result2.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    """
    猫眼url变化第一页为10,第二页为20...
    :param offset: 页数 * 10
    :return:
    """
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = Get_Text_Page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)
