from graph import *
import math



def rectangle(width, height, alfa):
    w, h = windowSize()
    focus = (w/2, h/2)
    x = focus[0]
    y = focus[1]
    penColor(0, 0, 0)
    penSize(1)
    x1 = x + round(width * (math.cos(math.radians(alfa))), 2)
    y1 = y + round(width * (math.sin(math.radians(alfa))), 2)
    r = math.hypot(width, height)
    alfa_2 = alfa + math.degrees(math.acos(width/r))
    alfa_3 = 90 + alfa
    x2 = x + round(r * (math.cos(math.radians(alfa_2))), 2)
    y2 = y + round(r * (math.sin(math.radians(alfa_2))), 2)
    x3 = x + round(height * (math.cos(math.radians(alfa_3))), 2)
    y3 = y + round(height * (math.sin(math.radians(alfa_3))), 2)
    brushColor("black")
    polygon([(x, y), (x1, y1), (x2, y2), (x3, y3)])






rectangle(100, 30, 30)

run()