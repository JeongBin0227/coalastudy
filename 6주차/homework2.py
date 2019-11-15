from time import sleep
from selenium import webdriver

driver =webdriver.Chrome("./chromedriver")

driver.get("https://www.instagram.com/witheverland/")
sleep(5)
#입력

container = driver.find_elements_by_css_selector("div.v1Nh3")
container = container[:12]
for co in container:
    co.click()
    # 시간 지연
    sleep(1)

    # 본문 선택 후 출력
    post = driver.find_element_by_css_selector("div.C4VMK").text
    sleep(3)
    print(post)

    # 닫기 버튼 클릭
    but_close = driver.find_element_by_css_selector("button.ckWGn")
    but_close.click()
    print("끝")



#평점
#주소
#카페정보 100개 수집
# koean =driver.find_element_by_css_selector("div.edit_box___1KtZ3 span")
# print(koean.text)