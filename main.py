from display import *
from draw import *

import math
import random

x = 0
y = 0

screen = new_screen()
color = [ 0, 255, 0 ]

color[ BLUE ] = MAX_COLOR
color[ RED ] = 0

degree = math.pi / 180
theta = 0

while ( theta < math.pi/2 ):
  draw_line(screen, 0, int(YRES * math.cos(theta)), int(XRES * math.sin(theta)), 0, color);
  theta += degree

color[ BLUE ] = 0
color[ RED ] = MAX_COLOR

draw_line(screen, XRES - 100, YRES - 100, XRES - 80, YRES - 100, color);
draw_line(screen, XRES - 100, YRES - 80, XRES - 80, YRES - 80, color);
draw_line(screen, XRES - 100, YRES - 100, XRES - 100, YRES - 80, color);
draw_line(screen, XRES - 80, YRES - 100, XRES - 80, YRES - 80, color);

draw_line(screen, XRES - 60, YRES - 100, XRES - 40, YRES - 100, color);
draw_line(screen, XRES - 60, YRES - 80, XRES - 40, YRES - 80, color);
draw_line(screen, XRES - 60, YRES - 100, XRES - 60, YRES - 80, color);
draw_line(screen, XRES - 40, YRES - 100, XRES - 40, YRES - 80, color);

draw_line(screen, XRES - 110, YRES - 50, XRES - 30, YRES - 50, color);
draw_line(screen, XRES - 110, YRES - 30, XRES - 30, YRES - 30, color);
draw_line(screen, XRES - 110, YRES - 50, XRES - 110, YRES - 30, color);
draw_line(screen, XRES - 30, YRES - 50, XRES - 30, YRES - 30, color);

display(screen)
