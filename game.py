import pygame
import sys

print(f'the quit event is type {pygame.QUIT}')
# Quit=256

# DIMENSIONS
TITLE_SIZE = 64
SCREEN_WIDTH = 8*TITLE_SIZE
SCREEN_HEIGHT = 8*TITLE_SIZE
SAND_HEIGHT = 20

pygame.init()

# COLORS
WATER_COLOR = (100, 200, 255)
SAND_COLOR = (100, 25, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chomp!!")

# for color
screen.fill(WATER_COLOR)

# make a rectangle
pygame.draw.rect(screen, SAND_COLOR, (0, SCREEN_HEIGHT - SAND_HEIGHT,
                                      SCREEN_WIDTH, SAND_HEIGHT))
pygame.draw.rect(screen, (100, 200, 0), (200, 200, 25, 25))
sand = pygame.image.load("assets/images/sand.png").convert()
# .convert() will make an image transparent

for i in range(SCREEN_WIDTH // TITLE_SIZE):
    screen.blit(sand, (TITLE_SIZE*i, SCREEN_HEIGHT-TITLE_SIZE))
# BLIT SAND TITLES ACROSS THE BOTTOM OF THE SCREEN
sandtop = pygame.image.load("assets/images/sand_top.png").convert()
sandtop.set_colorkey((0, 0, 0))
# use this to fill the black pixel with the background
for i in range(SCREEN_WIDTH // TITLE_SIZE):
    screen.blit(sandtop, (TITLE_SIZE*i, SCREEN_HEIGHT-2*TITLE_SIZE))

# .convert() will make an image transparent
pygame.display.flip()

while True:
    # could use: if event.type==pygame.QUIT: or -->
    for event in pygame.event.get():
        if event.type == 256:
            print('thank you for playing')
            pygame.quit()
            sys.exit()
