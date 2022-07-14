import tkinter as tk
import math

# 割り勘計算して文字表示


def click_btn_calc():
    price = int(p_entry.get())
    num = int(n_entry.get())
    onePrice = math.ceil((price/num)/100)*100
    r_label["text"] = f"1人あたり{onePrice}円({num-1}人)、幹事は{price-(onePrice*(num-1))}円です"


# メインウインドウ、キャンバス用意
root = tk.Tk()
root.title("割り勘しよう！")
root.resizable(False, False)
canvas = tk.Canvas(root, width=400, height=800, bg="skyblue")
canvas.pack()

# 各ラベル、入力欄用意
label_fontsize = 12
placeY = 20
# 金額入力欄
pLabel = tk.Label(text="金額", font=("Arial", label_fontsize), bg="skyblue")
pLabel.place(x=20, y=placeY)
p_entry = tk.Entry(width=20)
p_entry.place(x=20, y=placeY+30)
# 人数入力欄
nLabel = tk.Label(text="人数", font=("Arial", label_fontsize), bg="skyblue")
nLabel.place(x=20, y=placeY+50)
n_entry = tk.Entry(width=20)
n_entry.place(x=20, y=placeY+80)

# 計算ボタン
calc_button = tk.Button(text="計算する", command=click_btn_calc)
calc_button.place(x=20, y=placeY+110)
r_label = tk.Label(text="", font=("Arial", label_fontsize), bg="skyblue")
r_label.place(x=20, y=placeY+140)

root.mainloop()
