import pygame
import os

WIDTH,HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SpaceInvaders Game!")




YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('assets', 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('assets', 'spaceship_red.png'))
SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('assets', 'space.png')), (WIDTH, HEIGHT))


WHITE = (255, 255, 255)

def draw_window():
    WIN.fill(WHITE)
    WIN.blit(SPACE, (0,0))
    pygame.display.update()

def main():
    run =  True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
    pygame.quit()

if __name__ =="__main__":
    main()
