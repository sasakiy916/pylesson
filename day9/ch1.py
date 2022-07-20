import tkinter as tk
import datetime


def time_now():
    d = datetime.datetime.now()
    t = f"{d.hour:02}:{d.minute:02}:{d.second:02}"
    label["text"] = t
    root.after(1000, time_now)


root = tk.Tk()
root.geometry("400x100")
root.title("簡易時計")
label = tk.Label(font=("Times New Roman", 60))
label.pack()
time_now()
root.mainloop()
