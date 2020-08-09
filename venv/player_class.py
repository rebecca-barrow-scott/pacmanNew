import pygame
from settings import *
from map_class import *

class Player(pygame.sprite.DirtySprite):
    def __init__(self, app, x, y, width, height, color=pacman_yellow):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x,y))
        self.move = vector(0, 0)
        self.app = app
        self.map = None
        self.fruit = None
        self.score = 0

    def changeSpeed(self, x, y):
        self.move.x += x
        self.move.y += y

    def update(self):
        # move the player in the direction of the arrow key
        self.rect.x += self.move.x
        self.rect.y += self.move.y
        if self.map != None:
            block_hit_list = pygame.sprite.spritecollide(self, self.map, False)
            for block in block_hit_list:
                if self.move.x > 0:
                    self.rect.right = block.rect.left
                elif self.move.x < 0:
                    self.rect.left = block.rect.right
                elif self.move.y > 0:
                    self.rect.bottom = block.rect.top
                elif self.move.y < 0:
                    self.rect.top = block.rect.bottom
        # move the player to the other side of the screen
        if self.rect.x <= -5:
            self.rect.x = width
        if self.rect.x >= width+5:
            self.rect.x = -5
        # player eats fruit
        if self.fruit != None:
            hit_list = pygame.sprite.spritecollide(self, self.fruit, True)
            for hit in hit_list:
                self.score+=1
        self.dirty = 1


    def _split_letters(self, word):
        return [char for char in word]

    def _join_word(self, letters):
        word = letters[0]
        for i in range(1, len(letters)):
            word += letters[i]
        return word
