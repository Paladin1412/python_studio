# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author；鸿
import requests as r
import re
import time
import os
'''请求响应'''
url = 'https://www.vmgirls.com/12353.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}
response = r.get(url,headers = headers)
html = response.text


'''解析网页'''
dir_file = re.findall('<title>(.*?) 丨 .*?</title>',html)[-1]
if not os.path.exists(dir_file):
    os.mkdir(dir_file)
urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">',html)
# print(dir_file)

'''保存图片'''
for url in urls:
    time.sleep(1)
    file_name = url.split('/')[-1]
    response = r.get(url, headers=headers)
    with open(dir_file+'/'+file_name,'wb') as f:
        f.write(response.content)
print('爬取成功')