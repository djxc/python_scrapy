# -*- coding: utf-8 -*-
import json

def changeDirecttoJson(data1):    
    # Python 字典类型转换为 JSON 对象
    
    
    json_str = json.dumps(data1)
    print ("Python 原始数据：", repr(data1))
    print ("JSON 对象：", json_str)


def changejson2driect(json_str):
    # 将 JSON 对象转换为 Python 字典
    data2 = json.loads(json_str)
    print ("data2['name']: ", data2['name'])
    print ("data2['url']: ", data2['url'])


def writeJson():
    # 写入 JSON 数据
    with open('data.json', 'w') as f:
        json.dump(data1, f)
    
    
def readJsonfile():
    # 读取数据
    with open('data.json', 'r') as f:
        data = json.load(f)
        print(data['name'])
        
def readJsonfile1():
    # 读取数据
    with open('dj1.json', 'r') as f:
        while 1:
            lines = f.readlines(100000)
            if not lines:
                break
            for line in lines:
                l = line[:len(line)-2]
                data = json.loads(l)
                print(data["positionname"])
        

if __name__ == "__main__":
    data1 = {
        'no' : 1,
        'name' : 'Runoob',
        'url' : 'http://www.runoob.com'
    }
    readJsonfile1()
#    writeJson()
