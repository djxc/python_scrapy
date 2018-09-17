# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyMoiveItem(scrapy.Item):
    moiveName = scrapy.Field()  # 获取电影名称
    laugthNumber = scrapy.Field()
    
