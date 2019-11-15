from time import sleep

from selenium import webdriver

driver =webdriver.Chrome("./chromedriver")

driver.get("https://papago.naver.com/")
sleep(3)
#입력
search_box = driver.find_element_by_id("txtSource")
search_box.send_keys("Hello, my life")
sleep(3)
#출력
koean =driver.find_element_by_css_selector("div.edit_box___1KtZ3 span")
print(koean.text)