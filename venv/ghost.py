import pygame
import random
from settings import *
class Ghost(pygame.sprite.Sprite):
    def __init__(self, app, x, y, width, height, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.app = app
        self.rect = self.image.get_rect(center=(x, y))
        self.move = vector(0, 0)
        self.walls = None

    def update(self):
        self.rect.x += 0
        self.rect.y += 0
        
        if self.walls != None:
            block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
            for block in block_hit_list:
                if self.move.x > 0:
                    self.rect.right = block.rect.left
                else:
                    self.rect.left = block.rect.right
        if self.walls != None:
            block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
            for block in block_hit_list:
                if self.move.y > 0:
                    self.rect.bottom = block.rect.top
                else:
                    self.rect.top = block.rect.bottom