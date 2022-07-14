import tkinter as tk
import random


def btn_click():
    label["text"] = random.choice(["大吉", "中吉", "小吉", "狂"])
    label.update()


root = tk.Tk()
root.title("おみくじ")
root.resizable(False, False)  # 画面サイズの変更
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()
img = tk.PhotoImage(file="day7/images/miko.png")
canvas.create_image(400, 300, image=img)
label = tk.Label(root, text="? ?", font=("Arial", 120), bg="white")
label.place(x=380, y=60)
btn = tk.Button(root, text="おみくじを引く", font=(
    "Arial", 36), command=btn_click, bg="skyblue")
btn.place(x=370, y=400)
root.mainloop()
