#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 05:19:54 2020

@author: linhaohong
"""

import requests
from lxml.etree import HTML
import re
import os
import json
from fake_useragent import UserAgent
from retrying import retry

def get_url():
    '''获取文件中的所有url'''
    with open('company_list.json', 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
    url_ls = []
    for url in data:
        url_ls.append(url[-1])
    return url_ls

@retry(stop_max_attempt_number=2, wait_random_min=1000, wait_random_max=2000)
def get_response(url,headers):
    return requests.get(url, headers=headers).content.decode('gbk')

def get_company_news(company,url_ls,i,error_list):
    '''获取第i个公司的介绍'''
    headers = {
        'User-Agent': UserAgent().random
    }
    compare_news=[]#公司介绍
    url = url_ls[i]
    flag = 1
    try:
        response = get_response(url,headers)
        a = re.compile('class="con_txt">(.*?)</div>',re.S).findall(response)
        a[0] = a[0].replace("<br>"," ").replace("&nbsp;","")#公司简介
        a1 = re.compile('<h1 title=(.*?)>',re.S).findall(response)#公司名称
        a2 = re.compile('<p class="fp">.*?<span class="label">.*?</span>(.*?)</p>',re.S).findall(response)#公司地址
        a3 = re.compile('<p class="fp tmsg"><span class="label">.*?</span><span>(.*?)</span>',re.S).findall(response)#公司官网网址
        a2_str="".join(a2)
        a3_str="".join(a3)
        compare_news.append([a[0]])
        compare_news.append([a2_str.replace(" ","")])
        if [a3_str.replace(" ","")]==[""]:
            compare_news.append(['None'])
        else:
            compare_news.append([a3_str.replace(" ","")])
        print('{}详情获取成功...'.format(company))
    except Exception as e:
        print('{}详情获取失败... 原因为:{}'.format(company,e))
        error_list.append([url, "'序号':{}".format(i), e])
        flag = 0
    return compare_news,flag

def read_company_list():
    with open('company_list.json','r',encoding='utf-8') as f:
        data = json.loads(f.read())
    return data

def supplement_company_list(json_data,id):
    with open('company_info_list{}.json'.format(id),'w',encoding='utf-8') as f:
        f.write(json.dumps(json_data, ensure_ascii=False))
    print('company_info_list{}.json'.format(id), '写入成功...')

def write_error_company_list(json_data, id):
    with open('error_company_list{}.json'.format(id), 'w', encoding='utf-8') as f:
        f.write(json.dumps(json_data, ensure_ascii=False))
    print('error_company_list{}.json'.format(id), '写入成功...')

def company_info(start,end,id):
    url_ls = get_url()
    error_list = []
    data = read_company_list()
    for i in range(start,end):
        compare_news, flag = get_company_news(url_ls,i,error_list)
        if flag==1:
            data[i].append(compare_news)
        else:#如果flag改变了，说明出现了错误
            continue
    supplement_company_list(data,id)
    if error_list!=[]:
        write_error_company_list(error_list,id)

def run():
    task = read_task_json()
    company_info(task["start"], task["start"] + task["amount"], task["ID"])

if __name__ == '__main__':
    # run()
    company_info(0,20,1)
















































