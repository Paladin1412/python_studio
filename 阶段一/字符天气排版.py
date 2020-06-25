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
    temp_max=[]
    temp_min=[]
    weather=[]
    date=[]
    while j < n:
        ls = data["list"][i]
        if ls["dt_txt"].endswith("18:00:00"):
            j += 1
            temp.append(ls["main"]["temp"])
            temp_min.append(ls["main"]["temp_min"])
            temp_max.append(ls["main"]["temp_max"])
            date.append(ls["dt_txt"][5:10])
            weather.append(ls["weather"][0]["main"])
        i += 1
    return temp,temp_min,temp_max,date,weather
temp,temp_min,temp_max,date,weather = get_temp(5)
print('┌'+'-'*82+'┐')
print('│'+' '*22+'Welcome to the weather inquiry system!'+' '*22+'│')
print('├'+'-'*82+'┤')
print('│'+' '*4+'date'+' '*4+'│'+' '*4+'city'+' '*4+'│'+' '*4+'temp'+' '*4+'│'+' '*3+'temp_min'+' '*3+'│'+' '*3+'temp_max'+' '*3+'│'+' '*3+'weather'+' '*3+'│')
print('├'+'-'*82+'┤')
for i in range(5):
    print('│'+' '*3+date[i]+' '*4+'│'+' '*3+str(city_pinyin)+' '*(9-len(str(city_pinyin)))+'│'+' '*4+str(temp[i])+' '*(8-len(str(temp[i])))+'│'+' '*4+str(temp_min[i])+' '*(10-len(str(temp_min[i])))+'│'+' '*5+str(temp_max[i])+' '*(9-len(str(temp_max[i])))+'│'+' '*3+str(weather[i])+' '*(10-len(str(weather[i])))+'│')
print('└'+'-'*82+'┘')