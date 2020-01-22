#-*- coding: utf-8 -*-

from selenium import webdriver
from datetime import datetime
import io
import selenium as se

path = "C:\\Users\\USER\\Desktop\\chromedriver.exe"

driver = webdriver.Chrome(path)

url = "https://namu.wiki/w/"
lsts = ["수수루",
"퍼퓨머",
"딥컬러",
"어스스피릿"
]

for strs in lsts:
    url = "https://namu.wiki/w/"
    url = url + strs
    url = url + "(명일방주)"
    print(url)
    
    driver.get(url)
    
    e1 = driver.find_elements_by_class_name("wiki-paragraph")
    cnt = 0
    str = ""
    print(e1[0].text)
    for t in e1:
        if t.text == u"진영":
            print("진영: "+e1[cnt+1].text)
            str += e1[cnt+1].text + "\t"
        if t.text == u"성별":
            print("성별: "+e1[cnt+1].text)
            str += e1[cnt+1].text + "\t"
        if t.text == u"성우":
            print("성우: "+e1[cnt+1].text)
            str += e1[cnt+1].text + "\t"
        if t.text == u"일러스트":
            print("일러: "+e1[cnt+1].text)
            str += e1[cnt+1].text + "\t"
        if t.text == u"저지 가능 수":
            print("저지: "+e1[cnt+1].text)
            str += e1[cnt+1].text + "\t"
        if t.text == u"공격 속도":
            print("공속: "+e1[cnt+1].text)
            str += e1[cnt+1].text + "\t"
        if t.text == u"배치":
            print("재배치속도: "+e1[cnt+4].text)
            print("최종배치: "+e1[cnt+6].text)
            str += e1[cnt+4].text + "\t"
            str += e1[cnt+6].text
            print(str)
        if t.text == u"체력":
            print("체력: "+e1[cnt+1].text+e1[cnt+2].text)
        if t.text == u"공격력":
            print("공격: "+e1[cnt+1].text+e1[cnt+2].text)
        if t.text == u"방어력":
            print("방어: "+e1[cnt+1].text+e1[cnt+2].text)
        if t.text == u"마법 저항력":
            print("마법저항: "+e1[cnt+1].text+e1[cnt+2].text)
            break
            
        cnt = cnt + 1
