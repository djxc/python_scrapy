# -*- coding: utf-8 -*-
import scrapy
from scrapy_moive.items import ScrapyMoiveItem


class MymoivespyderSpider(scrapy.Spider):
    name = 'myMoiveSpyder'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/8hr/page/1']
    url = 'https://www.qiushibaike.com/8hr/page/'
    offset = 1
    

    def parse(self, response):
        subSelect = response.xpath('//div[@id="content-left"]/div')
        for sub in subSelect:
            num = sub.xpath('./div/span/i[@class="number"]/text()').extract()
            if int(num[0]) > 300:
                item = ScrapyMoiveItem()
                item['moiveName'] = sub.xpath('./a[@class="contentHerf"]/div/span/text()').extract()
                item['laugthNumber'] = int(num[0])
                yield item
        if self.offset < 5:
            self.offset += 1

        # 每次处理完一页的数据之后，重新发送下一页页面请求,爬取多个网页
        # self.offset自增10，同时拼接为新的url，并调用回调函数self.parse处理Response
        yield scrapy.Request(self.url + str(self.offset), callback = self.parse)
