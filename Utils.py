import requests

base_headers = {
    'User-Agent': 'Mozilla/5.集石桌游手机APP-集石榜.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
}


def Get_Text_Page(url):
    """
    抓取网页的html内容
    :param url:
    :return: 网页HTML内容
    """
    # headers = dict(base_headers)
    print('正在抓取的URL', url)
    try:
        response = requests.get(url, headers=base_headers)
        if response.status_code == 200:
            print('抓取成功', url, response.status_code)
            return response.text
    except ConnectionError:
        print('抓取失败', url)
        return None


def Get_Json_Page(url):
    """
    抓取网页的json内容
    :param url:
    :return: 网页json内容
    """
    # headers = dict(base_headers)
    print('正在抓取的URL', url)
    try:
        response = requests.get(url, headers=base_headers)
        if response.status_code == 200:
            print('抓取成功', url, response.status_code)
            return response.json()
    except ConnectionError:
        print('抓取失败', url)
        return None
