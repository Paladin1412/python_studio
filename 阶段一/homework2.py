# -*- coding: utf-8 -*-
"""
Created on Thu May  7 08:26:35 2020

@author: 刘伟鸿
"""
weather={
    'condition':['雷阵雨','晴天','小雨','阴天','阵雨转晴','多云','阵雨'],
    'temperature_min':[26,26,25,26,26,27,27],
    'temperature_max':[31,30,31,32,32,31,31],
    'week':['一','二','三','四','五','六','日']
}
for i in range(0,7):
    print('星期'+weather['week'][i]+'的温度为:'+str(weather['temperature_min'][i])+'~'+
          str(weather['temperature_max'][i])+'  天气为：'+weather['condition'][i])
input('输入任意键结束...')