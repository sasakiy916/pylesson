import pygame
import sys

#色定義(rgb)
WHITE=(255,255,255)
BLACK=(0,0,0)

def main():
    pygame.init() #初期化処理
    pygame.display.set_caption("My Game")
    screen = pygame.display.set_mode((800,600))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None,80)
    tmr = 0

    while True:
        tmr = tmr+1
        #以下のfor文はpygameで処理を終える時の提携
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        txt=font.render(str(tmr),True,WHITE)
        screen.fill(BLACK)
        screen.blit(txt,[300,200])
        pygame.display.update()
        clock.tick(10)

if __name__ == "__main__":
    main()
