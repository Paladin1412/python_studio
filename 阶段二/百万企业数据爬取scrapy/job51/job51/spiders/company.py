# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
import json
from math import ceil
company_f = open('conpany4000000-4500000.txt','a',encoding='utf-8')
# job_f = open('job1.txt','a',encoding='utf-8')
companyid_f = open('conpanyid25.txt','w',encoding='utf-8')
class CompanySpider(scrapy.Spider):
    name = 'company'
    allowed_domains = ['51job.com']
    start_urls = ['https://jobs.51job.com/all/co{}.html'.format(i) for i in range(4000000,4500001)]

    def get_company(self,selector):
        Xpath = [
            ('//*[@id="hidCOID"]/@value', 'c_id'),
            ('/html/body/div[2]/div[2]/div[2]/div/h1/@title', 'c_name'),
            ('/html/body/div[2]/div[2]/div[2]/div/img/@src', 'c_logo'),
            ('/html/body/div[2]/div[2]/div[2]/div/p[1]/@title', 'c_tst'),
            ('/html/body/div[2]/div[2]/div[3]/div[1]/div/div[1]/div[1]/div', 'c_describe'),
            ('/html/body/div[2]/div[2]/div[3]/div[2]/div/p[1]/text()', 'c_address'),
            ('/html/body/div[2]/div[2]/div[3]/div[2]/div/p[2]/span[2]/text()', 'c_office_website'),
            ('//*[@id="hidTotal"]/@value', 'c_pub_jobcount')
        ]
        companyj = {}
        for xpath, key in Xpath:
            try:
                if key == 'c_describe':
                    companyj[key] = str(selector.xpath(xpath).xpath('string(.)').extract()[-1]).replace(' ','').replace('\xa0','')
                else:
                    companyj[key] = str(selector.xpath(xpath).extract()[-1]).replace(' ','').replace('\xa0','')
            except Exception as e:
                # print(e.args)
                print('对不起，您选择的公司不存在或者已经过期!')
                companyj[key] = 'None'
        return companyj

    def get_jobs(self,selector,c_id,prefix = '//*[@id="joblistdata"]'):
        jobs = []
        try:
            jlen = len(selector.xpath(prefix+'//div[.]/p').extract())
            for i in range(1, jlen + 1):
                job = selector.xpath(prefix+'//div[{}]'.format(i)).xpath('string(.)').extract()[0]
                jobhref = selector.xpath(prefix+'//div[{}]/p/a/@href'.format(i)).extract()[0]
                jobid = jobhref.split('/')[-1].split('.html')[0]
                job = job.replace('\n            ', '*').replace(' ', '').replace('\n', '').split('*')[1:]
                jobj = {
                    'j_id': jobid,
                    'c_id': c_id,
                    'j_name': job[0],
                    'j_work_expe': job[1],
                    'j_address': job[2],
                    'j_salary': job[3],
                    'j_pub_date': job[4]
                }
                jobs.append(jobj)
        except Exception as e:
            print(e.args,'该公司无招聘信息')
        return jobs

    def nextjob(self,response):
        selector = Selector(text=response.text)
        c_id = response.url.split('/co')[-1].replace('.html','')
        jobs = self.get_jobs(selector, c_id, prefix='')
        for job in jobs:
            jobstr = json.dumps(job, ensure_ascii=False) + '\n'
            job_f.write(jobstr)
        print(len(jobs))

    def parse(self, response):
        selector = Selector(text=response.text)
        company = self.get_company(selector)
        companystr = json.dumps(company,ensure_ascii=False) + '\n'
        company_f.write(companystr)
        companyid_f.write(company['c_id'] + '\n')
        print(company)
        # jobs = self.get_jobs(selector,company['c_id'])
        # for job in jobs:
        #     jobstr = json.dumps(job,ensure_ascii=False) + '\n'
        #     job_f.write(jobstr)
        #     print(job)

        # '''下一页岗位数据'''
        # url = response.url
        # totalpege = ceil(int(company['c_pub_jobcount'])/20)
        # for pageno in range(1,totalpege+1):
        #     formdata = {
        #         'pageno':str(pageno),
        #         'hidTotal':str(company['c_pub_jobcount']),
        #         'type':'',
        #         'code':''
        #     }
        #     yield scrapy.FormRequest(url,formdata=formdata,callback=self.nextjob)
