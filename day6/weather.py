import requests
import json
from pprint import pprint

# 郵便番号zip={zip} 都道府県などの都市名q={city}
url = ('https://api.openweathermap.org/data/2.5/weather'
       '?zip={zip}&appid={key}&lang=ja&units=metric')
url = url.format(zip="146-0092,JP", key="06ce691210c9136926cfc99990184728")
jsondata = requests.get(url).json()
# pprint(jsondata)

print("都市名:", jsondata["name"])
print("気温:", jsondata["main"]["temp"], "℃")
print("天気:", jsondata["weather"][0]["main"])
print("天気詳細:", jsondata["weather"][0]["description"])
