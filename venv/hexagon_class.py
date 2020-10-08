import pygame
import math
from settings import *
import os

game_folder = os.path.dirname(__file__)
class Hexagon(pygame.sprite.Sprite):
    "Create a bar sprite"
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(game_folder, 'hex_back.png')).convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
