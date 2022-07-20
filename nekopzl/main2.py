from hashlib import new
import tkinter as tk
import random
import pprint

index = 0
timer = 0
score = 0
hisc = 1000
difficulty = 0
tsugi = 0
result = ""

cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0
mouse_c = 0


def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y


def mouse_press(e):
    global mouse_c
    mouse_c = 1


neko = []
check = []


# 盤面のリスト用意
for i in range(10):
    neko.append([0, 0, 0, 0, 0, 0, 0, 0])
    check.append([0, 0, 0, 0, 0, 0, 0, 0])


def init_neko():
    for y in range(len(neko)):
        for x in range(len(neko[y])):
            neko[y][x] = 0


def draw_neko():
    cvs.delete("NEKO")
    for y in range(10):
        for x in range(8):
            if neko[y][x] > 0:
                cvs.create_image(x*72+60, y*72+60,
                                 image=img_neko[neko[y][x]], tag="NEKO")


def check_neko():
    for y in range(10):
        for x in range(8):
            check[y][x] = neko[y][x]

    # 縦チェック
    for y in range(1, 9):
        for x in range(8):
            if check[y][x] > 0:
                if check[y-1][x] == check[y][x] and check[y+1][x] == check[y][x]:
                    neko[y-1][x] = 7
                    neko[y][x] = 7
                    neko[y+1][x] = 7

    # 横チェック
    for y in range(10):
        for x in range(1, 7):
            if check[y][x] > 0:
                if check[y][x-1] == check[y][x] and check[y][x+1] == check[y][x]:
                    neko[y][x-1] = 7
                    neko[y][x] = 7
                    neko[y][x+1] = 7

    # 斜めチェック
    for y in range(1, 9):
        for x in range(1, 7):
            if check[y][x] > 0:
                if check[y-1][x-1] == check[y][x] and check[y+1][x+1] == check[y][x]:
                    neko[y-1][x-1] = 7
                    neko[y][x] = 7
                    neko[y+1][x+1] = 7
                if check[y+1][x-1] == check[y][x] and check[y-1][x+1] == check[y][x]:
                    neko[y+1][x-1] = 7
                    neko[y][x] = 7
                    neko[y-1][x+1] = 7


def sweep_neko():
    num = 0
    for y in range(10):
        for x in range(8):
            if neko[y][x] == 7:
                # neko[y][x] = 0
                num = num+1
    return num


# def drop_neko():
#     flg = False
#     for y in range(8, -1, -1):
#         for x in range(8):
#             if neko[y][x] != 0 and neko[y+1][x] == 0:
#                 neko[y+1][x] = neko[y][x]
#                 neko[y][x] = 0
#                 flg = True
#     return flg


# def over_neko():
#     for x in range(8):
#         if neko[0][x] > 0:
#             return True
#     return False
# 盤面(3×3)が全部埋まってたら
def over_neko():
    for y in range(3):
        for x in range(3):
            if neko[y][x] == 0:
                return False
    return True


# def set_neko():
#     for x in range(8):
#         neko[0][x] = random.randint(0, difficulty)


def draw_txt(txt, x, y, siz, col, tg):
    fnt = ("Times New Roman", siz, "bold")
    cvs.create_text(x+2, y+2, text=txt, fill="black", font=fnt, tag=tg)
    cvs.create_text(x, y, text=txt, fill=col, font=fnt, tag=tg)


