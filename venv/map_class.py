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
            e: empty
        """
    def __init__(self, app):
        pygame.sprite.Sprite.__init__(self)
        self.app = app
        self.all_sprite_list = pygame.sprite.Group()
        self.map = """wwwwwwwwwwwwwwwwwww
w........w........w
w.ww.www.w.www.ww.w
w.................w
w.ww.w.wwwww.w.ww.w
w....w...w...w....w
wwww.www.w.www.wwww
eeew.w.......w.weee
wwww.w.wwbww.w.wwww
.......weeew.......
wwww.w.wwwww.w.wwww
eeew.w...e...w.weee
wwww.w.wwwww.w.wwww
w........w........w
w.ww.www.w.www.ww.w
w..w...........w..w
ww.w.w.wwwww.w.w.ww
w....w...w...w....w
w.wwwwww.w.wwwwww.w
w.................w
wwwwwwwwwwwwwwwwwww"""

    def draw(self):
        map_lines = self.map.splitlines()
        wall = pygame.sprite.Group()
        for y, lines in enumerate(map_lines):
            for x, letter in enumerate(lines):
                if letter == 'w':
                    tile = Tile(x*self.app.cell_width, y*self.app.cell_height, self.app.cell_width, self.app.cell_height, blue)
                    self.all_sprite_list.add(tile)
                if letter == 'b':
                    bar = Bar(x*self.app.cell_width, y * self.app.cell_height + self.app.cell_height // 2, self.app.cell_width, self.app.cell_height // 5, ghost_pink)
                    self.all_sprite_list.add(bar)
                if letter == '.':
                    fruit = Fruit(int(x*self.app.cell_width + self.app.cell_width//2), int(y*self.app.cell_height + self.app.cell_height//2), self.app.cell_width//5, self.app.cell_height//5, white)
                    self.all_sprite_list.add(fruit)