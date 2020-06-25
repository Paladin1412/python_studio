# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author；鸿
all_url = []
for a in range(1,12):
    with open('image_url{}.txt'.format(a),'r')as f:
        data = f.readlines()
    data = list(set(data))
    all_url.extend(data)
    print(len(data))

all_url = list(set(all_url))
print(len(all_url))
for url in all_url:
    with open('all_url1.txt','a')as f:
        f.write(url)