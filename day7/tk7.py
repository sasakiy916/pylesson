import tkinter as tk
root = tk.Tk()
root.title("My Winodow")
canvas = tk.Canvas(root, width=400, height=600)
canvas.pack()
img = tk.PhotoImage(file="day7/images/iroha.png")
canvas.create_image(200, 300, image=img)
root.mainloop()
