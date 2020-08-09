from pygame.math import Vector2 as vector
border_padding = 50
width, height = 545, 555
maze_width, maze_height = width-border_padding, height-border_padding
fps = 60


intro_text_size_title = 40
intro_text_size_subtitle = 30
intro_text_size = 20
intro_font = 'Bahnschrift Light'

#-#---COLORS---#-#
pacman_yellow = (248, 211, 10)
ghost_pink = (253, 173, 167)
ghost_cyan = (73, 223, 202)
ghost_red = (199, 59, 17)
ghost_orange = (255, 152, 48)
black = (0, 0, 0)
white = (255, 255, 255)
purple = (113, 63, 159)
hot_pink = (200, 67, 82)
green = (73, 174, 138)
blue = (73, 108, 174)
#-#---PLAYER__#-#
starting_pos = vector(9, 11)