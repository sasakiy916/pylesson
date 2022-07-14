import tkinter as tk


def btn_click():
    txt = entry.get()
    btn["text"] = txt


root = tk.Tk()
root.title("My Window")
root.geometry("400x200")
entry = tk.Entry(width=20)  # テキスト入力欄
entry.place(x=10, y=10)
btn = tk.Button(text="文字列の取得", command=btn_click)  # ボタン作成
btn.place(x=20, y=100)
root.mainloop()
