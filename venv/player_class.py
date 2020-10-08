import pygame
from settings import *
from map_class import *
import pygame.gfxdraw
class Player(pygame.sprite.DirtySprite):
    "Create a player sprite"
    def __init__(self, app, x, y, width, height, color=pacman_yellow):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = pygame.Surface([width, height], pygame.SRCALPHA)
        self.image.fill(color)
        # pygame.gfxdraw.aacircle(self.image,x, y, 5, blue)
        # pygame.gfxdraw.filled_circle(self.image, x, y, 5, blue)
        self.rect = self.image.get_rect(center=(x,y))
        self.move = vector(0, 0)
        self.app = app
        self.map = None
        self.fruit = None
        self.ghosts = None
        self.special = None
        self.state = 'normal'
        # initialise player attributes
        self.score = 0
        self.lives = 3
        #self.stored_path = None

    def change_dir(self, x, y):
        self.move.x += x
        self.move.y += y

    def update(self):
        # move the player in the direction of the arrow key
        self.rect.x += self.move.x
        # stop player from going through a wall
        if self.map != None:
            block_hit_list = pygame.sprite.spritecollide(self, self.map, False)
            for block in block_hit_list:
                if self.move.x > 0:
                    self.rect.right = block.rect.left
                else:
                    self.rect.left = block.rect.right
        # move player and stop them from going through a wall
        self.rect.y += self.move.y
        if self.map != None:
            block_hit_list = pygame.sprite.spritecollide(self, self.map, False)
            for block in block_hit_list:
                if self.move.y > 0:
                    self.rect.bottom = block.rect.top
                else:
                    self.rect.top = block.rect.bottom
        # move the player to the other side of the screen
        if self.rect.x < 5:
            self.rect.x = width
        if self.rect.x >= width+5:
            self.rect.x = 5
        # player collides with fruit
        if self.fruit != None:
            hit_list = pygame.sprite.spritecollide(self, self.fruit, True)
            for hit in hit_list:
                self.score+=1

        # player collides with special
        if self.special != None:
            hit_list = pygame.sprite.spritecollide(self, self.special, True)
            for hit in hit_list:
                self.state = 'reversed'
        # player collides with ghost
        if self.ghosts != None:
            hit_list = pygame.sprite.spritecollide(self, self.ghosts, True)
            for hit in hit_list:
                if self.state == 'reversed':
                    self.score += 100
                    self.rect.x = self.app.cell_width * 9
                    self.rect.y = self.app.cell_height * 11
                    self.state = 'normal'
                else:
                    if self.lives == 1:
                        self.app.state = "game_over"
                    else:
                        self.lives -= 1
                        self.rect.x = self.app.cell_width*9
                        self.rect.y = self.app.cell_height*11
        self.dirty = 1
