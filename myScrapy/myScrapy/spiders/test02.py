# -*- coding: utf-8 -*-

import scrapy
from myScrapy.items1 import MyscrapyItem1
 
class XiaoHuarSpider(scrapy.spiders.Spider):
    name = "getPicture"
    # 爬虫作用范围
    allowed_domains = ["dj.com"]

    url = "http://www.google.cn/maps/vt?lyrs=s@803&gl=cn&x="
    x = 1731111      #http://www.google.cn/maps/vt?lyrs=s@803&gl=cn&x=1731111&y=836147&z=21
    y = 836147
    z = '&z=21'
    # 起始url
    start_urls = [url + str(x) + '&y=' + str(y) + z]

    def parse(self, response):
        # 初始化模型对象
        item = MyscrapyItem1()
        item['picture'] = response
        

        if self.x < 1731115:
            self.x += 1

        # 每次处理完一页的数据之后，重新发送下一页页面请求
        # self.offset自增10，同时拼接为新的url，并调用回调函数self.parse处理Response
        yield scrapy.Request(self.url + str(self.x) + '&y=' + str(self.y) + self.z, callback = self.parse)
