import pygame
import sys

from settings import *
from map_class import *
pygame.init()
vector = pygame.math.Vector2

class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'intro'
        self.cell_width = maze_width//19
        self.cell_height = maze_height//21
        self.map = Map(self)
        self.load()


    def run(self):
        while self.running:
            if self.state == 'intro':
                self.intro_events()
                self.intro_update()
                self.intro_draw()
            elif self.state == 'playing':
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            else:
                self.running = False
            self.clock.tick(fps)
        pygame.quit()
        sys.exit()

    #-#-- HELPER FUNCTIONS --#-#
    def draw_text(self, text, pos, font_size, color, font_name):
        font = pygame.font.SysFont(font_name, font_size)
        rend_text = font.render(text, False, color)
        text_size = rend_text.get_size()
        pos[0] = pos[0]-text_size[0]//2
        pos[1] = pos[1] - text_size[1] // 2
        self.screen.blit(rend_text, pos)

    def load(self):
        self.background = pygame.Surface((maze_width, maze_height))


    def draw_grid(self):
        for w in range(width//self.cell_width):
            pygame.draw.line(self.background, ghost_orange, (w*self.cell_width, 0), (w*self.cell_width, height))
        for h in range(height//self.cell_height):
            pygame.draw.line(self.background, ghost_orange, (0, h*self.cell_height), (width, h*self.cell_height))

    #-#-- STATE FUNCTIONS --#-#
    # INTRO
    def intro_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'

    def intro_update(self): pass

    def intro_draw(self):
        self.screen.fill(black)
        self.draw_text('WELCOME TO PACMAN', [width//2, height//2-97],intro_text_size_title, ghost_red, intro_font)
        self.draw_text('WELCOME TO PACMAN', [width//2+2, height//2-100],intro_text_size_title, purple, intro_font)
        self.draw_text('WELCOME TO PACMAN',  [width//2, height//2-100],intro_text_size_title, pacman_yellow, intro_font)
        self.draw_text('PRESS SPACEBAR TO START', [width//2+1, height//2-49],intro_text_size_subtitle, hot_pink, intro_font)
        self.draw_text('PRESS SPACEBAR TO START', [width//2, height//2-50],intro_text_size_subtitle, ghost_pink, intro_font)
        self.draw_text('REBECCA BARROW-SCOTT', [width//2, height-40],intro_text_size, ghost_cyan, intro_font)
        self.draw_text('3815 ICT SOFTWARE ENGINEERING', [width//2, height-20],intro_text_size, blue, intro_font)
        pygame.display.update()

    # PLAYING
    def playing_events(self):
        for event in pygame.event.get():
            # quit the game
            if event.type == pygame.QUIT:
                self.running = False

    def playing_update(self):
        pass

    # creates the playing screen
    def playing_draw(self):
        self.screen.fill(black)
        self.screen.blit(self.background, (border_padding//2, border_padding//2))
        self.draw_grid()
        self.draw_text('CURRENT SCORE: 0', [110, 15], intro_text_size_subtitle, white, intro_font)
        self.draw_text('1 2 3', [width-110, 15], intro_text_size_subtitle, white, intro_font)
        self.draw_text('3815 ICT MILESTONE 1: PROTOTYPE', [width//2, height-13], intro_text_size, hot_pink, intro_font)
        self.map.draw()
        self.map.all_sprite_list.draw(self.background)

        pygame.display.update()