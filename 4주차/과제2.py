import requests
from bs4 import BeautifulSoup
import openpyxl

try :
    wb = openpyxl.load_workbook("homewokr2.xlsx")
    print("불러오기 완료")
except:
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(["제목","기사내용"])
    print("새로운 파일을 만들었습니다.")

sheet = wb.active

count = 0
for page in range(6,9):
    print(page)
    raw = requests.get("https://search.daum.net/search?w=news&DA=PGD&enc=utf8&cluster=y&cluster_page=1&q=코알라&p="+str(page))
    html = BeautifulSoup(raw.text, 'html.parser')

    # 컨테이너 : ul.list_info li
    # 기사제목 : div.wrap_tit a
    # 기사내용 : p

    #1. 컨테이너 수집
    articles = html.select("ul.list_info li")

    #2. 기사데이터 수집
    for ar in articles:
        title = ar.select_one("div.wrap_tit a").text
        source =ar.select_one("p").text
        sheet.append([title, source])
        count = count + 1;

    wb.save("homewokr2.xlsx")
print(count)

