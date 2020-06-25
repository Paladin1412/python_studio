# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author；鸿
import requests
from lxml.etree import HTML
from wget import download
import urllib.request as r
import os
import time
import re
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}


# response = requests.get(url, headers=headers)
# html = response.text
# html = HTML(html)
# html_xpath = '//*[@id="pic-detail"]/div/div[2]/div[2]/ul/li/div/div/a[.]/img/@data-backup'
# html_url = html.xpath(html_xpath)
# for url in html_url:
#     img_filename = 'doutula/{}'.format(url.split('/')[-1])
#     download(url,img_filename)
#     #r.urlretrieve(url,img_filename)#下载方式


'''1.下载所有网页字符串内容-保存到文件中'''
def get_html(url,i):
    response = requests.get(url, headers=headers)
    html = response.text
    if not os.path.exists('doutula_html'):
        os.mkdir('doutula_html')
    with open('doutula_html/{}.html'.format(i), 'w',encoding='utf-8') as f:
        f.write(html)
    print('{}.html  下载成功...'.format(i))

def get_all_html(url,n):
    for i in range(1,n+1):
        # time.sleep(1)
        get_html(url.format(i),i)

url = 'https://www.doutula.com/photo/list/?page={}'
get_all_html(url,3350)

'''2.通过提取所有要下载的图片地址-保存到文件中'''
def get_all_url(begin,end,count):
    for i in range(begin,end+1):
        with open('doutula_html/{}.html'.format(i),'rb') as f:
            html = f.read()
        html = HTML(html)
        html_xpath = '//*[@id="pic-detail"]/div/div[2]/div[2]/ul/li/div/div/a[.]/img/@data-backup'
        url_ls = html.xpath(html_xpath)
        # html_img_xpath = '//*[@id="pic-detail"]/div/div[2]/div[2]/ul/li/div/div/a[.]/p/text()'
        # html_img_filename = html.xpath(html_img_xpath)
        if not os.path.exists('doutula_url'):
            os.mkdir('doutula_url')
        for url in url_ls:
            # filename_suffix = url.split('.')[-1]
            str = url+'\n'
            with open('doutula_url/{}_url.txt'.format(count),'a',encoding='utf-8') as f:
                f.write(str)
        print('{}.html_url获取成功...'.format(i))
        if i==3444:
            break;
for i in range(int(3444/50)+1):
    get_all_url(i*50+1,(i+1)*50,i)
'''3.通读取文件中的地址下载所有图片-到文件中'''
for i in range(63,69):
    f = open('doutula_url/{}_url.txt'.format(i),'r',encoding='utf-8')
    urls = f.readlines()
    f.close()
    for j in range(len(urls)):
        url_list = urls[j].replace('\n','')
        if not os.path.exists('doutula_img'):
            os.mkdir('doutula_img')
        img_filename = 'doutula_img/{}'.format(url_list.split('/')[-1])
        if img_filename.endswith('.null'):
            img_filename = re.sub('.null','.jpg',img_filename)
        r.urlretrieve(url_list,img_filename)#下载方式
        print('{}_url.txt ---{}下载成功...'.format(i,url_list.split('/')[-1]))
    print('{}_url.txt 下载完毕！'.format(i))
'''4.'''