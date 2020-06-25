# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author；鸿
import requests
import json
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'Cookie': 'cas_tgt_id=d2NjX2NyeXB0ATQxNDU1MzVGNDM0MjQzOzQzNDEzMjMwNDUzOTQyMzU0NTM5MzI0NjQxMzYzMzQzMzczNjQzMzYzNjM5NDEzNDM3MzMzNDQxMzUzMDM3MzIzMzMxNDQzNzM5NDQ0MzQzNDEzMjM2MzUzNzMzMzUzOTQ2MzgzMDM4NDI0NjM3MzU0MzQ0NDEzMjQyMzMzNTM2MzAzNTM4MzUzNDQ1NDE0NTQ2NDQzNzM3MzkzNTQyNDQzMzMzMzMzODQ2MzUzMTQ2NDYzODQzNDEzNDQxNDI0NjMyMzEzMTMzNDEzOTM2NDQ0MzM4MzkzMDQ2MzkzMjQxMzgzOTM0MzE0MjMwMzQ0NDM3MzQ0NTQ2MzA0MzQyMzYzMDM5MzYzOTMzMzg0MTQzMzAzODQ0MzEzOTQzMzQzNjMxNDE0NTMyMzgzNjM3NDMzNzMxNDIzNzM0MzMzMjM5MzYzMDMxMzE0MjMwMzQzODMyNDE0NDM2MzAzNTQzNDUzMjM0MzgzMzM5NDQ0NjQyMzI0NTM4NDEzMzQzMzUzMzMyMzAzNjM0NDIzMDM1NDE0MjMzNDQ0MTMzMzczOTMxNDE0MTM1MzMzMTMxNDE0MzQzMzQ0MjMzMzczNzM0NDMzMzMzMzYzMjQyNDIzMDM1MzMzMzQzMzUzOTM1MzIzMzM4NDY0NjQ1NDQzNjM3Mzg0MzM1Mzc0NjQ0MzczNDM5MzczNDM3MzUzNzQyMzQzNDMyMzQzMTQ0NDQ0MjQ1MzgzMDMxNDQzMTMxNDQzODQ0NDQzOTQ1Mzg0MjM2MzY0Mjs7MzEzMDMwMzAzMDsyMEY1QzY2ODc2QTdCRTc4MkUyQkU4QjBBODZBQUNDNjs1M0IwMTNCOTQ3MUQxMDc3OzMxMzQ2NDY1NjQzNzM2MzUyRDM2NjUzMDMxMkQzNDM3MzIzMTJENjIzMjMyMzMyRDMzNjUzMDMwNjEzNjM3NjIzMTY1MzY2Mzs; browserCheckResult=A; J_SESSION_ID=9ba6c241b79420ad1c1cc4ec78dda0c719fa4f59f2daf904; cftk=9K7T-O26R-V47W-8OI3-K60X-4ACW-ON58-E7YK; latestRecordTimestamp=1591457352740'
}
for i in range(1,8):
    url = 'https://119.3.187.87/label-console/rest/v2/dee636f2a4890e12aaf0c9abb5bd6ed9/datasets/fYPynhHuglQv7Jw5Fy0/workforce-tasks/NWM1JfIzvwGXuMYXCJc/data-annotations/samples?label_name=__none__&sample_state=__none__&limit=100&offset={}&process_parameter=&high_score=&low_score=&order=&worker_id=&search_conditions='.format(i)
    text = requests.get(url, headers=headers, verify=False).text
    text_json = json.loads(text)
    samples = text_json['samples']
    with open('urls.txt', 'a') as fp:
        for sample in samples:
            fp.write(sample['source'] + '\n')