import requests
from bs4 import BeautifulSoup

raw = requests.get("https://map.naver.com",headers={"User-Agent":"Mozilla/5.0"})

html = BeautifulSoup(raw.text,'html.parser')

