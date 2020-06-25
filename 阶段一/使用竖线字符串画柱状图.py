# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author；鸿
from xpinyin import Pinyin
import json
import urllib.request as r
city = str(input("请输入需要查询的城市："))
p = Pinyin()
city_pinyin = p.get_pinyin(city, "")
url = "http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric".format(city_pinyin)
data = r.urlopen(url).read().decode("utf-8")
data = json.loads(data)

def get_temp(n):
    i = 0
    j = 0
    temp = []
    date=[]
    while j < n:
        ls = data["list"][i]
        if ls["dt_txt"].endswith("18:00:00"):
            j += 1
            temp.append(ls["main"]["temp"])
            date.append(ls["dt_txt"][5:10])
        i += 1
    return temp,date

temp,date = get_temp(5)
max_temp=max(temp)
print('-'*15+city+'未来五天天气柱状图'+'-'*15)
for i in range(int(max_temp)):
    for j in range(5):
        if(temp[j]<max_temp):
            print(' '*10,end='')
        else:
            print(' '*4+'=='+' '*4,end='')
    max_temp-=1
    print('')
print('-'*50)
for i in range(len(date)):
    print(' '*1+str(temp[i])+'℃'+' '*3,end='')
print('')
for i in range(len(date)):
    print(' '*3+date[i]+' '*2,end='')

