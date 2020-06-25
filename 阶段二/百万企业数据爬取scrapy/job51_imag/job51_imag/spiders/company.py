# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
import json

company_f = open('conpany_img.txt','a',encoding='utf-8')
class CompanySpider(scrapy.Spider):
    name = 'company'
    allowed_domains = ['51job.com']
    ##杜: 1300000, 2600000    id: 2
    ##黎: 2600000, 3900000    id: 3
    ##段: 3900000, 5200000    id: 4
    ##林: 5200000, 6500001    id: 5
    start_urls = ['https://jobs.51job.com/all/co{}.html'.format(i) for i in range(0,1300000)]

    def get_image_url(self,selector):
        companyj = {}
        Xpath = [
            ('//*[@id="hidCOID"]/@value', 'c_id'),
            ('/html/body/div[2]/div[2]/div[2]/div/h1/@title', 'c_name'),
        ]
        c_img = selector.xpath('//*[@id="divCoPoster"]/ul/li[.]/a/@bigimg').extract()
        if(c_img == []):
            return companyj
        for xpath,key in Xpath:
            try:
                companyj[key] = selector.xpath(xpath).extract()[0]
            except Exception as err:
                print('对不起，您选择的公司不存在或者已经过期!')
                companyj[key] = 'None'
        for i in range(len(c_img)):
            c_img[i] = 'https:' + c_img[i]
        companyj['c_img'] = c_img
        return companyj


    def parse(self, response):
        selector = Selector(text=response.text)
        company = self.get_image_url(selector)
        if company!= {}:
            companystr = json.dumps(company, ensure_ascii=False) + '\n'
            company_f.write(companystr)
            print(company)