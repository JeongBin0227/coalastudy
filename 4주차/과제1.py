# 컨테이너: div.lst_thum_wrap li
# 제목: div.lst_thum_wrap li a strong
# 저자: div.lst_thum_wrap li span.writer

import requests
from bs4 import BeautifulSoup
import  openpyxl
count = 0

try :
    wb = openpyxl.load_workbook("homewokr1.xlsx")
    print("불러오기 완료")
except:
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(["제목","저자"])
    print("새로운 파일을 만들었습니다.")

sheet = wb.active

for page in range(6,8):
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
        title = ar.select_one("div.lst_thum_wrap li a strong").text.strip()
        people =ar.select_one("div.lst_thum_wrap li span.writer").text.strip()
        sheet.append([title, people])
        count = count + 1;

    wb.save("homewokr1.xlsx")
print(count)


