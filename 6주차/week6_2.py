from time import sleep

from selenium import webdriver

driver =webdriver.Chrome("./chromedriver")

driver.get("https://www.naver.com/")
sleep(3)
#컨테이너
search_box = driver.find_element_by_id("query")
search_box.send_keys("치킨")
#가게이름
