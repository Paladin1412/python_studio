# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author；鸿
import json
import requests
import os
from wget import download

company_url=open('conpany_img.txt','r',encoding='utf-8').readlines()
for i in range(len(company_url)):
    company=json.loads(company_url[i])
    for url in company['c_img']:
        try:
            if not os.path.exists('c_imgs'):
                os.mkdir('c_imgs')
            img_filename = company['c_name']+company['c_id']+url.split('/')[-1]
            download(url,'c_imgs/'+img_filename)
            print( company['c_id'] + company['c_name'] + '下载成功...')
        except Exception as err:
            print(err.args)
            continue