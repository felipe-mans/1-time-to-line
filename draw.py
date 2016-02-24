from display import *

def draw_line( screen, x0, y0, x1, y1, color ):

  if x1 < x0:
    holder = x1
    hold = x0
    x0 = holder
    x1 = hold

  A = y1 - y0
  B = -1 * (x1 - x0)

  if (y1 > y0):
    x = x0
    y = y0
    d = (2*A) + B
    if (A < B):
      while ( x < x1):
        plot(screen,color,x,y)
        if (d > 0):
          y = y + 1
          d = d + (2*B)
        x = x + 1
        d = d + (2*A)
    else:
      while ( y < y1 ):
        plot(screen,color,x,y)
        if (d < 0):
          x = x + 1
          d = d + (2*A)
        y = y + 1
        d = d + (2*B)

  else:
    x = x0
    y = y0
    d = (2*A) - B
    if (A > B):
      while ( x < x1 ):
        plot(screen,color,x,y)
        if (d < 0):
          y = y - 1
          d = d - (2*B)
        x = x + 1
        d = d + (2 * A)
    else:
      while ( y > y1 ):
        plot(screen,color,x,y)
        if (d > 0):
          x = x + 1
          d = d + (2*A)
        y = y - 1
        d = d - (2*B)
