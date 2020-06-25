# -*- coding: utf-8 -*-
"""
Created on Thu May  7 22:21:50 2020

@author: 17814
"""
import geopandas as gpd
import warnings
import matplotlib.pyplot as plt
from xpinyin import Pinyin
import urllib.request as r
import json
import pandas as pd
warnings.filterwarnings('ignore')#防止报错
plt.rcParams['font.sans-serif']=['SimHei']#中文显示
plt.rcParams['axes.unicode_minus'] = False

GuangDong_spatial = gpd.GeoDataFrame.from_file(r'C:\Users\17814\Desktop\GuangDong.json')
city_temp=[]
for i in range(22):
    city=GuangDong_spatial['name'][i][:2]
    city_pinyin=Pinyin().get_pinyin(city,'')
    url='http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'.format(city_pinyin)
    data=r.urlopen(url).read().decode('utf-8')
    data=json.loads(data)
    city_temp.append(float(data['main']['temp']))
GuangDong_spatial['温度']=city_temp
plt.figure(figsize=(20,20))
plt.title('2020-5-10 广东省温度情况', fontsize = 20)
GuangDong_spatial.plot(ax=plt.subplot(1,1,1), alpha=1,edgecolor='k', linewidth = 0.5,legend=True, column='温度', cmap = 'Reds')
# 设置网格线
plt.grid(True,alpha=0.5)
plt.savefig('figpath.png', dpi=400, bbox_inches='tight')#保存图片
plt.show()