# -*- coding: utf-8 -*-
"""
Created on Fri May  8 09:57:05 2020

@author: 17814
"""

from xpinyin import Pinyin
import urllib.request as r
if __name__=="__main__":
    city=str(input('请输入需要查询的城市：'))
    p = Pinyin()
    city_pinyin = p.get_pinyin(city, '')
    url='http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'.format(city_pinyin)
    data=r.urlopen(url).read().decode('utf-8')
    import json
    data=json.loads(data)
    print(city+'的温度为：'+str(data['main']['temp'])+'℃')
    print(city+'的天气情况为：'+str(data['weather'][0]['description']))
    print(city+'的气压为：'+str(data['main']['pressure'])+'P')
    input("Prease <enter>")