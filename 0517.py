#0517
#pip install beautifulsoup4
from bs4 import BeautifulSoup
import requests

# url(www.naver.com) -> 크롬에서 DNS로 보냄 (Domain Name Serve)
# DNS에서 진짜주소 111.111.111등의 진짜 주소 보냄 
# 크롬이 다시 111.~진짜주소 활용해서 네이버로 연결 : request
# 네이버에서 개인에게 응답 : response

headers = {
    "User-Agent" : "DongYang Mirae Univ"
}
webpage = requests.get("https://n.news.naver.com/mnews/article/009/0005131365?sid=102", headers=headers)
print(webpage)
print(webpage.content)
soup =  BeautifulSoup(webpage.content, "html.parser")
print(soup)

news = soup.select_one("#dic_area").get_text().strip()
print(news)

#pip install selenium
#pip install webdriver_manager

import time #기본으로 설치되어 있는 모듈

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service= service)
'''
#(1) news를 가져온다.
driver.get("http://www.naver.com/")
time.sleep(1)

#원하는 버튼을 누르는 명령을 한다. 뉴스 버튼 누름
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/div[1]/div[1]/ul[2]/li[2]/a").click()
time.sleep(1)

#).text
newstitle1 = driver.find_element(By.XPATH, "/html/body/div[2]/div/section[1]/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/a/div[2]/div").text
time.sleep(1)
print(newstitle1)

# 아파트 가격 알아보기
driver.get("https://m.land.naver.com/search")

driver.find_element(By.XPATH, "/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input").send_keys("우성꿈동산")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/button[2]/i").click()
time.sleep(1)
# 전세값 가져오기
rentprice =  driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[5]/div/section/div/div/div[1]/div[2]/div/div/dl[2]").text
print(rentprice)

# 고양이 사진 가져오기
driver.get("https://www.naver.com/")
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div/div[3]/form/fieldset/div/input").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div/div[3]/form/fieldset/div/input").send_keys("고양이 사진")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div/div[3]/form/fieldset/button/span[2]").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div[1]/section[1]/div/div[3]/div/div[9]/a").text
'''
# 주식 종목 정보 가져오기
driver.get("https://finance.naver.com/")
'''
subject1 = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[1]/th/a").text
time.sleep(1)
subject2 = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[2]/th/a").text
time.sleep(1)
subject3 = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[3]/th/a").text
time.sleep(1)
print(subject1, subject2, subject3)
'''

lst = []
for i in range(10) : #0~9까지이므로 i+1
    subject = driver.find_element(By.XPATH, f"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i+1}]/th/a").text # variable i 생성
    lst.append(subject)
print(lst)

lst2 = []
for i in range(10) :
    subject = driver.find_element(By.XPATH, f"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i+1}]/td[1]").text
    lst2.append(subject)
print(lst2)
    
