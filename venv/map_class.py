import pygame
from settings import *
from tile_class import *
from fruit_class import *
from bar_class import *
class Map(pygame.sprite.Sprite):
    """
    Creates a Map
        #-#--MAP KEY--#-#
            w: wall
            .: fruit
            b: bar
            b: bar
            e: empty
    """
    def __init__(self, app):
        pygame.sprite.Sprite.__init__(self)
        self.app = app
        self.all_sprite_list = pygame.sprite.Group()
        self.wall_list = pygame.sprite.Group()
        self.fruit_list = pygame.sprite.Group()
        self.map_file = open("D:/2020/Trimester 2/3815ICT Software Engineering/pacman_new/venv/map.txt", 'r')

    def draw(self):
        x, y = 0, 0
        for line in self.map_file:
            letters = self._split_line(line)
            x=0
            # draw a sprite depending on the input from map.txt
            for letter in letters:
                if letter == 'w':
                    tile = Tile(x*self.app.cell_width, y*self.app.cell_height, self.app.cell_width, self.app.cell_height, blue)
                    self.all_sprite_list.add(tile)
                    self.wall_list.add(tile)
                if letter == 'b':
                    bar = Bar(x*self.app.cell_width, y * self.app.cell_height + self.app.cell_height // 2, self.app.cell_width, self.app.cell_height // 5, ghost_pink)
                    self.all_sprite_list.add(bar)
                if letter == '.':
                    fruit = Fruit(int(x*self.app.cell_width + self.app.cell_width//2), int(y*self.app.cell_height + self.app.cell_height//2), self.app.cell_width//5, self.app.cell_height//5, white)
                    self.all_sprite_list.add(fruit)
                    self.fruit_list.add(fruit)
                x+=1
            y+=1

    # splits a line/word into the letters
    def _split_line(self, line):
        return [char for char in line]