import pygame
import math
from settings import *

from tile_class import *
from fruit_class import *
from bar_class import *
from special_class import *
from hexagon_class import *

class Map(pygame.sprite.Sprite):
    """
    Creates a Map
        #-#--MAP KEY--#-#
            w: wall
            .: fruit
            b: bar
            b: bar
            e: empty
            s: special
    """
    def __init__(self, app):
        pygame.sprite.Sprite.__init__(self)
        self.app = app
        self.all_sprite_list = pygame.sprite.Group()
        self.wall_list = pygame.sprite.Group()
        self.fruit_list = pygame.sprite.Group()
        self.special_list = pygame.sprite.Group()
        self.map_file = open("E:\\2020\Trimester 2\\3815ICT Software Engineering\\milestone2\\pacman\\pacmanNew\\venv\\map.txt", 'r')
        self.top_map = open("E:\\2020\Trimester 2\\3815ICT Software Engineering\\milestone2\\pacman\\pacmanNew\\venv\\top_file.txt", 'r')

    def draw(self, map_type):
        if map_type == 'square':
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
                    if letter == 's':
                        special = Special(int(x*self.app.cell_width + self.app.cell_width//5), int(y*self.app.cell_height + self.app.cell_height//5), self.app.cell_width//2, self.app.cell_height//2, ghost_red)
                        self.all_sprite_list.add(special)
                        self.special_list.add(special)
                    if letter == '.':
                        fruit = Fruit(int(x*self.app.cell_width + self.app.cell_width//2), int(y*self.app.cell_height + self.app.cell_height//2), self.app.cell_width//5, self.app.cell_height//5, white)
                        self.all_sprite_list.add(fruit)
                        self.fruit_list.add(fruit)
                    x+=1
                y+=1
        elif map_type == 'hex':
            x, y = 0, 0
            for line in self.top_map:
                letters = self._split_line(line)
                x = 0
                # draw a sprite depending on the input from map.txt
                for letter in letters:
                    if letter == 'w':
                        tile = Tile(x * self.app.cell_width, y * self.app.cell_height, self.app.cell_width,
                                    self.app.cell_height, blue)
                        self.all_sprite_list.add(tile)
                        self.wall_list.add(tile)
                    if letter == '.':
                        fruit = Fruit(int(x * self.app.cell_width + self.app.cell_width // 2),
                                      int(y * self.app.cell_height + self.app.cell_height // 2),
                                      self.app.cell_width // 5, self.app.cell_height // 5, white)
                        self.all_sprite_list.add(fruit)
                        self.fruit_list.add(fruit)
                    x += 1
                y += 1

            hex_size = 20
            grid_x_pixels = 0.9 * maze_width
            grid_y_pixels = 0.9 + maze_height
            sep_x = 3 * hex_size
            sep_y = 0.86 * hex_size
            grid_x = int(grid_x_pixels / sep_x) + 1
            grid_y = int(grid_y_pixels / sep_y) + 1
            current_x = int(maze_width/2.0 - grid_x_pixels/2.0)
            current_y = int(maze_height/2.0 - grid_y_pixels/2.0)
            for i in range(grid_y):
                if i%2 == 0:
                    current_x = 2.7 * hex_size
                for j in range(grid_x):
                    self.draw_hexagon(current_x, current_y, hex_size)
                    current_x += sep_x
                current_x = maze_width / 2.0 - grid_x_pixels / 2.0
                current_y += sep_y
            hex = Hexagon(100, 100)
            self.all_sprite_list.add(hex)
            self.wall_list.add(hex)



        elif map_type == 'top':
            x, y = 0, 0
            for line in self.top_map:
                letters = self._split_line(line)
                x = 0
                # draw a sprite depending on the input from map.txt
                for letter in letters:
                    if letter == 'w':
                        tile = Tile(x * self.app.cell_width, y * self.app.cell_height, self.app.cell_width,
                                    self.app.cell_height, blue)
                        self.all_sprite_list.add(tile)
                        self.wall_list.add(tile)
                    if letter == '.':
                        fruit = Fruit(int(x*self.app.cell_width + self.app.cell_width//2), int(y*self.app.cell_height + self.app.cell_height//2), self.app.cell_width//5, self.app.cell_height//5, white)
                        self.all_sprite_list.add(fruit)
                        self.fruit_list.add(fruit)
                    x += 1
                y += 1

    # splits a line/word into the letters
    def _split_line(self, line):
        return [char for char in line]

    def draw_hexagon(self, x, y, side):
        x = int(x)
        y = int(y)
        pygame.draw.line(self.app.background,
                         grey,
                           # 1
                         [x + side * math.sin(math.pi / 2), y + side * math.cos(math.pi / 2)],
                          # 2
                         [x + side * math.sin(math.pi / 6), y + side * math.cos(math.pi / 6)])

        pygame.draw.line(self.app.background,
                         grey,
                          # 2
                         [x + side * math.sin(math.pi / 6), y + side * math.cos(math.pi / 6)],
                          # 3
                         [x + side * math.sin(11 * math.pi / 6), y + side * math.cos(11 * math.pi / 6)])
        pygame.draw.line(self.app.background,
                         grey,
                         # 3
                         [x + side * math.sin(11 * math.pi / 6), y + side * math.cos(11 * math.pi / 6)],
                         # 4
                         [x + side * math.sin(3 * math.pi / 2), y + side * math.cos(3 * math.pi / 2)])
        pygame.draw.line(self.app.background,
                         grey,
                         # 4
                         [x + side * math.sin(3 * math.pi / 2), y + side * math.cos(3 * math.pi / 2)],
                         # 5
                         [x + side * math.sin(7 * math.pi / 6), y + side * math.cos(7 * math.pi / 6)])
        pygame.draw.line(self.app.background,
                         grey,
                         # 5
                         [x + side * math.sin(7 * math.pi / 6), y + side * math.cos(7 * math.pi / 6)],
                         # 6
                         [x + side * math.sin(5 * math.pi / 6), y + side * math.cos(5 * math.pi / 6)])
        pygame.draw.line(self.app.background,
                         grey,
                         # 6
                         [x + side * math.sin(5 * math.pi / 6), y + side * math.cos(5 * math.pi / 6)],
                         # 1
                         [x + side * math.sin(math.pi / 2), y + side * math.cos(math.pi / 2)])