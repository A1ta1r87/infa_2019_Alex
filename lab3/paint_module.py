from graph import *
import math

def inclined_rectangle(width, height, alfa, x, y, color):
    import math
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
    if type(color) == tuple or type(color) == list:  # строкой или rgb кортежем
        r = color[0]
        g = color[1]
        b = color[2]
        brushColor(r, g, b)
    else:
        brushColor(color)
    polygon([(x, y), (x1, y1), (x2, y2), (x3, y3)])


def triangle_painter(ab, ac, cab, x, y, bax, color):  # ab, ac - стороны треугольника; cab - угол между ними;
    penColor(0, 0, 0)                                 # x, y - координаты нач. точки; bax - угол наклона 1-ой стороны
    penSize(1)                                        # (если 0 - параллельно оси x); color - цвет заливки треугольника
    if type(color) == tuple or type(color) == list:   # строкой или rgb кортежем
        r = color[0]
        g = color[1]
        b = color[2]
        brushColor(r, g, b)
    else:
        brushColor(color)
    if bax == 0:
        x1 = x + ab
        y1 = y + 0
        x2 = x + round(ac * (math.cos(math.radians(cab))), 2)
        y2 = y + round(ac * (math.sin(math.radians(cab))), 2)
    else:
        x1 = x + round(ab * (math.cos(math.radians(bax))), 2)
        y1 = y + round(ab * (math.sin(math.radians(bax))), 2)
        x2 = x + round(ac * (math.cos(math.radians(cab + bax))), 2)
        y2 = y + round(ac * (math.sin(math.radians(cab + bax))), 2)

    return polygon([(x, y), (x1, y1), (x2, y2)])


def quarter_circle(r, position, x, y, color):
    points = [(x, y)]
    moveTo(x, y)
    if position == 'SE' or position == 4:
        x1 = x + r
        y1 = y
        x2 = x
        y2 = y + r
        points.append([x1, y1])
        alfa = 1
        for i in range(90):
            xi = x + round(r * (math.cos(math.radians(alfa))), 2)
            yi = y + round(r * (math.sin(math.radians(alfa))), 2)
            points.append([xi, yi])
            alfa += 1
    elif position == 'SW' or position == 3:
        x1 = x - r
        y1 = y
        x2 = x
        y2 = y + r
        points.append([x1, y1])
        alfa = 1
        for i in range(90):
            xi = x - round(r * (math.cos(math.radians(alfa))), 2)
            yi = y + round(r * (math.sin(math.radians(alfa))), 2)
            points.append([xi, yi])
            alfa += 1
    elif position == 'NE' or position == 2:
        x1 = x + r
        y1 = y
        x2 = x
        y2 = y - r
        points.append([x1, y1])
        alfa = 1
        for i in range(90):
            xi = x + round(r * (math.cos(math.radians(alfa))), 2)
            yi = y - round(r * (math.sin(math.radians(alfa))), 2)
            points.append([xi, yi])
            alfa += 1
    elif position == 'NW' or position == 1:
        x1 = x - r
        y1 = y
        x2 = x
        y2 = y - r
        points.append([x1, y1])
        alfa = 179
        for i in range(90):
            xi = x + round(r * (math.cos(math.radians(alfa))), 2)
            yi = y - round(r * (math.sin(math.radians(alfa))), 2)
            points.append([xi, yi])
            alfa -= 1
    else:
        return print('Enter correct parameters')
    points.append([x2, y2])
    if type(color) == tuple or type(color) == list:  # строкой или rgb кортежем
        r = color[0]
        g = color[1]
        b = color[2]
        brushColor(r, g, b)
    else:
        brushColor(color)
    return polygon(points)

def triangle_hatching(a, x, y, x1, y1, n):
    step = a/n
    for i in range(n + 1):
        moveTo(x, y)
        xi = x1
        yi = y1
        lineTo(xi, yi)
        x1 += step



