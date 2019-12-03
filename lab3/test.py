from graph import *
import math
width, height = windowSize()
x = width/2
y = height/2


def triangle_hatching(a, x, y, x1, y1, n):
    step = a/n
    for i in range(n + 1):
        moveTo(x, y)
        xi = x1
        yi = y1
        lineTo(xi, yi)
        x1 += step


ab = 60
x1 = x - round(ab * (math.cos(math.radians(30))), 1)
y1 = y + round(ab * (math.sin(math.radians(30))), 1)
bc = 2 * ab * math.sin(math.radians(60))
triangle_hatching(bc, x, y, x1, y1, 10)
run()
