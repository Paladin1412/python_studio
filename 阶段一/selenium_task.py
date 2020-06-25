from selenium import webdriver
import time
import urllib.request

def open_url(url='https://www.geetest.com/demo/click-popup.html'):
    option = webdriver.ChromeOptions()
    option.add_argument('--no-sandbox')  
    option.add_argument('--headless')  
    # 注意path，我这里是chromedriver放在/home/apk/chromedriver
    web = webdriver.Chrome(executable_path='/root/chromedriver', chrome_options=option)
    web.get(url)
    web.execute_script("document.getElementsByClassName('geetest_radar_tip')[0].click()")
    return web

def retry_click(web):
    web.execute_script("document.getElementsByClassName('geetest_refresh')[0].click()")
    time.sleep(1)
    ele = web.find_elements_by_xpath('//*[@class="geetest_item_img"]')
    for i in ele:
        pic_url = i.get_attribute('src').split('?')[0]
    return pic_url

def first_click(web):
    web.execute_script("document.getElementsByClassName('geetest_radar_tip')[0].click()")
    ele = web.find_elements_by_xpath('//*[@class="geetest_item_img"]')
    for i in ele:
        pic_url = i.get_attribute('src').split('?')[0]
    return pic_url



import os
web = open_url()
j = 0
count = 100
all_urls = []
while True:
    try:
        urls = []
        for i in range(6):
            url = retry_click(web)
            print(url)
            urls.append(url)
            all_urls.append(url)
        for url in urls:
            if not os.path.exists('imgs{}'.format(count)):
                os.mkdir('imgs{}'.format(count))
            r.urlretrieve(url,'imgs{}/'.format(count)+url.split('/')[-1])
            j+=1
    except Exception as e:
        web.execute_script("document.getElementsByClassName('geetest_reset_tip_content')[0].click()")
    if j>=2000:
        count+=1
        j = 0
    if len(all_urls)>2000:
        all_url_set = set(all_urls)
        all_urls = list(all_url_set)
        with open('img_url{}'.format(count),'w') as f:
            for all_url in all_urls:
                f.write(all_url+'\n')