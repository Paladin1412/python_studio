# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author；鸿
import requests
import time
import json
url ='https://api.geetest.com/refresh.php?gt=a2df2dc1b1ea8f3588d64fabd43ce43c&challenge=ef9d9c12e40b60b62646addc27b3e5fd&lang=zh-cn&type=click&callback=geetest_1590980553067'
data = requests.get(url).text
print(int(round(time.time() * 1000)))
print(data)
response = requests.get('https://cn.account.xiaomi.com/pass/v2/getCode?t=1590853431293&icodeType=register').text
response=response.replace("&&&START&&&","")
resopnse=json.loads(response)
old_challenge = resopnse['challenge']
gt=resopnse["gt"]
print(gt)