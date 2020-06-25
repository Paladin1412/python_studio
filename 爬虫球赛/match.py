# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author；鸿
import requests
from lxml.etree import HTML
import json
import re
import demjson
from fake_useragent import UserAgent
from retrying import retry

@retry(stop_max_attempt_number=2, wait_random_min=1000, wait_random_max=2000)
def get_response(url,headers):
    return requests.get(url,headers)

@retry(stop_max_attempt_number=2, wait_random_min=1000, wait_random_max=2000)
def get_sp_response(url,headers):
    return requests.get(url,headers)

def Date(startyear,endyear):
    date = []
    month_day = [31,28,31,30,31,30,31,31,30,31,30,31]
    for year in range(startyear,endyear+1):
        if year%400==0:
            month_day[1]=29
        elif year%4==0 and year%100!=0:
            month_day[1]=29
        else:
            month_day[1]=28
        for month in range(1,13):
            for day in range(1,month_day[month-1]+1):
                if month<=9:
                    month_s='0'+str(month)
                else:
                    month_s = str(month)
                if day<=9:
                    day_s='0'+str(day)
                else:
                    day_s = str(day)
                date.append(str(year)+'-'+month_s+'-'+day_s)
    return date

def get_data(date,all_match_des,err_data_list,err_url_list):
    headers={
        'headers':UserAgent().random
    }
    flag = 0
    url = 'https://live.aicai.com/jsbf/timelyscore!dynamicMatchDataForJczq.htm?dateTime={}'.format(date)
    response = get_response(url,headers)
    html = response.text
    if '访问失败！'in str(html):
        print(date+'无球赛!')
    else:
        data = json.loads(html)
        data_str = data['result']['jsbf_matchs']
        #id
        match_id = re.findall('<span id=\"jq_league_matchTime_(.*?)\">.*?<\/span>',data_str,re.S)
        #星期
        data_weekIndex = re.findall('<td class="txtbbb xx_bg_weekIndex" id="jq_matchindex_.*?_td">(.*?)</td>',data_str,re.S)
        #联赛timelyscore
        league = re.findall('<td style="color:#fff; background:#.*?" id="jq_league_.*?_td" status="0">(.*?)</td>',data_str,re.S)
        #时间
        date_matchTime = re.findall('<span id="jq_league_matchTime_.*?">(.*?)</span>',data_str,re.S)
        # 球队 & 比分
        data_rel = re.findall('<span id=\"jq_status_.*?\" rel=\".*?\">(.*?)<\/span>', data_str, re.S)
        data_team_1 = re.findall('<span id="jq_match_hostteam_.*?_span">(.*?)</span>', data_str, re.S)
        data_team_2 = re.findall('<span id="jq_match_guestteam_.*?_span">(.*?)</span>', data_str, re.S)
        data_timelyscore = re.findall('<a id="jq_timelyscore_.*?" class="wcbf_color">(.*?)</a>', data_str, re.S)
        if '取消' in data_rel:
            cancel_index = data_rel.index('取消')
            data_timelyscore.insert(cancel_index, '-')
        if '延期' in data_rel:
            cancel_index = data_rel.index('延期')
            data_timelyscore.insert(cancel_index, '-')
        if '夭折' in data_rel:
            cancel_index = data_rel.index('夭折')
            data_timelyscore.insert(cancel_index, '-')
        if '未开赛' in data_rel:
            cancel_index = data_rel.index('未开赛')
            data_timelyscore.insert(cancel_index, '-')
        data_allscore = []
        for i in range(len(data_team_1)):
            str_s = data_team_1[i] + ' ' + data_timelyscore[i] + ' ' + data_team_2[i]
            data_allscore.append(str_s)
        # 半场比分data_halfscore
        temp = re.findall('<span class="red">(.*?)</span>', data_str, re.S)
        data_halfscore = []
        for i in range(len(temp)):
            if ':' in temp[i]:
                data_halfscore.append(temp[i])
        if '取消' in data_rel:
            cancel_index = data_rel.index('取消')
            data_halfscore.insert(cancel_index, '-')
        if '延期' in data_rel:
            cancel_index = data_rel.index('延期')
            data_halfscore.insert(cancel_index, '-')
        if '夭折' in data_rel:
            l_index = data_rel.index('夭折')
            data_halfscore.insert(cancel_index, '-')
        if '未开赛' in data_rel:
            l_index = data_rel.index('未开赛')
            data_halfscore.insert(cancel_index, '-')
        #让球
        data_letpoint = re.findall('<td id="jq_rangqiu_.*?" letPoint="(.*?)"><strong class="txt_333">',data_str,re.S)
        date_last = date.replace('-','')[2:]
        try:
            url_js = 'https://live.aicai.com/static/no_cache/jc/zcnew/data/hist/{}zcRefer.js'.format(date_last)
            text = get_sp_response(url_js,headers).text
            text_json = demjson.decode(text)
        except Exception as err:
            flag = 1
            jczq_spf_gd = ['--', '--', '--']
            jczq_xspf_gd = ['--', '--', '--']
            print('{}日竞彩sp解析失败... 原因为{} url:{}'.format(date,str(err.args),url_js))
            err_url_list.append(['{}日竞彩sp解析失败... 原因为{} url:{}'.format(date,str(err.args),url_js)])
        for i in range(len(match_id)):
            try:
                if flag==0:
                    jczq_xspf_gd = text_json[match_id[i]]['sp']
                    jczq_spf_gd = text_json[match_id[i]]['sp']
                    if jczq_xspf_gd == {}:
                        jczq_xspf_gd = ['--','--','--']
                    elif jczq_spf_gd == {}:
                        jczq_spf_gd = ['--','--','--']
                    else:
                        if  not 'jczq_xspf_gd' in jczq_xspf_gd:
                            jczq_xspf_gd = ['--','--','--']
                        else:
                            jczq_xspf_gd = jczq_xspf_gd['jczq_xspf_gd'].split('-')
                        if  not 'jczq_spf_gd' in jczq_xspf_gd:
                            jczq_spf_gd = ['--','--','--']
                        else:
                            jczq_spf_gd = jczq_spf_gd['jczq_spf_gd'].split('-')
                match_des = {
                    'match_id':match_id[i],
                    'data_weekIndex':data_weekIndex[i],
                    'league':league[i],
                    'date_matchTime':date_matchTime[i],
                    'data_allscore':data_allscore[i],
                    'data_halfscore':data_halfscore[i],
                    'data_letpoint':'0:'+data_letpoint[i],
                    'jczq_xspf_gd':jczq_xspf_gd,
                    'jczq_spf_gd':jczq_spf_gd
                }
                all_match_des.append(match_des)
                print('{}日第{}条数据获取成功！'.format(date, i + 1))
            except Exception as e:
                print('{}日第{}条数据获取失败... 原因为:{}'.format(date,i+1,str(e.args)))
                err_data_list.append(['{}日第{}条数据获取失败... 原因为:{}'.format(date,i+1,str(e.args))])

