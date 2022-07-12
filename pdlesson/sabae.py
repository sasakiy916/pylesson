import pandas as pd
import folium

df = pd.read_csv("pdlesson/csv/200.csv", encoding="shift-jis")
m = folium.Map(location=[35.942957, 136.198863], zoom_start=16)
print(len(df))
print(df.columns.values)

hydrant = df[["緯度", "経度"]].values
print(len(hydrant))
print(hydrant)

for data in hydrant:
    folium.Marker([data[0], data[1]]).add_to(m)
m.save("hydrant.html")
