import pygame
import random
from settings import *
from player_class import *
class Ghost(pygame.sprite.Sprite):
    "Create a ghost srpite"
    def __init__(self, app, x, y, width, height, color, pacman, personality="random"):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.app = app
        self.rect = self.image.get_rect(center=(x, y))
        self.move = vector(0, -1)
        self.walls = None
        self.personality = personality
        self.state = 'normal'
        self.color = color
        self.pacman = pacman

    def update(self):
        if self.app.state == 'playing_top':
            # if the ghost hits a left or right wall, change the y direction
            if self.rect.x >= self.pacman.rect.x:
                self.move.x = -1
            else:
                self.move.x = 1
            self.rect.x += self.move.x + random.choice([-1, 1])
            if self.walls != None:
                block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
                for block in block_hit_list:
                    if self.move.x > 0:
                        self.rect.right = block.rect.left
                        self.move.y = -1
                        self.move.x = 0
                    else:
                        self.rect.left = block.rect.right
                        self.move.y = 1
                        self.move.x = 0
            # if the ghost hits a top or bottom wall, change the x direction
            if self.rect.y >= self.pacman.rect.y:
                self.move.y = -1
            else:
                self.move.y = 1
            self.rect.y += self.move.y +  + random.choice([-1, 1])
            if self.walls != None:
                block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
                for block in block_hit_list:
                    if self.move.y > 0:
                        self.rect.bottom = block.rect.top
                        self.move.x = random.choice([-1, 1])
                        self.move.y = 0
                    else:
                        self.rect.top = block.rect.bottom
                        self.move.x = random.choice([-1, 1])
                        self.move.y = 0



        elif self.app.state == 'playing_square':
            self.rect.x += self.move.x
            # if the ghost hits a left or right wall, change the y direction
            if self.walls != None:
                block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
                for block in block_hit_list:
                    if self.move.x > 0:
                        self.rect.right = block.rect.left
                        self.move.y = random.choice([-1, 1])
                        self.move.x = 0
                    else:
                        self.rect.left = block.rect.right
                        self.move.y = random.choice([-1, 1])
                        self.move.x = 0
            # if the ghost hits a top or bottom wall, change the x direction
            self.rect.y += self.move.y
            if self.walls != None:
                block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
                for block in block_hit_list:
                    if self.move.y > 0:
                        self.rect.bottom = block.rect.top
                        self.move.x = -1
                        self.move.y = 0
                    else:
                        self.rect.top = block.rect.bottom
                        self.move.x = 1
                        self.move.y = 0



    def change_state(self):
        if self.state == 'normal':
            self.state = 'reversed'
            self.image.fill(dark_blue)
        elif self.state == 'reversed':
            self.state = 'normal'
            self.image.fill(self.color)