import pygame
import sys


def main():
    pygame.init()
    pygame.display.set_caption("My Game")
    screen = pygame.display.set_mode((640, 360))
    clock = pygame.time.Clock()

    images = "pygame/images/"
    # 画像をロード
    img_bg = pygame.image.load(f"{images}pg_bg.png")
    # 2枚の画像をリストに入れる
    img_chara = [
        pygame.image.load(f"{images}pg_chara0.png"),
        pygame.image.load(f"{images}pg_chara1.png"),
    ]
    tmr = 0
    while True:
        tmr = tmr+1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 何かしらキーが押されたら
            if event.type == pygame.KEYDOWN:
                # F1キーだったら
                if event.key == pygame.K_F1:
                    # フルスクリーンモードに変更
                    screen = pygame.display.set_mode(
                        (640, 360), pygame.FULLSCREEN)
                if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                    screen = pygame.display.set_mode((640, 360))
        # オフセットさせる量(0~159)
        x = tmr % 160
        # 背景を5枚敷き詰める
        for i in range(5):
            # 配置する(毎フレーム←に1ドットずつずらして配置)
            screen.blit(img_bg, [i*160-x, 0])
        # 2枚の絵を交互に配置
        screen.blit(img_chara[tmr % 2], [224, 160])
        pygame.display.update()
        clock.tick(5)


if __name__ == "__main__":
    main()
