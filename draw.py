from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
  x = x0
  y = y0
  A = y1 - y0
  B = (x1 - x0) * -1

  if(octant = 1):
    d = (2*A) + B
    while ( x <= x1 ):
        plot(x,y)
        if ( d > 0 ):
          y += 1
          d += (2*B)
        x += 1
        d += (2*A)

  if(octant = 2):
    x = x0
    y = y0
    d = A + (2*B)
    while ( x <= y1 ):
      plot(x,y)
      if ( d < ):
        x += 1
        d += 2A
      y += 1
      d += (2*b)

    pass
