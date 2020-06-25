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
    while j < n:
        ls = data["list"][i]
        if ls["dt_txt"].endswith("18:00:00"):
            j += 1
            temp.append(ls["main"]["temp"])
        i += 1
    return temp
temp = get_temp(5)
temp_sum=sum([i for i in temp])#列表推导式
temp_mean=temp_sum/len(temp)
print(city+'未来'+str(len(temp))+'天的平均温度为：{:.2f}'.format(temp_mean))