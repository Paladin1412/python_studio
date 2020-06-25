# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author；鸿
from xpinyin import Pinyin
import urllib.request as r
import json
import os
import re


def get_jsondata(city):
    p = Pinyin()
    city_pinyin = p.get_pinyin(city, '')
    url = 'http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'.format(
        city_pinyin)
    data = r.urlopen(url).read().decode('utf-8')
    data = json.loads(data)
    return data


if __name__ == "__main__":
    city_history = []
    data = {}
    if os.path.exists('.\city_temp'):
        lists = os.listdir('.\city_temp')
        if lists == []:
            print('您没有历史查询记录！')
        else:
            for i in lists:
                city_history.append(i[:2])
            print('您的历史查询城市为：' + str(city_history))
    city = str(input('请输入需要查询的城市：'))
    if not os.path.exists('.\city_temp'):
        os.mkdir('.\city_temp')
        if not os.path.exists('.\city_temp\\' + city + '.txt'):
            data = get_jsondata(city)
            with open('.\city_temp\\' + city + '.txt', 'w') as f:
                f.write(str(data))
    else:
        if not os.path.exists('.\city_temp\\' + city + '.txt'):
            data = get_jsondata(city)
            with open('.\city_temp\\' + city + '.txt', 'w') as f:
                f.write(str(data))
        else:
            with open('.\city_temp\\' + city + '.txt', 'r') as f:
                data = f.read()
                data = eval(data)
    i = 0
    j = 0
    temp = []
    while j < 5:
        ls = data['list'][i]
        if ls['dt_txt'].endswith('18:00:00'):
            j += 1
            temp.append(ls['main']['temp'])
            print(ls['dt_txt'][:-3] + city +'的温度为：' + str(ls['main']['temp']))
            print(ls['dt_txt'][:-3] + city +'的天气情况为：' + str(ls['weather'][0]['description']))
            print('-' * 50)
        i += 1

