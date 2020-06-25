# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author；鸿
import requests
import json
#
# response = requests.post('https://proxy.qg.net/allocate?Key=00F1C1E4FF537E88')
# print(response.text)
# # str_s = '{"Code":0,"TaskID":"5BYwJ6rcyzcJtcf5","Num":1,"Data":[{"IP":"117.26.40.113","port":"60221","deadline":"2020-06-09 08:11:25","host":"117.26.40.113:60221"}]}'
# text_json = json.loads(str_s)
#
#
# #目标请求地址
# targetUrl = "https://www.baidu.com/s?wd=ip地址查询"
#
# #代理服务器
# proxyHost = text_json['Data'][0]['IP'] #ip地址
# proxyPort = text_json['Data'][0]['port'] #端口号
#
# # proxyMeta = "http://%(host)s:%(port)s" % {
# # "host" : proxyHost,
# # "port" : proxyPort,
# # }
#
# #pip install -U requests[socks] socks5代理
# proxyMeta = "socks5://%(host)s:%(port)s" % {
# "host" : proxyHost,
# "port" : proxyPort,
# }
#
# proxies = {
# "http" : proxyMeta,
# }
#
# resp = requests.get(targetUrl, proxies=proxies)
# print(resp.status_code)
# print(resp.content.decode('utf-8'))

