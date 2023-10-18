import pygame
import time
import sys

print(f'the quit event is type {pygame.QUIT}')
#Quit=256

#DIMENSIONS
SCREEN_WIDTH=400
SCREEN_HEIGHT=400
SAND_HEIGHT=20
TITLE_SIZE=64
pygame.init()

#COLORS
WATER_COLOR=(100,200,255)
SAND_COLOR=(100,25,0)

screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chomp!!")

# for color
screen.fill(WATER_COLOR)

#make a rectangle
pygame.draw.rect(screen, SAND_COLOR, (0,SCREEN_HEIGHT-SAND_HEIGHT,
                                      SCREEN_WIDTH, SAND_HEIGHT))
pygame.draw.rect(screen,(100,200,0), (200, 200, 25, 25))
sand = pygame.image.load("assets/images/sand.png").convert()
screen.blit(sand, (SCREEN_WIDTH / 2 - TITLE_SIZE / 2,
                   SCREEN_HEIGHT / 2 - TITLE_SIZE / 2))
#.convert() will make an image transparent
pygame.display.flip()

while True:
    #could use: if event.type==pygame.QUIT: or -->
    for event in pygame.event.get():
        if event.type==256:
            print('thank you for playing')
            pygame.quit()
            sys.exit()



