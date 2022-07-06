import requests
from bs4 import BeautifulSoup

res=requests.get("https://joytas.net/kaba/")
res.encoding=res.apparent_encoding
soup=BeautifulSoup(res.text,"html.parser")

links=soup.select("li a")

with open("zoo.txt","w",encoding="utf-8") as file:
    for link in links:
        file.write(f"{link.text}:{link.get('href')}\n")
