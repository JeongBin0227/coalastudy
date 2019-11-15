import requests
from bs4 import BeautifulSoup

f = open('hex.txt', 'r')
fx =open("hex2.csv","w",encoding="cp949")
fx.write("r, g,b \n")

while True:
    line = f.readline()
    if not line:
        break
    fx.write(str(int(line[0:2],16)))
    fx.write(str(int(line[2:4], 16)))
    fx.write(str(int(line[4:6], 16)))
    fx.write("\n")

f.close()
fx.close()
