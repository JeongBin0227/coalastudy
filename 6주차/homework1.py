from time import sleep

from selenium import webdriver

driver =webdriver.Chrome("./chromedriver")

driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")
sleep(5)
#입력
id = driver.find_element_by_id("id")
id.send_keys("####")
pw = driver.find_element_by_id("pw")
pw.send_keys("////")
sleep(5)
login = driver.find_element_by_css_selector("input.btn_global")
login.click()


