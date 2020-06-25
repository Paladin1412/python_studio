# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author；鸿
import matplotlib.pyplot as plt
import numpy as np
import urllib.request as r
from xpinyin import Pinyin
import warnings
import json
warnings.filterwarnings("ignore")  # 防止报错
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 中文显示
plt.rcParams["axes.unicode_minus"] = False
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
    date = []
    while j < n:
        ls = data["list"][i]
        if ls["dt_txt"].endswith("18:00:00"):
            j += 1
            temp.append(ls["main"]["temp"])
            date.append(ls["dt_txt"][5:10])
        i += 1
    plt.plot(date, temp, ls="-", lw=2, label=city + "未来" + str(n) + "天温度情况")
    plt.ylim(24, 34)
    plt.legend()
    plt.show()


get_temp(5)
