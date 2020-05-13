# 爬取新浪微博

## 项目简介
崔庆才图书<python3网络爬虫开发实战>第六章AJAX数据爬取,中的一个小项目.


## 简介
微博首页: https://m.weibo.cn/
用户首页: https://m.weibo.cn/u/2674042787?uid=2674042787

借助chrome开发者工具,查看Ajax请求,Ajax 其实有其特殊的请求类型,它叫做xhr, 开发者工具中Network选项卡,选择Xhr,方便查找
Ajax请求

用户前十条微博(基础url): https://m.weibo.cn/api/container/getIndex?uid=2674042787&type=uid&value=2674042787&containerid=1076032674042787

十条之后的微博(基础url上添加since_id): https://m.weibo.cn/api/container/getIndex?uid=2674042787&type=uid&value=2674042787&containerid=1076032674042787&since_id=4493187957957263

uid 为用户微博用户id,进入用户首页,url上会显示, value = uid

每一个请求的url中,第九行为since_id字段,为十条微博url中since_id等于的值.



