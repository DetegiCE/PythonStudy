#-*- coding: utf-8 -*-

from selenium import webdriver
from datetime import datetime
import io
import selenium as se

path = "C:\\Users\\USER\\Desktop\\chromedriver.exe"

driver = webdriver.Chrome(path)

url = "https://namu.wiki/w/"
lsts = ["라플란드",
"스펙터",
"새비지",
"브로카",
"스와이어",
"아스테시아",
"크루아상",
"바이슨",
"니어",
"벌컨",
"프로젝트 레드",
"와이 푸",
"클리프하트",
"에프이터",
"스노우상트",
"맨티코어",
"블루포이즌",
"플래티넘",
"그레이스롯",
"메테오라이트",
"프로방스",
"파이어워치",
"익스큐터",
"아미야",
"나이트메어",
"스카이파이어",
"사일런스",
"와파린",
"프틸롭시스",
"브리즈",
"실론",
"메이어",
"이스티나",
"글라우쿠스",
"프라마닉스",
"소라"
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
            if e1[cnt+1].text[-1] == "초":
                str += e1[cnt+1].text[0:-1] + "s\t"
            else:
                str += e1[cnt+1].text + "\t"
        if t.text == u"배치":
            print("재배치속도: "+e1[cnt+4].text)
            print("최종배치: "+e1[cnt+6].text)
            if e1[cnt+4].text[-1] == "초":
                str += e1[cnt+4].text[0:-1] + "s\t"
            else:
                str += e1[cnt+4].text + "\t"
            str += e1[cnt+6].text + "\t"
        if t.text == u"체력":
            print("체력: "+e1[cnt+1].text+e1[cnt+2].text)
            str += e1[cnt+1].text.split("→")[-1]
            str += e1[cnt+2].text + "\t"
        if t.text == u"공격력":
            print("공격: "+e1[cnt+1].text+e1[cnt+2].text)
            str += e1[cnt+1].text.split("→")[-1]
            str += e1[cnt+2].text + "\t"
        if t.text == u"방어력":
            print("방어: "+e1[cnt+1].text+e1[cnt+2].text)
            str += e1[cnt+1].text.split("→")[-1]
            str += e1[cnt+2].text + "\t"
        if t.text == u"마법 저항력":
            print("마법저항: "+e1[cnt+1].text+e1[cnt+2].text)
            str += e1[cnt+1].text.split("→")[-1]
            str += e1[cnt+2].text + "\t"
            print(str)
            break
            
        cnt = cnt + 1
