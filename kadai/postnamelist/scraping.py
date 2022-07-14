import time
import requests
from bs4 import BeautifulSoup

url = "https://joytas.net/page/"
page = 1
# 記事のあるページ全ての記事一覧を取得する
while True:
    # ページ数表示
    print(f"{page}ページ目:")
    time.sleep(0.5)  # 0.5秒停止
    # リクエスト送信
    res = requests.get(url+f"{page}")
    res.encoding = res.apparent_encoding
    # レスポンスからサイトの内容を取得
    soup = BeautifulSoup(res.text, "html.parser")
    # 記事一覧部分を取得
    list = soup.select("#list")[0]  # 結果はlistで返されるが中身は一つなのでindex指定して一つにしてる

    # 記事タイトル一覧を取得
    for a in list.find_all("a"):
        print(a.get("title"))

    # 次ページボタンがあればpageを1増やす
    next = soup.select(".next")
    if len(next) != 0:
        page += 1
        time.sleep(2)  # 2秒停止
    else:
        break
