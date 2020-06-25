# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author；鸿
import requests as r
from lxml import etree
url = 'https://live.aicai.com/pages/jsbf/jczq.shtml'
reponse = r.get(url)
html = etree.HTML(reponse.text)
table_head_tds = html.xpath('//table[@id="jq_jsbf_body"]/thead/tr/td')
print(table_head_tds)
teble_head = []
for td in table_head_tds[:-1]:
    text = td.xpath('text()')
    if text==[]:
        text = td.xpath('./select/option[@value="sp_val"]/text()')
    teble_head.append(text[0])
print(teble_head)