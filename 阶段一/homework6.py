# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author；鸿
import urllib.request as r
url='http://api.openweathermap.org/data/2.5/forecast?q=shenzhen,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)
i=0
j=0
temp=[]
while j<5:
    ls = data['list'][i]
    if ls['dt_txt'].endswith('18:00:00'):
        j+=1
        temp.append(ls['main']['temp'])
        print(ls['dt_txt'][:-3]+'深圳的温度为：'+str(ls['main']['temp']))
        print(ls['dt_txt'][:-3]+'深圳的最低温度为：' + str(ls['main']['temp_min']))
        print(ls['dt_txt'][:-3]+'深圳的最高温度为：' + str(ls['main']['temp_max']))
        print(ls['dt_txt'][:-3]+'深圳的天气情况为：' + str(ls['weather'][0]['description']))
        print(ls['dt_txt'][:-3]+'深圳的气压为：' + str(ls['main']['pressure']))
    i+=1
print('-'*10+'英文版'+'-'*10)
i=0
j=0
while j<5:
    ls = data['list'][i]
    if ls['dt_txt'].endswith('18:00:00'):
        j+=1
        print(ls['dt_txt']+'深圳的温度为：'+str(ls['main']['temp']))
        print(ls['dt_txt']+'深圳的最低温度为：' + str(ls['main']['temp_min']))
        print(ls['dt_txt']+'深圳的最高温度为：' + str(ls['main']['temp_max']))
        print(ls['dt_txt']+'深圳的天气情况为：' + str(ls['weather'][0]['main']))
        print(ls['dt_txt']+'深圳的气压为：' + str(ls['main']['pressure']))
    i+=1
print('*'*20+'气温折线图'+'*'*20)
for i in range(8,13):
    if i<10:
        print('05-0'+str(i)+'-'*int(temp[i-8])+str(temp[i-8]))
    else:
        print('05-' + str(i) + '-' * int(temp[i-8]) + str(temp[i-8]))