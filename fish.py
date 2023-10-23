import pygame
from settings import *


class Fish(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/images/orange_fish.png")
        self.image.set_colorkey((0, 0, 0))
        self.x= x
        self.y= y
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        print("I am a brand new fish")
        pass



    def update(self):
        if self.moving_left:
            self.x-=2
        elif self.moving_right:
            self.x += 2
        elif self.moving_up:
            self.y -=2
        elif self.moving_down:
            self.y += 2
        if self.x<0:
            self.x=0
        if self.x>SCREEN_WIDTH-TITLE_SIZE:
            self.x=SCREEN_WIDTH-TITLE_SIZE
        if self.y<0:
            self.y=0
        if self.y>SCREEN_HEIGHT-3*TITLE_SIZE:
            self.y=SCREEN_HEIGHT-3*TITLE_SIZE




    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))