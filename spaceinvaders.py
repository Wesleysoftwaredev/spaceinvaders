import pygame
import os

WIDTH,HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SpaceInvaders Game!")

VEL = 5
FPS = 60


WHITE = (255, 255, 255)
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40


YELLOW_SPACESHIP_IMAGE = (pygame.image.load(os.path.join('assets', 'spaceship_yellow.png')))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_HEIGHT, SPACESHIP_WIDTH)),90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_HEIGHT, SPACESHIP_WIDTH)),90)

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'space.png')), (WIDTH, HEIGHT))


def draw_window(red,yellow):
    WIN.fill(WHITE)
    WIN.blit(SPACE, (0,0))
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()

def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    clock = pygame.time.Clock()
    run =  True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]:
            yellow.x -= VEL
        if keys_pressed[pygame.K_w]:
            yellow.y -= VEL
        if keys_pressed[pygame.K_d]:
            yellow.x += VEL
        if keys_pressed[pygame.K_s]:
            yellow.y += VEL
    
        
        
        draw_window(red,yellow)
    pygame.quit()

if __name__ =="__main__":
    main()
