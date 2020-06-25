# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author；鸿
import re
import urllib.request as r
url='http://api.openweathermap.org/data/2.5/forecast?q=zhuhai,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)


html = str(data['list'])
temp = re.findall("'main': {'temp': (.*?), 'feels_like': .*?, 'temp_min': .*?, 'temp_max': .*?, 'pressure': .*?, 'sea_level': .*?, 'grnd_level': .*?, 'humidity': .*?, 'temp_kf': .*?}",html)

print(temp)

