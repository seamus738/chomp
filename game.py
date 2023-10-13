import pygame
import time
import sys

print(f'the quit event is type {pygame.QUIT}')
#Quit=256

pygame.init()

screen=pygame.display.set_mode((400,400))
pygame.display.set_caption("Chomp!!")

# for color
screen.fill((100,200,255))

#make a rectangle
pygame.draw.rect(screen, (100,25,0), (0,380, 400, 400))
pygame.draw.rect(screen,(100,200,0), (200, 200, 25, 25))
sand = pygame.image.load("assets/images/sand.png").convert()
screen.blit(sand, (200,200, 64, 64))
#.convert() will make an image transparent
pygame.display.flip()

while True:
    #could use: if event.type==pygame.QUIT: or -->
    for event in pygame.event.get():
        if event.type==256:
            print('thank you for playing')
            pygame.quit()
            sys.exit()



