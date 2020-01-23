#-*- coding: utf-8 -*-

from selenium import webdriver
from datetime import datetime
import io
import selenium as se

path = "C:\\Users\\USER\\Desktop\\chromedriver.exe"

driver = webdriver.Chrome(path)

url = "https://aceship.github.io/AN-EN-Tags/akhrchars.html?opname="
lsts = ["Matterhorn",
"Greyy",
"Sussurro",
"Myrtle",
"Dur-nar",
"Vermeil",
"Ethan",
"May",
"Ambriel"]

for strs in lsts:
    url = "https://aceship.github.io/AN-EN-Tags/akhrchars.html?opname="
    url += strs
    print(url)
    
    driver.get(url)
    driver.implicitly_wait(5)
    
    str = ""
    
    #영문 이름
    str = str + strs + "\t"
    
    #일러스트
    e = driver.find_elements_by_xpath("//*[@id=\"info-illustrator\"]/div[2]/a")
    str = str + e[0].text + "\t"
    
    #CV
    e = driver.find_elements_by_xpath("//*[@id=\"info-voiceactor\"]/div[2]/a")
    str = str + e[0].text + "\t"
    
    #codename
    e = driver.find_elements_by_xpath("//*[@id=\"op-displaynum\"]")
    str = str + e[0].text + "\t"
    
    #gender
    e = driver.find_elements_by_xpath("//*[@id=\"op-gender\"]")
    str = str + e[0].text + "\t"
    
    #병과
    e = driver.find_elements_by_xpath("//*[@id=\"op-className\"]")
    str = str + e[0].text + "\n"
    
    #신뢰도
    e = driver.find_elements_by_xpath("//*[@id=\"op-trust\"]/div/div")
    str = str + e[0].text + "\n"
    
    str = str + "\n------------------------------------------\n"
    
    #level set
    driver.find_element_by_id('elite0LevelDisplay').send_keys("45")
    
    #max hp
    e = driver.find_elements_by_xpath("//*[@id=\"elite0maxHp\"]")
    str = str + e[0].text + "\t"
    
    #redeploy
    e = driver.find_elements_by_xpath("//*[@id=\"elite0respawnTime\"]")
    str = str + e[0].text + "\t"
    
    #attack power
    e = driver.find_elements_by_xpath("//*[@id=\"elite0atk\"]")
    str = str + e[0].text + "\t"
    
    #cost
    e = driver.find_elements_by_xpath("//*[@id=\"elite0cost\"]")
    str = str + e[0].text + "\t"
    
    #defense
    e = driver.find_elements_by_xpath("//*[@id=\"elite0def\"]")
    str = str + e[0].text + "\t"
    
    #block
    e = driver.find_elements_by_xpath("//*[@id=\"elite0blockCnt\"]")
    str = str + e[0].text + "\t"
    
    #mag resist
    e = driver.find_elements_by_xpath("//*[@id=\"elite0magicResistance\"]")
    str = str + e[0].text + "\t"
    
    #attack time
    e = driver.find_elements_by_xpath("//*[@id=\"elite0baseAttackTime\"]")
    str = str + e[0].text + "\t"
    
    driver.find_element_by_xpath("//*[@id=\"elite-topnav\"]/li[2]/a").click()
    
    str = str + "\n------------------------------------------\n"
    
    #level set
    driver.find_element_by_id('elite1LevelDisplay').send_keys("60")
    
    #max hp
    e = driver.find_elements_by_xpath("//*[@id=\"elite1maxHp\"]")
    str = str + e[0].text + "\t"
    
    #redeploy
    e = driver.find_elements_by_xpath("//*[@id=\"elite1respawnTime\"]")
    str = str + e[0].text + "\t"
    
    #attack power
    e = driver.find_elements_by_xpath("//*[@id=\"elite1atk\"]")
    str = str + e[0].text + "\t"
    
    #cost
    e = driver.find_elements_by_xpath("//*[@id=\"elite1cost\"]")
    str = str + e[0].text + "\t"
    
    #defense
    e = driver.find_elements_by_xpath("//*[@id=\"elite1def\"]")
    str = str + e[0].text + "\t"
    
    #block
    e = driver.find_elements_by_xpath("//*[@id=\"elite1blockCnt\"]")
    str = str + e[0].text + "\t"
    
    #mag resist
    e = driver.find_elements_by_xpath("//*[@id=\"elite1magicResistance\"]")
    str = str + e[0].text + "\t"
    
    #attack time
    e = driver.find_elements_by_xpath("//*[@id=\"elite1baseAttackTime\"]")
    str = str + e[0].text + "\t"
    
    driver.find_element_by_xpath("//*[@id=\"elite-topnav\"]/li[3]/a").click()
    
    str = str + "\n------------------------------------------\n"
    
    #level set
    driver.find_element_by_id('elite2LevelDisplay').send_keys("70")
    
    #max hp
    e = driver.find_elements_by_xpath("//*[@id=\"elite2maxHp\"]")
    str = str + e[0].text + "\t"
    
    #redeploy
    e = driver.find_elements_by_xpath("//*[@id=\"elite2respawnTime\"]")
    str = str + e[0].text + "\t"
    
    #attack power
    e = driver.find_elements_by_xpath("//*[@id=\"elite2atk\"]")
    str = str + e[0].text + "\t"
    
    #cost
    e = driver.find_elements_by_xpath("//*[@id=\"elite2cost\"]")
    str = str + e[0].text + "\t"
    
    #defense
    e = driver.find_elements_by_xpath("//*[@id=\"elite2def\"]")
    str = str + e[0].text + "\t"
    
    #block
    e = driver.find_elements_by_xpath("//*[@id=\"elite2blockCnt\"]")
    str = str + e[0].text + "\t"
    
    #mag resist
    e = driver.find_elements_by_xpath("//*[@id=\"elite2magicResistance\"]")
    str = str + e[0].text + "\t"
    
    #attack time
    e = driver.find_elements_by_xpath("//*[@id=\"elite2baseAttackTime\"]")
    str = str + e[0].text + "\t"
    
    str = str + "\n------------------------------------------\n"

    #talent
    e = driver.find_elements_by_xpath("//*[@id=\"op-talentlist\"]")
    str = str + e[0].text + "\t"
    
    str = str + "\n------------------------------------------\n"
    
    #skill1
    e = driver.find_elements_by_xpath("//*[@id=\"skill0\"]/div[1]/span")
    str = str + e[0].text + "\t"
    
    try:
        e = driver.find_elements_by_xpath("//*[@id=\"skill0level0stats\"]/tbody/tr[7]/td/div[3]")
        str = str + "(" + e[0].text + ")\t"
    except:
        str = str + "(!!!ERROR!!!)\t"
    
    str = str + "\n------------------------------------------\n"
    
    #skill2
    try:
        driver.find_element_by_xpath("//*[@id=\"skill-tabs\"]/li[2]/button").click()
    except:
        str = str + "(!!!SKILL2 ERROR!!!)\t"
        print(str+"\n\n")
        continue
    
    e = driver.find_elements_by_xpath("//*[@id=\"skill1\"]/div[1]/span")
    str = str + e[0].text + "\t"
    
    try:
        e = driver.find_elements_by_xpath("//*[@id=\"skill1level0stats\"]/tbody/tr[7]/td/div[3]")
        str = str + "(" + e[0].text + ")\t"
    except:
        str = str + "(!!!ERROR!!!)\t"
    
    
    print(str+"\n\n")
