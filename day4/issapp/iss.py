import requests as req
import json
import turtle as tt
url="http://api.open-notify.org/iss-now.json"
screen=None
iss=None

def setup():
    global iss,screen
    screen=tt.Screen()
    screen.setup(1000,500)
    screen.bgpic("earth.gif")
    screen.setworldcoordinates(-180,-90,180,90)
    tt.register_shape("iss.gif")
    iss=tt.Turtle()
    iss.shape("iss.gif")
    iss.pencolor("red")
    iss.hideturtle()
    iss.penup()

def track_iss():
    res=req.get(url)
    data=json.loads(res.text)
    pos=data["iss_position"]
    lat=float(pos["latitude"])
    lng=float(pos["longitude"])
    print("緯度{},経度{}".format(lat,lng))
    iss.goto(lng,lat)
    if not iss.isvisible():
        iss.pendown()
        iss.showturtle()

    canvas=tt.getcanvas()
    canvas.after(5000,track_iss)

setup()
track_iss()
tt.mainloop()
