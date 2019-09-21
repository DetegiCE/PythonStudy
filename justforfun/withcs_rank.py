#-*- coding: utf-8 -*-

from selenium import webdriver
from datetime import datetime
import io
import selenium as se

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("no-sandbox")
options.add_argument("--disable-dev-shm-usage")

options.add_argument("user-agent=Mozilla/5.0 "
                     "(Macintosh; Intel Mac OS X 10_12_6) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/61.0.3163.100 Safari/537.36")

options.add_argument("lang=ko_KR")

#browser = se.webdriver.Chrome(chrome_options = options)

names = [u"김류빈",u"정무영",u"홍승재",u"정우성",u"박홍빈",u"이상욱",u"이성진",u"신범준",u"강지원",u"지성초",u"오승환"]
ids = ["martinok1103","jmy3033","acehong1021","mung3477","qkrghdqls1","vecum0814","sagjin0000","ericbj","jiwon7258","tjdch99","osh925"]

f = io.open('/var/www/html/data.txt', mode = 'wt', encoding='utf-8')

now = datetime.now()
#f.write(u'||UPDATE : %s-%s-%s %s:%s:%s (UTC)'%(now.year, now.month, now.day, now.hour, now.minute, now.second))

cnt = 0

for str in ids:
        url = "https://withcs.net/u/"
        url += str
        #browser = webdriver.PhantomJS()
        browser = se.webdriver.Chrome(chrome_options = options)
        browser.get(url)
        selet = browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/h2")
        selem = browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/ul/button[1]/span")
        selef = browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/ul/button[2]/span")
        a = selet.text.split('-')
        #print(a[0])
        bb = names[cnt]
        f.write(bb)
        f.write(u'|')
        cnt = cnt+ 1
        f.write(a[0])
        f.write(u'|')
        #print(a[1].lstrip())
        aa = unicode(a[1].lstrip())
        f.write(aa)
        f.write(u'|')
        #print(selem.text)
        f.write(selem.text+'|')
        #print(selef.text)
        f.write(selef.text+'|')
        #print(int(selem.text)+int(selef.text))
        #f.write(int(selem.text)+int(selef.text))
        print('complete '+str)
        browser.quit()
#f.write(now)
f.write(u'||UPDATE : %s-%s-%s %s:%s:%s (UTC)'%(now.year,now.month,now.day,now.hour,now.minute,now.second))
f.close()
