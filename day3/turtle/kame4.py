import turtle
t=turtle.Turtle()
t.shape("turtle")
t.forward(100) #向いてる方向に100移動
for i in range(3):
    t.right(144) #120度右回転
    t.forward(100)
t.home() #原点に移動し、デフォルトの方向を向く(右)
turtle.mainloop()
