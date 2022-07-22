import pygame
import sys

images = "day10/rpg/images/"
WHITE = (255, 255, 255)

# 背景は最初にロード
imgBtlBG = pygame.image.load(f"{images}btlbg.png")
# 敵画像は出現のたびにロードする
imgEnemy = None

emy_num = 0  # 敵index
emy_x = 0  # 敵画像を表示する際のx座標
emy_y = 0  # y座標


def init_battle():
    global imgEnemy, emy_num, emy_x, emy_y
    emy_num = emy_num+1
    if emy_num == 5:
        emy_num = 1
    # 敵画像をロード
    imgEnemy = pygame.image.load(f"{images}enemy{str(emy_num)}.png")
    # 足元の位置(440,560)を元に座標を算出(画像の大きさは違っても足元の位置は同じ)
    emy_x = 440-imgEnemy.get_width()/2
    emy_y = 560-imgEnemy.get_height()


def draw_battle(bg, fnt):
    # 背景を配置
    bg.blit(imgBtlBG, [0, 0])
    # 敵画像を配置
    bg.blit(imgEnemy, [emy_x, emy_y])
    # 文言を作成
    sur = fnt.render(f"{images}enemy{str(emy_num)}.png", True, WHITE)
    # 文言を配置
    bg.blit(sur, [360, 580])


def main():
    pygame.init()
    pygame.display.set_caption("戦闘開始の処理")
    screen = pygame.display.set_mode((880, 720))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 40)

    init_battle()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    init_battle()

        draw_battle(screen, font)
        pygame.display.update()
        clock.tick(5)


if __name__ == "__main__":
    main()
