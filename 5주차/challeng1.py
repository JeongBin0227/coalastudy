# 네이버 영화 데이터 수집
import requests
from bs4 import BeautifulSoup

raw = requests.get("https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth",headers={"User-Agent": "Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')


# 컨테이너
movies = html.select("td.overview-top")

# 제목 - h4 a
# 평점 - div.rating_txt span
# 장르 - td.overview-top p
# 감독 - td.overview-top div.txt-block a
# 배우 - td.overview-top div.txt-block a
for m in movies:
    genre = m.select("p")
    for g in genre:
        if "Action" in g.text:
            continue
    title= m.select_one("h4 a").text
    try:
        score = m.select_one("div.rating_txt span").text
    except:
        score=''
    try:
        info = m .select("div.txt-block")
        directors = info[0].select("a")
        actor = info[1].select("a")
    except:
        directors=''
        actor=''

    print(title)
    print(score)
    for d in directors:
        print(d.text)
    for a in actor:
        print(a.text)
    print("------------------------------------------------------------")

