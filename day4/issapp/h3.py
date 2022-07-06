import requests as req
import json
import turtle
screen=turtle.Screen()
screen.setup(1000,500)
screen.bgpic("earth.gif")
# 座標系を変換
screen.setworldcoordinates(-180,-90,180,90)

url="http://api.open-notify.org/iss-now.json"
res=req.get(url)
data=json.loads(res.text)
pos=data["iss_position"]
print("ISSの緯度は{},経度は{}".format(pos["latitude"],pos["longitude"]))
turtle.mainloop()
