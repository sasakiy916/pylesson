import tkinter as tk

from cv2 import IMWRITE_PNG_BILEVEL
images = "day9/images"

x = 0
ani = 0
frame = 0


def animation():
    global x, ani, frame
    frame += 1
    x = x+1
    if x == 480:
        x = 0
    canvas.delete("BG")
    canvas.create_image(x-240, 150, image=img_bg, tag="BG")
    canvas.create_image(x+240, 150, image=img_bg, tag="BG")
    if frame % 4 == 0:
        ani = (ani+1) % 4
    canvas.create_image(240, 200, image=img_dog[ani], tag="BG")
    root.after(50, animation)


root = tk.Tk()
root.title("アニメーション")
canvas = tk.Canvas(width=480, height=300)
canvas.pack()
img_bg = tk.PhotoImage(file=f"{images}/park.png")
img_dog = [
    tk.PhotoImage(file=f"{images}/dog0.png"),
    tk.PhotoImage(file=f"{images}/dog1.png"),
    tk.PhotoImage(file=f"{images}/dog2.png"),
    tk.PhotoImage(file=f"{images}/dog3.png"),
]
animation()
root.mainloop()
