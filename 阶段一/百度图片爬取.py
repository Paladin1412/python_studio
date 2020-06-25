# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author；鸿
import requests as r
import re
import time
import os
word = str(input('请输入需要爬取图片的名称：'))
url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&fm=index&pos=history&word={}'.format(word)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}
response = r.get(url,headers=headers)
html = response.text

urls = re.findall('"middleURL":"(.*?)"',html)
if not os.path.exists(word):
    os.mkdir(word)
i=0
for url in urls:
    time.sleep(1)
    response = r.get(url,headers=headers)
    with open(word+'/'+str(i)+'.jpg','wb') as f:
        f.write(response.content)
    i+=1
print('爬取完成')