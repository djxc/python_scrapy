# -*- coding: utf-8 -*-
import userAgents
import time
import urllib
import logging
from myLog import MyLog
import re

def linkWeb():
    url = 'http://www.baidu.com'
    try:
        response = urllib.request.urlopen(url, timeout=3)
    except urllib.error:
        print('网络地址错误')
        exit()
    with open('test.txt', 'w') as fp:
        fp.write(response.read().decode())
    print(response.getcode())
    print(response.info())

def Urllib2ModifyHeader():
		#这个是PC + IE 的User-Agent
		PIUA = userAgents.pcUserAgent.get('IE 9.0')
		#这个是Mobile + UC的User-Agent
		MUUA = userAgents.mobileUserAgent.get('UC standard')
		#测试用的网站选择的是有道翻译        

		useUserAgent(PIUA,1)
		useUserAgent(MUUA,2)

def useUserAgent(userAgent,name):
     url = 'http://fanyi.youdao.com'
     request = urllib.request.Request(url)
     request.add_header(userAgent.split(':')[0],userAgent.split(':')[1])
     response = urllib.request.urlopen(request)

     fileName = str(name) + '.html'

     with open(fileName,'a') as fp:
#         fp.write("%s\n\n" %userAgent)
         fp.write(response.read().decode())

def testLogging():
    logFormat = '%(asctime)-12s %(levelname)-8s %(name)-10s %(message)-12s'
    logFileName = './testLog.txt'
    logging.basicConfig(level = logging.INFO,
    format = logFormat, filename = logFileName, filemode = 'w')
    logging.debug('debug message')
    logging.info('info message')
    logging.warning('warning message')
    logging.error('error message')
    logging.critical('critical message')

def testLog():
    mylog = MyLog()
    mylog.debug('it is debug')
    mylog.error("I'm error")

def testTime():
    print(time.time())
    print(time.strftime('%Y-%m-%d %X %A', time.localtime()))

def testRe():
    s = 'I am dj, i am from linyi and i am very happy! i am 10 years old.'
    print(re.search('am', s).group())
    print(re.match('am', s))
    print(re.findall('am .\d .*', s))
    
if __name__ == "__main__":
#    linkWeb()
#    Urllib2ModifyHeader()
#    testLogging()
#    testLog()
    testTime()
    testRe()
