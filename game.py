import pygame
import sys
import random
import fish


print(f'the quit event is type {pygame.QUIT}')
# Quit=256

from settings import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chomp!!")

# for color
screen.fill(WATER_COLOR)

# make a rectangle


game_font=pygame.font.Font('assets/fonts/Black_Crayon.ttf', 128)

sand = pygame.image.load("assets/images/sand.png").convert()
    # .convert() will make an image transparent
sandtop = pygame.image.load("assets/images/sand_top.png").convert()
sandtop.set_colorkey((0, 0, 0))
seaweed = pygame.image.load("assets/images/seagrass.png").convert()
seaweed.set_colorkey((0, 0, 0))
my_fish=fish.Fish(200, 200) #create a new fish

background=screen.copy()

def draw_background():
    background.fill(WATER_COLOR)

    for i in range(SCREEN_WIDTH // TITLE_SIZE):
        background.blit(sand, (TITLE_SIZE*i, SCREEN_HEIGHT-TITLE_SIZE))
    # BLIT SAND TITLES ACROSS THE BOTTOM OF THE SCREEN

    # use this to fill the black pixel with the background
    for i in range(SCREEN_WIDTH // TITLE_SIZE):
        background.blit(sandtop, (TITLE_SIZE*i, SCREEN_HEIGHT-2*TITLE_SIZE))

    for _ in range(4):
        y=random.randint(SCREEN_HEIGHT-2*TITLE_SIZE, SCREEN_HEIGHT)-(.5*TITLE_SIZE)
        x=random.randint(0, SCREEN_WIDTH)
        background.blit(seaweed, (x, y))

    #draw chomp title
    text=game_font.render("Chomp!", True, (255, 69, 0))
    background.blit(text, (SCREEN_WIDTH//2-text.get_width()//2,SCREEN_HEIGHT//2-text.get_height()//2))

pygame.display.flip()
draw_background()


while True:
    # could use: if event.type==pygame.QUIT: or -->
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('thank you for playing')
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:

            if event.key==pygame.K_LEFT:
                my_fish.move_left()

            if event.key==pygame.K_RIGHT:
                my_fish.move_right()

            if event.key==pygame.K_UP:
                my_fish.move_up()
                
            if event.key==pygame.K_DOWN:
                my_fish.move_down()

    #update the game screen
    screen.blit(background,(0,0))
    my_fish.draw(screen)
    pygame.display.flip()