def game_main():
    global index, timer, score, hisc, difficulty, tsugi, result
    global cursor_x, cursor_y, mouse_c
    if index == 0:  # タイトルロゴ
        draw_txt("ねこねこ", 312, 240, 100, "violet", "TITLE")
        # cvs.create_rectangle(168, 384, 456, 456,
        #                      fill="skyblue", width=0, tag="TITLE")
        # draw_txt("Easy", 312, 420, 40, "white", "TITLE")
        # cvs.create_rectangle(168, 528, 456, 600,
        #                      fill="lightgreen", width=0, tag="TITLE")
        # draw_txt("Normal", 312, 564, 40, "white", "TITLE")
        # cvs.create_rectangle(168, 672, 456, 744,
        #                      fill="orange", width=0, tag="TITLE")
        # draw_txt("Hard", 312, 708, 40, "white", "TITLE")
        cvs.create_rectangle(96, 528, 528, 600,
                             fill="orange", width=0, tag="TITLE")
        draw_txt("GAME START", 312, 564, 40, "white", "TITLE")
        index = 1
        mouse_c = 0
    elif index == 1:  # タイトル画面 スタート待ち
        difficulty = 0
        if mouse_c == 1:
            #     if 168 < mouse_x < 456 and 384 < mouse_y < 456:
            #         difficulty = 4
            #     if 168 < mouse_x < 456 and 528 < mouse_y < 600:
            #         difficulty = 5
            #     if 168 < mouse_x < 456 and 672 < mouse_y < 744:
            #         difficulty = 6
            # if difficulty > 0:
            #     for y in range(10):
            #         for x in range(8):
            #             neko[y][x] = 0
            mouse_c = 0
            score = 0
            # tsugi = 0
            tsugi = 1
            cursor_x = 0
            cursor_y = 0
            # set_neko()
            init_neko()
            draw_neko()
            cvs.delete("TITLE")
            index = 3
    #         index = 2
    # elif index == 2:  # 落下
    #     if drop_neko() == False:
    #         index = 3
    #     draw_neko()
    elif index == 3:  # 揃ったか
        check_neko()
        draw_neko()
        index = 4
    elif index == 4:  # 揃ったネコがあれば消す
        sc = sweep_neko()
        score = score + sc*difficulty*2
        if score > hisc:
            hisc = score
        if sc > 0:  # 揃ってたら(どっちかの勝ち)
            # index = 2
            # index = 3
            index = 6
            result = f"P{1 if tsugi==2 else 2} WIN"
        else:
            if over_neko() == False:  # 盤面が埋まってなければ
                # tsugi = random.randint(1, difficulty)
                index = 5
            else:  # 盤面が埋まってたら(引き分け)
                index = 6
                timer = 0
                result = "DRAW"
        draw_neko()
    elif index == 5:  # マウス入力待ち
        # if 24 <= mouse_x < 24+72*8 and 24 <= mouse_y < 24+72*10:
        if 24 <= mouse_x < 24+72*3 and 24 <= mouse_y < 24+72*3:
            cursor_x = int((mouse_x-24)/72)
            cursor_y = int((mouse_y-24)/72)
            if mouse_c == 1:
                mouse_c = 0
                # set_neko()
                # neko[cursor_y][cursor_x] = tsugi
                # クリックした場所が空白かどうか
                if neko[cursor_y][cursor_x] == 0:
                    neko[cursor_y][cursor_x] = tsugi
                    # tsugi = 0
                    if tsugi == 1:
                        tsugi = 2
                    else:
                        tsugi = 1
                index = 3
        cvs.delete("CURSOR")
        cvs.create_image(cursor_x*72+60, cursor_y*72 +
                         60, image=cursor, tag="CURSOR")
        draw_neko()
    elif index == 6:  # 結果表示
        timer = timer + 1
        if timer == 1:
            # draw_txt("GAME OVER", 312, 348, 60, "red", "OVER")
            draw_txt(result, 312, 348, 60, "red", "OVER")
        if timer == 30:
            cvs.delete("OVER")
            timer = 0
            index = 0
    cvs.delete("INFO")
    # draw_txt("SCORE" + str(score), 160, 60, 32, "blue", "INFO")
    # draw_txt("HISC" + str(hisc), 450, 60, 32, "yellow", "INFO")
    if tsugi > 0:
        cvs.create_image(752, 128, image=img_neko[tsugi], tag="INFO")
    root.after(100, game_main)
    # if 660 <= mouse_x < 840 and 100 <= mouse_y < 160 and mouse_c == 1:
    #     mouse_c = 0
    #     check_neko()
    # if 24 <= mouse_x < 24+72*8 and 24 <= mouse_y < 24+72*10:
    #     cursor_x = int((mouse_x-24)/72)
    #     cursor_y = int((mouse_y-24)/72)
    #     if mouse_c == 1:
    #         mouse_c = 0
    #         neko[cursor_y][cursor_x] = random.randint(1, 2)
    # cvs.delete("CURSOR")
    # cvs.create_image(cursor_x*72+60, cursor_y*72 +
    #                  60, image=cursor, tag="CURSOR")
    # cvs.delete("NEKO")
    # draw_neko()
    # root.after(100, game_main)


root = tk.Tk()
root.title("落ち物パズル「ねこねこ」")
root.resizable(False, False)
root.bind("<Motion>", mouse_move)
root.bind("<ButtonPress>", mouse_press)
cvs = tk.Canvas(root, width=912, height=768)
cvs.pack()

bg = tk.PhotoImage(file="nekopzl/images/neko_bg.png")
cursor = tk.PhotoImage(file="nekopzl/images/neko_cursor.png")
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
game_main()
root.mainloop()
