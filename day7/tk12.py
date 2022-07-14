import tkinter as tk
import tkinter.messagebox as mbox


def bt_click():
    mbox.showinfo("情報", "ボタンを押しました")


root = tk.Tk()
root.title("My Window")
root.geometry("400x200")
btn = tk.Button(text="テスト", command=bt_click)
btn.pack()
root.mainloop()
