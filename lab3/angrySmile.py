from graph import *
width, height = windowSize()
focus = (width/2, height/2)
x = focus[0]
y = focus[1]
def inclined_rectangle(width, height, alfa, x, y):
    import math
    w, h = windowSize()
    focus = (w/2, h/2)
    x0 = x + focus[0]
    y0 = y + focus[1]
    penColor(0, 0, 0)
    penSize(1)
    x1 = x0 + round(width * (math.cos(math.radians(alfa))), 2)
    y1 = y0 + round(width * (math.sin(math.radians(alfa))), 2)
    r = math.hypot(width, height)
    alfa_2 = alfa + math.degrees(math.acos(width/r))
    alfa_3 = 90 + alfa
    x2 = x0 + round(r * (math.cos(math.radians(alfa_2))), 2)
    y2 = y0 + round(r * (math.sin(math.radians(alfa_2))), 2)
    x3 = x0 + round(height * (math.cos(math.radians(alfa_3))), 2)
    y3 = y0 + round(height * (math.sin(math.radians(alfa_3))), 2)
    brushColor("black")
    polygon([(x0, y0), (x1, y1), (x2, y2), (x3, y3)])
penColor(0, 0, 0)
penSize(1)
brushColor("yellow")
circle(x, y, 100)
brushColor("red")
circle((x - 50), (y - 30), 20)
circle((x + 50), (y - 30), 15)
brushColor("black")
circle((x - 50), (y - 30), 8)
circle((x + 50), (y - 30), 8)
# polygon([((x-100), (y-92)), ((x-95), (y-97)), ((x-20), (y-38)), ((x-25), (y-33))])
# polygon([((x+100), (y-70)), ((x+95), (y-75)), ((x+20), (y-38)), ((x+25), (y-33))])
rectangle((x - 50), (y + 50), (x + 50), (y + 70))
inclined_rectangle(80, 10, 30, -80, -80)
inclined_rectangle(80, 10, -30, 20, -40)

run()