def run():
    dates = Date(2014,2020)
    date_count = dates[0].split('-')[0]
    err_date_f = open('err_data_list_{}.text'.format(date_count), 'a', encoding='utf-8')
    err_url_f = open('err_url_list_{}.text'.format(date_count), 'a', encoding='utf-8')
    all_match_des_f = open('all_match_des_{}.text'.format(date_count), 'a', encoding='utf-8')
    for date in dates:
        all_match_des = []
        err_data_list = []
        err_url_list = []
        if date.split('-')[0] > date_count:
            err_date_f.close()
            err_url_f.close()
            all_match_des_f.close()
            date_count = date.split('-')[0]
            err_date_f = open('err_data_list_{}.text'.format(date_count), 'a', encoding='utf-8')
            err_url_f = open('err_url_list_{}.text'.format(date_count), 'a', encoding='utf-8')
            all_match_des_f = open('all_match_des_{}.text'.format(date_count), 'a', encoding='utf-8')
        get_data(date,all_match_des,err_data_list,err_url_list)
        if all_match_des!=[]:
            str_all_match_des = str(all_match_des) + '\n'
            all_match_des_f.write(str_all_match_des)
        if err_data_list != []:
            str_err_date_list = str(err_data_list) + '\n'
            err_date_f.write(str_err_date_list)
        if err_url_list != []:
            str_err_url_list = str(err_url_list) + '\n'
            err_url_f.write(str_err_url_list)
        date_count = date.split('-')[0]


if __name__ == '__main__':
    run()