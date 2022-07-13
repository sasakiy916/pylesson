import requests
import json
from datetime import datetime, timedelta, timezone

url = ('https://api.openweathermap.org/data/2.5/forecast'
       '?q={city}&appid={key}&lang=ja&units=metric')
url = url.format(city="Tokyo,JP", key="06ce691210c9136926cfc99990184728")
print(url)
jsondata = requests.get(url).json()

# timezoneを日本に変更
tz = timezone(timedelta(hours=+9), "JST")
for dat in jsondata["list"]:
    jst = str(datetime.fromtimestamp(dat["dt"], tz))[:-9]
    weather = dat["weather"][0]["description"]
    temp = dat["main"]["temp"]
    print(f"日時:{jst[5:]},天気:{weather},気温:{temp}度")
