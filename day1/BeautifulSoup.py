import requests
from bs4 import BeautifulSoup

res = requests.get("https://joytas.net/kaba/")
res.encoding=res.apparent_encoding

soup=BeautifulSoup(res.text,"html.parser")

#print(soup)

ele=soup.find("title")
print(ele.text)

imgs=soup.find_all("img")
for img in imgs:
    print(img.get("src"))

div=soup.find(id="headerImageBox")

imgs=soup.select(".headerImage")
for img in imgs:
    print(img.get("src"))

trs = soup.find_all("tr")
for tr in trs:
    td=tr.find_all("td")
    count =0
    for t in td:
        if count%3==0:
            print(t.text)
        count=count+1
