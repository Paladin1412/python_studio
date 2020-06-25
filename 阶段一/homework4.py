# -*- coding: utf-8 -*-
"""
Created on Thu May  7 20:36:41 2020

@author: 17814
"""

import urllib.request as r
url='http://api.openweathermap.org/data/2.5/weather?q=shenzhen&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)
print(data['main'])
print('深圳'+'的天气情况为：'+data['weather'][0]['description'])
print('深圳'+'的温度为：'+str(data['main']['temp']))
print('深圳'+'的天气气压为：'+str(data['main']['pressure']))