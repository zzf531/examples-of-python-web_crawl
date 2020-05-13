# 爬取淘宝商品信息

## 项目简介
崔庆才图书<python3网络爬虫开发实战> 7.4章节中的一个小项目.


## 操作
- 确保安装Chrome,并配置好ChromeDriver,安装Selenium
- 使用Selenium来模拟浏览器操作,抓取淘宝的商品信息,并将结果保存

基础url: 'https://s.taobao.com/search?q=ipad    ipad为搜索商品

思路: url控制搜索的商品, 翻页操作,获取页码输入框,获取确定按钮.


显示等待: 指定要查找的节点,然后指定一个最长等待时间,如果在规定时间内加载出来这个节点,就返回查找节点,如果规定时间内,没有找出来,就抛出超时异常.

```python
browser = webdriver.Chrome()
browser.get('www.taobao.com')

wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
button = wait.ubtil(EC.element_to_be_clickable(By.CSS_SELECTOR, '.btn-serch'))
```
引入WebDriverWait对象,指定最长等待时间,然后调用它的until()方法,传入等待条件.

比如，这里传入了 presence_of_element_located 这个条件，代表节点出现的意思，其参数是节点的定位元组，也就是 ID 为 q 的节点搜索框。

这样可以做到的效果就是，在 10 秒内如果 ID 为 q 的节点（即搜索框）成功加载出来，就返回该节点；如果超过 10 秒还没有加载出来，就抛出异常。

对于按钮，element_to_be_clickable，也就是可点击，所以查找按钮时查找 CSS 选择器为.btn-search 的按钮，

更多详细的等待条件的参数及用法介绍可以参考官方文档：http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions