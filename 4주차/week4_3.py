import requests
from bs4 import BeautifulSoup
#-*- coding: utf-8 -*-

f=open("hitsong.csv","w",encoding="cp949")
f.write("제목, 채널명, 재생수, 좋아요 \n")
raw = requests.get("https://tv.naver.com/r")
#print(raw.text)

html = BeautifulSoup(raw.text, 'html.parser')

container = html.select("div.cds")
print(container[0])

#2. 영상데이터 수집
for cont in container:
    title = cont.select_one("dt.title").text.strip()
    chn = cont.select_one("dd.chn").text.strip()
    hit = cont.select_one("span.hit").text.strip()
    like = cont.select_one("span.like").text.strip()

    title = title.replace(",","")
    chn = chn.replace(",", "")
    hit = hit.replace(",", "")
    like = like.replace(",", "")

    hit = hit.replace("재생 수", "")
    like = like.replace("좋아요 수", "")
    f.write(title+','+chn+','+hit+','+like+'\n')


    # print(title.text.strip())
    # print(chn.text.strip())
    # print(hit.text.strip())
    # print(like.text.strip())


f.close()