import requests
from bs4 import BeautifulSoup

count = 0
for n in range(1, 4):
    # p=1, p=2, p=3으로 반복해준다.
    raw = requests.get("https://news.ycombinator.com/news?p="+str(n),
                       headers={"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

    articles = html.select("tr.athing")

    for ar in articles:
        rank = ar.select_one("span.rank").text
        title = ar.select_one("a.storylink").text
        print(rank, title)
        count = count +1

print(count)

