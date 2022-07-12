from cmath import isnan
from numpy import NaN
import pandas as pd
import folium
import math

df = pd.read_csv("pdlesson/csv/774.csv")
m = folium.Map(location=[35.942957, 136.198863], zoom_start=16)

event = df[["緯度", "経度", "イベント名"]].values

for data in event:
    print(data[2])
    print(math.isnan(data[0]))
    if math.isnan(data[0]) or math.isnan(data[1]):
        continue
    folium.Marker([data[0], data[1]], tooltip=data[2]).add_to(m)
m.save("event.html")
