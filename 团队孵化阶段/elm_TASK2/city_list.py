# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author；鸿
import requests
from xpinyin import Pinyin
from json import loads
def latlong():
    '''返回城市的经纬度'''
    url = 'https://shadow.elemecdn.com/lib/city-list@0.0.3/city_list.json'
    response = loads(requests.get(url).text)
    city_name = str(input('请输入城市名称（中文）：'))
    city_pinyin=Pinyin().get_pinyin(city_name,'')
    num = response['alphabet'].index(chr(ord(city_pinyin[0])-32))
    cities = response['cityList'][num]['cities']
    for city in cities:
        if city['name'] == city_name:
            return city['latitude'],city['longitude']