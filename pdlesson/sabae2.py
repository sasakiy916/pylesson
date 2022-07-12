import folium

m = folium.Map(location=[35.942957, 136.198863], zoom_start=16)
folium.Marker([35.942957, 136.198863]).add_to(m)
m.save("sabae.html")
