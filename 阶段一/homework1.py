# -*- coding: utf-8 -*-
"""
Created on Wed May  6 17:24:03 2020

@author: 刘伟鸿
"""
condition=['雷阵雨','晴天','小雨','阴天','阵雨转晴','多云','阵雨']
temperature=[26,26,25,26,26,27,27]
week=['一','二','三','四','五','六','日']
i=1
while i<=7:
    print('星期'+week[i-1]+'的温度为：'+str(temperature[i-1])+'℃  '+'天气为：'+condition[i-1])
    i+=1
sum=0.0
j=1
while j<=7:
    sum+=float(temperature[j-1])
    j+=1
print('一周的平均温度为:{:.2f}'.format(sum/7))
