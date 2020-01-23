#-*- coding: utf-8 -*-

from selenium import webdriver
from datetime import datetime
import io
import selenium as se
import urllib.request

path = "C:\\Users\\USER\\Desktop\\chromedriver.exe"

driver = webdriver.Chrome(path)

url = "https://aceship.github.io/AN-EN-Tags/akhrchars.html?opname="
lsts = ["Ch\'en",
"Siege",
"Shining",
"Nightingale",
"Ifrit",
"Eyjafjalla",
"Exusiai",
"Angelina",
"SilverAsh",
"Hoshiguma",
"Saria",
"Skadi",
"Schwarz",
"Hellagur",
"Magallan",
"Mostima",
"Blaze",
"Aak",
"Nian"
]

idn = []

link = []
errs = []

for strs in lsts:
    url = "https://aceship.github.io/AN-EN-Tags/akhrchars.html?opname="
    url += strs
    print(url)
    
    driver.get(url)
    driver.implicitly_wait(5)
    
    #elite 0
    '''
    try:
        img = driver.find_element_by_xpath("//*[@id=\"opCG_0_tab\"]/img")
        link.append(img.get_attribute('src'))
    except:
        try:
            img = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[2]/div/div[1]/div/div[1]/img")
            link.append(img.get_attribute('src'))
        except:
            errs.append(strs)
            print("ERROR : "+strs)
    '''
            
    #elite 2
    try:
        img = driver.find_element_by_xpath("//*[@id=\"opCG_2_tab\"]/img")
        link.append(img.get_attribute('src'))
    except:
        errs.append(strs)
        print("ERROR : "+strs)

    
print("---------------------------------")

for st in link:
    stt = st.split("_")
    idn.append(stt[1])

cnt = 0
for st in link:
    print(st)
    #urllib.request.urlretrieve(st, "C:\\Users\\USER\\Desktop\\amiyabot\\pics\\operator\\o"+str(idn[cnt])+".png")
    urllib.request.urlretrieve(st, "C:\\Users\\USER\\Desktop\\amiyabot\\pics\\operator\\p"+str(idn[cnt])+".png")
    cnt = cnt + 1
    
for st in errs:
    print("ERROR : "+st)

print("complete")
