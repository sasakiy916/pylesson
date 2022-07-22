import pygame
import sys
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
images = "day10/rpg/images/"

imgBtlBG = pygame.image.load(f"{images}btlbg.png")
imgEnemy = pygame.image.load(f"{images}enemy1.png")
emy_x = 440 - imgEnemy.get_width()/2
emy_y = 560 - imgEnemy.get_height()

message = [""]*10


def init_message():
    for i in range(10):
        message[i] = ""


def set_message(msg):
    for i in range(10):
        if message[i] == "":
            message[i] = msg
            return
    for i in range(9):
        message[i] = message[i+1]
    message[9] = msg


def draw_text(bg, txt, x, y, fnt, col):
    # 黒で文字の影を作成
    sur = fnt.render(txt, True, BLACK)
    bg.blit(sur, [x+1, y+2])
    # 文言を影の上に表示
    sur = fnt.render(txt, True, col)
    bg.blit(sur, [x, y])


def draw_battle(bg, fnt):
    bg.blit(imgBtlBG, [0, 0])
    bg.blit(imgEnemy, [emy_x, emy_y])
    for i in range(10):
        draw_text(bg, message[i], 600, 100+i*50, fnt, WHITE)


def main():
    pygame.init()
    pygame.display.set_caption("戦闘中のメッセージ")
    screen = pygame.display.set_mode((800, 720))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 40)

    init_message()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                set_message("KEYDOWN "+str(event.key))

        draw_battle(screen, font)
        pygame.display.update()
        clock.tick(5)


if __name__ == "__main__":
    main()
