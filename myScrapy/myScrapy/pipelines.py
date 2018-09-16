b# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class MyscrapyPipeline(object):    
    """ 
       功能：保存item数据 
   """
    def __init__(self):
        self.filename = open("dj.json", "w")
        self.file = open('dj.txt', 'w')

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii = False) + ",\n"
        print(text.encode("utf-8"))
        self.file.write(text)     
        json.dump(text, self.filename)
        return item

    def close_spider(self, spider):
        self.filename.close()
        self.file.close()
