import tkinter as tk

neko = [
    [1, 0, 0, 0, 0, 0, 7, 7],
    [0, 2, 0, 0, 0, 0, 7, 7],
    [0, 0, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 6, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 2, 3, 4, 5, 6]
]


def draw_neko():
    for y in range(10):
        for x in range(8):
            if neko[y][x] > 0:
                cvs.create_image(x*72+60, y*72+60, image=img_neko[neko[y][x]])


root = tk.Tk()
root.title("二次元リストでマスを管理する")
root.resizable(False, False)
cvs = tk.Canvas(root, width=912, height=768)
cvs.pack()

bg = tk.PhotoImage(file="nekopzl/images/neko_bg.png")
img_neko = [
    None,
    tk.PhotoImage(file="nekopzl/images/neko1.png"),
    tk.PhotoImage(file="nekopzl/images/neko2.png"),
    tk.PhotoImage(file="nekopzl/images/neko3.png"),
    tk.PhotoImage(file="nekopzl/images/neko4.png"),
    tk.PhotoImage(file="nekopzl/images/neko5.png"),
    tk.PhotoImage(file="nekopzl/images/neko6.png"),
    tk.PhotoImage(file="nekopzl/images/neko_niku.png"),
]

cvs.create_image(456, 384, image=bg)
draw_neko()
root.mainloop()
