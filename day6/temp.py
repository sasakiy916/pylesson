import requests
import json
from datetime import datetime, timedelta, timezone
from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

url = ('https://api.openweathermap.org/data/2.5/forecast'
       '?q={city}&appid={key}&lang=ja&units=metric')
url = url.format(city="Tokyo,JP", key="06ce691210c9136926cfc99990184728")
print(url)
jsondata = requests.get(url).json()

df = pd.DataFrame(columns=["気温"])

# timezoneを日本に変更
tz = timezone(timedelta(hours=+9), "JST")
for dat in jsondata["list"]:
    jst = str(datetime.fromtimestamp(dat["dt"], tz))[5:-9]
    weather = dat["weather"][0]["description"]
    temp = dat["main"]["temp"]
    df.loc[jst] = temp

pprint(df)
df.plot(figsize=(15, 8))
plt.ylim(-10, 40)
plt.grid()
plt.show()
