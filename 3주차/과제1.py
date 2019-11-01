# 컨테이너: div.lst_thum_wrap li
# 제목: div.lst_thum_wrap li a strong
# 저자: div.lst_thum_wrap li span.writer

import requests
from bs4 import BeautifulSoup

count = 0
for page in range(1,6):
    print(page)
    raw = requests.get("https://series.naver.com/ebook/top100List.nhn?page="+str(page)+"&refresh_start=0",headers={"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

    # 컨테이너 : ul.type01 > li
    # 기사제목 : a._sp_each_title
    # 언론사 : span._sp_each_source

    #1. 컨테이너 수집
    books = html.select("div.lst_thum_wrap li")

    #2. 책데이터 수집
    for ar in books:
        title = ar.select_one("div.lst_thum_wrap li a strong").text
        people =ar.select_one("div.lst_thum_wrap li span.writer").text
        print(title, people)
        count = count +1;

print(count)


