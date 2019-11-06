# 네이버 영화 데이터 수집

import requests
from bs4 import BeautifulSoup

raw = requests.get("https://movie.naver.com/movie/running/current.nhn", headers={"User-Agent":"Mozilla/5.0"})

html = BeautifulSoup(raw.text, 'html.parser')


# 컨테이너
movies = html.select("dl lst_dsc")

# 제목
# 평점
# 장르
# 감독
for m in movies:
    title= m.select_one("dt.tit a").text()
    score = m.select_one("div.star_t1 span.num")
    info = m .select("dl.info_txt1 dd")
    genre = info[0].select("a")
    directors = info[1].select("a")
    actor=info[2].select("a")

