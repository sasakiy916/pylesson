import requests as req
import json
import turtle
screen=turtle.Screen()
screen.setup(1000,500)
screen.bgpic("earth.gif")
screen.setworldcoordinates(-180,-90,180,90)

iss=turtle.Turtle()
turtle.register_shape("iss.gif")
iss.shape("iss.gif")

url="http://api.open-notify.org/iss-now.json"
res=req.get(url)
data=json.loads(res.text)
pos=data["iss_position"]
lat=float(pos["latitude"])
lng=float(pos["longitude"])

iss.penup()
iss.goto(lng,lat)
iss.pendown()

turtle.mainloop()
