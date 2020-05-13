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
KEYWORD = 'iPad'
url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
browser.get(url)
input1 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form> input')))
input2 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input')))
submit = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
input3 = browser.find_element(By.CSS_SELECTOR, '#mainsrp-pager div.form> input')
page = 1
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active> span'), str(2)))

print(input1)
print(input2)
print(input3)
print(submit.text)
browser.close()