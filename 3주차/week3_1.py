import requests
from bs4 import BeautifulSoup

raw = requests.get("https://tv.naver.com/r")
#print(raw.text)

html = BeautifulSoup(raw.text, 'html.parser')
#print(html)

#1-3위 컨테이너 : div.inner
#제목 : dt.title
#채널명 : dd.chn
#재생수 : span.hit
#좋아요수 : span.like

#1. 컨테이너 수집

# container = html.select("div.inner")
# print(container[0])
#
# #2. 영상데이터 수집
# for cont in container:
#     title = cont.select_one("dt.title")
#     chn = cont.select_one("dd.chn")
#     hit = cont.select_one("span.hit")
#     like = cont.select_one("span.like")
#     print(title.text.strip())
#     print(chn.text.strip())
#     print(hit.text.strip())
#     print(like.text.strip())


container = html.select("div.cds")
print(container[0])

#2. 영상데이터 수집
for cont in container:
    title = cont.select_one("dt.title")
    chn = cont.select_one("dd.chn")
    hit = cont.select_one("span.hit")
    like = cont.select_one("span.like")
    print(title.text.strip())
    print(chn.text.strip())
    print(hit.text.strip())
    print(like.text.strip())