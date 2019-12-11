from paint_module import *

width, height = windowSize()
x = width/2
y = height/2

# def ellipse_painter(a, b, x, y):                # a, b = малые оси (1/2 стороны); x, y - коорд. центра эллипса
#     points = []
#     for i in range(360):
#         xi = x + a * math.cos(math.radians(i))
#         yi = y - b * math.sin(math.radians(i))
#         points.append([xi, yi])
#
#     return polygon(points)
def wave_painter(start_place):
    r = 35
    rb = 45
    b = round(math.cos(math.radians(rb)) * r, 2)
    a = round(math.sin(math.radians(rb)) * r, 2)
    x = a
    y = start_place + b
    points = []
    n = 1
    moveTo(x, y)
    for i in range(width):
        for k in range(rb*2):

            xi = round(x + r * math.cos(math.radians((90+rb)-k)), 2)
            if n % 2 == 0:
                yi = round(y + r * math.sin(math.radians((90+rb)-k)), 2)
            else:
                yi = round(y - r * math.sin(math.radians((90+rb)-k)), 2)
            i += 1
            points.append([xi, yi])
        x += 2*a
        if n % 2 != 0:
            y -= 2*b
        else:
            y += 2*b
        n += 1
        moveTo(x, y)
    return points

wave_painter(height*0.8)
run()
