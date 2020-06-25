# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author；鸿
import requests
import re
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}
def get_url(i):
    url = 'https://www.qiushibaike.com/text/page/{}/'.format(i)
    return url
def get_text_span():
    text = []
    for i in range(1,6):
        url = get_url(i)
        response = requests.get(url,headers=headers)
        html = etree.HTML(response.text)
        text_span = html.xpath('//div[@id="content"]//div[contains(@class,"content")]/span')
        for span in text_span:
            if span.xpath('text()')[0]=='查看全文':
                continue
            text.append(span.xpath('text()'))
    return text

if __name__=="__main__":
    texts = get_text_span()
    for text in texts:
        text = re.sub('<br/>|\n', '', text[0])
        str = text + '\n\n'
        with open('嗅事百科.txt','a',encoding='utf-8') as f:
            f.write(str)
    print('文件保存成功！')

# import requests
# import re
# from lxml import etree
# url = 'https://www.qiushibaike.com/text/page/1/'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
# }
# response = requests.get(url,headers=headers)
# html = response.text
# #print(html)
#
# p='''
# <div class="content">
# <span>
#
#
# (.*?)
# </span>
# '''
# result=re.findall(p,html,re.S)
# for i in result:
#     text = re.sub('<br/>|\n','',i)
#     print(text)


#text = re.findall('< a href=".*?" target=".*?" class=".*?" onclick=".*?"><div class="content"><span>(.*?)</span></div>',html,re.S)