from fake_useragent import UserAgent
url='https://h5.ele.me/restapi/eus/login/mobile_send_code'
data={
    'mobile':'17637242350',
    'scf':'ms'
}
headers={
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'content-length': '72',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': '__wpkreporterwid_=52a4dd0e-f0e1-45f9-393d-9914d1e2f80d; ubt_ssid=mqmrh8166zjhen0ylww5cu3k9ppdre2l_2020-06-07; perf_ssid=zpq5i8uj861pb5b5mj7t9d1ees1qweyy_2020-06-07; ut_ubt_ssid=blk5zezfz4t1hu1redces0g8j56w11tg_2020-06-07; cna=e9pXF21sJigCAXF2DXOwC4iK; _bl_uid=Utk6wbF644Iremvn5zzt35k66e83; _utrace=28fe3bba1c0ce75484a3e70f9f99d0e3_2020-06-07; _samesite_flag_=true; t=b86f23f7ee94141c087ef5d6f60ac6b5; _tb_token_=ed355b1388036; csg=09484496; t_eleuc4=id4=0%40BA%2FvuHCrrRtQk0MqN0A8ZvMLx537DUeqNxrjZQ%3D%3D; munb=2206579483915; track_id=1591519662|1007f241d03ec6fad54df7f148fd7ac1b04c216fcbaff38b51|ff7c1e2216e2db4412046bcf836fcbf7; tzyy=9933c52edbe4e66dbe32ecc02f6db1fa; cookie2=100cc461ef8464a5e59d11b41db80870; l=eBOWF_cmQVTtCnFKBO5Zhurza77t3IOXhsPzaNbMiInca1yA_hL2aNQDdKL98dtjgtfvxeKPOzL1BRn2JxaU-xaVX9zbTF6ZmYvvF; USERID=1000081304180; UTUSER=1000081304180; SID=CQAAAOjZfap06gAEAABUbGXlEAwxTzSc-Df4jV78HQ48Ise0o10lLnzh; ZDS=1.0|1591571541|WGdv8IeEintFPiD2CWLtgO2Unrdq32nJYQGsZyYw/NostACLD6dj0b4rGRuTyYARdoAGQhOWNRu5zJgHLoGlhw==; x5check_ele=YbcTUKJkbaNwLZWZBOWNnctwWElpmGQZ6Nf7s6mEM6E%3D; x5sec=7b227466653b32223a223361663166356630396339343136376536623566396162323234323165663266434c577739765946454d7952683436583262765176674561447a45774d4441774f44457a4d4451784f4441374d673d3d227d; isg=BMrKpE9UoNjpUix1GcKiVYxdG7Bsu04VQJF0XVQDdp2oB2rBPEueJRBxE3Xb98at',
    'origin': 'https://h5.ele.me',
    'referer': 'https://h5.ele.me/login/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Mobile Safari/537.36',
    # x-font-version: bf567591c8124d0bbd5642aaac739edd
    'x-captcha-platform': '1',
    'x-captcha-session-id': '01kFEDk-kqcMrI7gDGQ52H7mgoz1AOz0RGOKSSD4n_A4Sf6tl3P4-7baYwdvUZeAunD9bU_PCl1vapuvprHnGq5uy5tCnEO9h2-vlgYxj5u3kjftngikzTT5sGq4pMdRq_HB0LWJrnf9dDKLnBxky5Fe1qJKQNPOCRo-MgoGBh9VSo4dNgSp5dx50HzITs0O0E',
    'x-captcha-sig': '05vFSFBfoiapFXEtEHvSpjr4Z8cUsWdp7nZeC0Sgtz5ObH0fYaR8P_FuPBbex74yIjMBAw0nmYqNB84cTP3n5rPRKCrxGrm78sL5GnT9T4ToghFIgwcQ0_Do9oaCLq19ZK9mKAv8xMNmwFF9-D5OOF_-lXhk0fjKDTKDLBoNPkBfrmCCYe6VJOfVewuB9A3LTCMhbqra_qOIe6p_i8oyvJ7DBZ4mrl8DoVPxfnA4AHaiOQyqZcdpzdzm8LvjoQUrhpDsIGmZMGguU5nxu7e281wgUZcv7Jv6xJtbdw_X3w6W3M8nL1WMXyaD0tycQqQIxsbbAJAbtNAyuryYyorg-6G_XHxPXmJY_XI3QBkBoAilN-0IBLL5lE11dXPGUs1fjl2DIxWtInidrV3qgLOgPqnWoYZtkniuYMQ9p_2GaWmoE',
    'x-captcha-token': 'CF_APP_ELE:1591585595135:0.9711154330264884',
    'x-fy-umt': 'T50ED07071B31124EFE950885DCD386EC5ED034EC8298A4DA971913EC5B',
    'x-shard': 'loc=116.322056,39.89491',
    'x-ua': 'RenderWay/H5 AppName/wap',
    'x-uab': '124#kzpb0J7PxG0xA1GZ1JQ/LeKVVpRFx4SskGpMsoiJW3tTEF49ilorncB9UvaXj4OcvUs9XOLX0ssWXgR4fILgXa8/HzcksNdp+RNSxYk1+kicAPFUODuQg9PjF24K6J6TNtRQthzzrE0mBkD6agYB6yd/j2jHMH1vS+QekrxhveLvB/hgVEQOA/kFrGrcrK37JKT3qQpWMnhNJs21d+wXnNLr5pfbBVtjz1eeLccUxNeucmPXt8ZkpSqYQu6D6uGUpKCTKOKhXpelnxUZMMsovTFHnzV3Nsr4f4jT18rDWVJ7KZ2ZlMan6KvBIZYLlm92HmRYwlzCgTSd7ZeZlULJ4W4D7C9plmI4mfWZJqot6w1o1nIelUX2g7vtIn/pbw/2m4WeIqXLg5Sd1Z2elMXng7OBInYLlwYnH4IxS8aVg5JT1nIZlQ0ZH3b1IIKLlmbnmfWeI8HZ/+HwCoEJNONNH4vYVBDtP/+52Y8Y1iCpilqKJE+vwAoO8vitAABWzUbNQtq4jCzw7cc/J6go/FeQIB8cwKiv4rm7hexXHwaCy6aFjNI+lq09C6lPbCqLEXMhN7YOW40bwsPXLTG30f8cuOIO/uikrtJLzyH5zsAd63LQRTr1TJOtEKnL9yFFaweKc66aydhZBUHAPnD3+T9PW57Se2Lr/FHBJiBIINf6VGjas8LY0P7Cg/WSabzHu1NjKtrhzGsVYjdN0cIp/+utySZe6WZjrdQFcEot/IT1xhxM0M/4/viCbSE5mjwCGqEqxaap7rZqrn0tF+/Xs/Cu+w1/sSzWUPb4MaDo9h+GeGOAJ7Y0VRKvvRMhHJqTx106d80bYhgR0RXE6uemyYXBIEVQOka4IJink+vulswn5QF9IdDXx8spNoyDhMYnfzASOYCsjFu5DkINs4gwZwbv5NRk7vm52I6wvD+LKhr2D/khZusdvQe5ml+FjTGacyEVNWpeoirbUgBz0urU8T1Wb01kL6Ky5GxMyuUu2DjuWbcNgo0nzrKcU8PtaGeqRpBI31hoRfzBQBrW3Brggi9hvnT1ao28kygqevcvvG6CJAfhlfAgrDQ4dKyyNj/zcQ0sOPSBnMFFjtbcca9FdWVH9IuWQqoq56y0v2Njwoj0aLMhCwm1hIdkM5/e9qZfnJF5dXiRhVW7C+vgmTOCAxvu+LE8EN1dRK70eagm8JluHDW5rzfITx0fPpPSc4koaxnCVbnyYk=='
}
reponse=requests.post(url,headers=headers,data=data)
print(reponse)
# validate_token=json.loads(reponse.text)['validate_token']
# validate_code=input()
# # 登陆验证的url
# url='https://h5.ele.me/restapi/eus/login/login_by_mobile'
# data={
#     'mobile':'17637242350',
#     'scf':'ms',
#     'validate_code':validate_code,
#     'validate_token':validate_token,
# }
#
# reponse=requests.post(url,headers=headers,data=data)
# cookie=requests.utils.dict_from_cookiejar(reponse.cookies)
