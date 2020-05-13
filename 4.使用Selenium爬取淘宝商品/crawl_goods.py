import json
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
import pymongo
from pyquery import PyQuery as pq

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
KEYWORD = 'Macbook pro'


def index_page(page):
    """
    抓取索引页
    :param page: 页码
    """
    print(' 正在爬取第 ', page, ' 页 ')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)
        if page > 1:
            # 输入到第几页
            input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form> input')))
            # 确定按钮,跳转到第几页
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form> span.btn.J_Submit')))
            input.clear()  # 清空文字
            input.send_keys(page)  # 输入文字
            submit.click()  # 点击按钮
        #  当前页面,页码高亮显示
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active> span'), str(page)))
        #  等待对应页面的商品信息加载
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        index_page(page)


def get_products():
    """提取商品数据"""
    html = browser.page_source  # page_source 获取源码
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            # 'image': item.find('.pic .img').attr('data-src'),
            '价格': item.find('.price').text(),
            '详情': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        with open('goods.txt', 'a', encoding='utf8') as w:
            w.write(json.dumps(product, ensure_ascii=False) + '\n')


MONGO_URL = 'localhost'
MONGO_DB = 'taobao'
MONGO_COLLECTION = 'products'
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


def save_to_mongo(result):
    try:
        if db[MONGO_COLLECTION].insert(result):
            print(' 存储到 MongoDB 成功 ')
    except Exception:
        print(' 存储到 MongoDB 失败 ')


if __name__ == '__main__':
    MAX_PAGE = 3
    """遍历每一页"""
    for i in range(1, MAX_PAGE + 1):
        index_page(i)
