import pygame
from settings import *
class Fruit(pygame.sprite.Sprite):
    "Create a fruit sprite"
    def __init__(self, x, y, width, height, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))