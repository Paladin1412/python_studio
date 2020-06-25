# -*- coding: utf-8 -*-
"""
Created on Thu May  7 22:21:50 2020

@author: 17814
"""
from xpinyin import Pinyin
import requests
import re
import os
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}
city=['广州', '韶关', '深圳', '珠海', '汕头', '佛山', '江门', '湛江', '茂名', '肇庆',
      '惠州', '梅州', '汕尾', '河源', '阳江', '清远', '东莞', '中山', '东沙', '潮州',
      '揭阳', '云浮', '北京', '上海', '重庆', '天津', '杭州', '成都', '长沙', '西安']
city_weather={}
for i in range(len(city)):
    city_pinyin=Pinyin().get_pinyin(city[i],'')
    url='http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'.format(city_pinyin)
    response = requests.get(url,headers = headers)
    html = response.text
    description = re.findall('{"id":.*?,"main":".*?","description":"(.*?)","icon":".*?"}',html)
    city_weather[city[i]] = str(description)
with open('city_weather_30.txt','w') as f:
    f.write(str(city_weather))
print('文件保存成功！')