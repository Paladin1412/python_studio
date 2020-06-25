# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author；鸿
from xpinyin import Pinyin
import urllib.request as r
city=str(input('请输入需要查询的城市：'))
p = Pinyin()
city_pinyin = p.get_pinyin(city, '')
url='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'.format(city_pinyin)
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)
temp=[]
for i in data['list']:
    temp.append(i['main']['temp'])
temp=sorted(temp)
print('升序：'+str(temp))
temp.sort(reverse=True)
print('降序：'+str(temp))
