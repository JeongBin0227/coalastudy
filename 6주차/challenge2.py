from time import sleep

from selenium import webdriver

driver =webdriver.Chrome("./chromedriver")

driver.get("https://www.google.com/maps/?hl=ko")
sleep(5)
#입력
search_box = driver.find_element_by_id("searchboxinput")
search_box.send_keys("카페")
search_button = driver.find_element_by_id("searchbox-searchbutton")
search_button.click()
sleep(5)

#컨테이너


for a in range(1,5):
    container = driver.find_elements_by_css_selector("div.section-result-text-content")

    #이름  div h3 span
    for co in container:
        name = co.find_element_by_css_selector("div h3 span")
        score = co.find_element_by_css_selector("span.cards-rating-score")
        where = co.find_element_by_css_selector("span.section-result-location")
        print(name.text)
        print(score.text)
        print(where.text)
        print("*"*20)

    print("페이지 변경")
    button = driver.find_element_by_id("n7lv7yjyC35__section-pagination-button-next")
    button.click()
#가게이름
#평점
#주소
#카페정보 100개 수집
# koean =driver.find_element_by_css_selector("div.edit_box___1KtZ3 span")
# print(koean.text)