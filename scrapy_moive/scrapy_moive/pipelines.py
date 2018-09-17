# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time

class ScrapyMoivePipeline(object):
    def process_item(self, item, spider):
        now = time.strftime('%Y-%m-%d', time.localtime())
        fileName = 'dj' + now + '.txt'
        with open(fileName, 'a') as fp:
            for s in item['moiveName']:                
                fp.write(s + '\n\n')
        return item
