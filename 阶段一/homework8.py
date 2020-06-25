# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author；鸿
import urllib.request as r
city=str(input('请输入要查询的城市：'))
url='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'.format(city)
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)
def weather(city):
    i=0
    j=0
    temp=[]
    while j<5:
        ls = data['list'][i]
        if ls['dt_txt'].endswith('18:00:00'):
            j+=1
            temp.append(ls['main']['temp'])
            print(ls['dt_txt'][:-3]+city+'的温度为：'+str(ls['main']['temp']))
            print(ls['dt_txt'][:-3]+city+'的最低温度为：' + str(ls['main']['temp_min']))
            print(ls['dt_txt'][:-3]+city+'的最高温度为：' + str(ls['main']['temp_max']))
            print(ls['dt_txt'][:-3]+city+'的天气情况为：' + str(ls['weather'][0]['description']))
            print(ls['dt_txt'][:-3]+city+'的气压为：' + str(ls['main']['pressure']))
        i+=1
weather(city)

