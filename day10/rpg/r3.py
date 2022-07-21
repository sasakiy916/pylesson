import pygame
import sys
import random

images = "day10/rpg/images/"
BLACK = (0, 0, 0)
# CYAN = (0, 255, 255)
# GRAY = (96, 96, 96)

MAZE_W = 11
MAZE_H = 9
maze = []
for y in range(MAZE_H):
    maze.append([0]*MAZE_W)

# 迷路の幅を3倍にする
DUNGEON_W = MAZE_W*3
DUNGEON_H = MAZE_H*3
dungeon = []
# 縦横をそれぞれ3倍にした(27行33列)2次元配列をθで初期化
for y in range(DUNGEON_H):
    dungeon.append([0]*DUNGEON_W)
# 画像をロード
imgWall = pygame.image.load(f"{images}wall.png")
imgFloor = pygame.image.load(f"{images}floor.png")
imgPlayer = pygame.image.load(f"{images}player.png")

pl_x = 4
pl_y = 4


def make_dungeon():  # ダンジョンの自動生成
    XP = [0, 1, 0, -1]
    YP = [-1, 0, 1, 0]
    # 周りの壁
    for x in range(MAZE_W):
        maze[0][x] = 1
        maze[-1][x] = 1
    for y in range(1, MAZE_H-1):
        maze[y][0] = 1
        maze[y][-1] = 1
    # 中を何もない状態に
    for y in range(1, MAZE_H-1):
        for x in range(1, MAZE_W-1):
            maze[y][x] = 0

    # 柱
    for y in range(2, MAZE_H-2, 2):
        for x in range(2, MAZE_W-2, 2):
            maze[y][x] = 1
    # 柱から上下左右に壁を作る
    for y in range(2, MAZE_H-2, 2):
        for x in range(2, MAZE_W-2, 2):
            d = random.randint(0, 3)
            if x > 2:  # 二列目からは左に壁を作らない
                d = random.randint(0, 2)
            maze[y+YP[d]][x+XP[d]] = 1

    # 迷路からダンジョンを作る
    # 全体を壁にする
    for y in range(DUNGEON_H):
        for x in range(DUNGEON_W):
            dungeon[y][x] = 9
    # 部屋と通路の配置
    for y in range(1, MAZE_H-1):
        for x in range(1, MAZE_W-1):
            dx = x*3+1
            dy = y*3+1
            if maze[y][x] == 0:
                if random.randint(0, 99) < 20:  # 部屋(3x3)を作る
                    for ry in range(-1, 2):
                        for rx in range(-1, 2):
                            dungeon[dy+ry][dx+rx] = 0
                else:  # 通路を作る(maze配列の上下左右をチェックして0だった場合はそこに繋がるように0を入れる)
                    dungeon[dy][dx] = 0
                    if maze[y-1][x] == 0:
                        dungeon[dy-1][dx] = 0
                    if maze[y+1][x] == 0:
                        dungeon[dy+1][dx] = 0
                    if maze[y][x-1] == 0:
                        dungeon[dy][dx-1] = 0
                    if maze[y][x+1] == 0:
                        dungeon[dy][dx+1] = 0


def draw_dungeon(bg):  # ダンジョンを描画する
    bg.fill(BLACK)  # 全体を黒く塗りつぶす
    for y in range(-5, 6):
        for x in range(-5, 6):
            X = (x+5)*16  # 画像を貼る際のx座標
            Y = (y+5)*16  # 画像を貼る際のy座標
            dx = pl_x+x  # プレイヤーの現在座標に基づくx_index
            dy = pl_y+y
            # indexがmapの中に入っていたら画像を貼る(そうでなかったら黒のまま)
            if 0 <= dx < DUNGEON_W and 0 <= dy < DUNGEON_H:
                if dungeon[dy][dx] == 0:
                    bg.blit(imgFloor, [X, Y])
                if dungeon[dy][dx] == 9:
                    bg.blit(imgWall, [X, Y])
            if x == 0 and y == 0:  # ウインドウの中央に主人公を表示
                bg.blit(imgPlayer, [X, Y-8])


def move_player():  # 主人公の移動
    global pl_x, pl_y
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] == 1:
        if dungeon[pl_y-1][pl_x] != 9:
            pl_y = pl_y-1
    if key[pygame.K_DOWN] == 1:
        if dungeon[pl_y+1][pl_x] != 9:
            pl_y = pl_y+1
    if key[pygame.K_LEFT] == 1:
        if dungeon[pl_y][pl_x-1] != 9:
            pl_x = pl_x-1
    if key[pygame.K_RIGHT] == 1:
        if dungeon[pl_y][pl_x+1] != 9:
            pl_x = pl_x+1


def main():
    pygame.init()
    pygame.display.set_caption("ダンジョン内を歩く")
    screen = pygame.display.set_mode((176, 176))
    clock = pygame.time.Clock()

    make_dungeon()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        move_player()
        draw_dungeon(screen)
        pygame.display.update()
        clock.tick(5)


if __name__ == "__main__":
    main()
