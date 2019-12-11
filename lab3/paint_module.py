from graph import *
import math


def rectangle_painter(width, height, x, y, color=brushColor(), alfa=0):          # alfa - угол наклона прямоугольника
    x1 = x + round(width * (math.cos(math.radians(alfa))), 2)
    y1 = y + round(width * (math.sin(math.radians(alfa))), 2)
    r = math.hypot(width, height)
    alfa_2 = alfa + math.degrees(math.acos(width/r))
    alfa_3 = 90 + alfa
    x2 = x + round(r * (math.cos(math.radians(alfa_2))), 2)
    y2 = y + round(r * (math.sin(math.radians(alfa_2))), 2)
    x3 = x + round(height * (math.cos(math.radians(alfa_3))), 2)
    y3 = y + round(height * (math.sin(math.radians(alfa_3))), 2)
    if type(color) == tuple or type(color) == list:
        r = color[0]
        g = color[1]
        b = color[2]
        brushColor(r, g, b)
    else:
        brushColor(color)
    polygon([(x, y), (x1, y1), (x2, y2), (x3, y3)])


""" 
ab, ac - стороны треугольника; cab - угол между ними; x, y - координаты нач. точки; 
bax - угол наклона 1-ой стороны(если 0 - параллельно оси x); color - цвет заливки треуг-ника# строкой или rgb кортежем    
"""

def triangle_painter(ab, ac, cab, x, y, color=brushColor(), bax=0):
    if type(color) == tuple or type(color) == list:
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


""" position - отрисовываемый сектор, опред. по сторонам светаили номерам ('NW':1, 'NE':2, 'SW':3, 'SE':4);
    x, y - коорд. центра
"""

def quarter_circle(r, x, y, color=brushColor(), position='NW'):
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


def triangle_hatching(side, x, y, x1, y1, n):      # a - сторона, на кот-ую падают отрезки; x1, y1 - коорд. её начала;
    step = side/n                                  # x, y, - коорд. вершины, из кот-ой идут отрезки; n - кол-во частей,
    for i in range(n):                      # на кот-ое делят сторону "а" подающие отрезки
        moveTo(x, y)
        xi = x1
        yi = y1
        lineTo(xi, yi)
        x1 += step


def ellipse_painter(a, b, x, y):                # a, b = малые оси (1/2 стороны); x, y - коорд. центра эллипса
    points = []
    for i in range(360):
        xi = x + a * math.cos(math.radians(i))
        yi = y - b * math.sin(math.radians(i))
        points.append([xi, yi])

    return polygon(points)


def cloud_painter(r, n, x, y, color='white', form="circle"):
    if type(color) == tuple or type(color) == list:  # строкой или rgb кортежем
        red = color[0]
        green = color[1]
        blue = color[2]
        brushColor(red, green, blue)
    else:
        brushColor(color)
    if form == 'circle':
        for i in range(n):
            if i % 2 == 0:
                circle(x, y, r)
            else:
                circle(x, (y-r), r)
            x += r/1.5
    elif form == 'ellipse':
        a = r[0]
        b = r[1]
        for i in range(n):
            if i % 2 == 0:
                ellipse_painter(a, b, x, y)
            else:
                ellipse_painter(a, b, x, (y-b))
            x += a/1.4


def boat_painter(boatWidth, boatHeight, x, y):
    quarter_circle(boatHeight, x, y, 'brown', 'SW')
    rectangle_painter((boatWidth*0.6), boatHeight, x, y, 'brown')
    triangle_painter(boatWidth*0.3, boatHeight, 90, (x + boatWidth*0.6), y, 'brown')
    rectangle_painter(boatWidth * 0.02, boatHeight * 3, (x + boatWidth * 0.2), (y - boatHeight * 3), 'black')
    sail_ac = math.hypot(boatHeight*1.5, boatHeight*0.375)
    sail_ab = math.hypot(boatHeight*1.5, boatHeight*1.5)
    sail_bax = round(math.degrees(math.acos(boatHeight*1.5 / sail_ab)))
    yac = round(math.degrees(math.acos(boatHeight*1.5 / sail_ac)), 2)
    sail_cab = 90 - (yac + sail_bax)
    triangle_painter(sail_ab, sail_ac, sail_cab, (x + boatWidth * 0.22), (y - boatHeight * 3), [245, 245, 220], sail_bax)
    sail_bax = -sail_bax
    sail_cab = -sail_cab
    triangle_painter(sail_ab, sail_ac, sail_cab, (x + boatWidth * 0.22), y, 'beige', sail_bax)
    brushColor('black')
    p = (boatWidth*0.3 + boatHeight + math.hypot(boatWidth*0.3, boatHeight)) / 2
    boatWindowR = math.sqrt((p - boatWidth*0.3)*(p - boatHeight)*(p - math.hypot(boatWidth*0.3, boatHeight)) / p)
    boatWindowX = (x + boatWidth*0.6 + boatWindowR)
    boatWindowY = y + boatWindowR
    circle(boatWindowX, boatWindowY, boatWindowR*0.8)
    brushColor('white')
    circle(boatWindowX, boatWindowY, boatWindowR*0.6)


def beach_umbrella_painter(umbrella_width, umbrella_height, x, y, color):
    rectangle_painter(umbrella_width*0.05, umbrella_height, (x - umbrella_width*0.025), y, color)
    bottom_side = umbrella_width
    side = bottom_side / (2 * math.sin(math.radians(60)))
    triangle_painter(side, side, 120, x, y, color, 30)
    x1 = x - round(side * (math.cos(math.radians(30))), 1)
    y1 = y + round(side * (math.sin(math.radians(30))), 1)
    triangle_hatching(bottom_side, x, y, x1, y1, 8)


def sun_painter(x, y, r_sun, n, len_ray=None):
    points = []
    brushColor('yellow')
    circle(x, y, r_sun)
    step = 360/n                # шаг между точками, делящими окружность на n частей
    alfa = 360 / (2 * n)        # угол наклона отрезка, соед. центр и вершину луча
    for i in range(n+1):
        xi = x + r_sun * (math.cos(math.radians(step * i)))  # коорд. точек основания луча
        yi = y - r_sun * (math.sin(math.radians(step * i)))
        points.append([round(xi, 2), round(yi, 2)])
        if i == 0:
            continue
        if len_ray is None and i == 1:   # если длина луча не задана, и есть вторая точка: рассчитываем длину основания
            a = math.sqrt(((points[i][0] - points[i - 1][0]) ** 2) + ((points[i][1] - points[i - 1][1]) ** 2)) / 2
            beta = 360 / (2 * n + 1)        # beta - угол вершины луча, (180-beta)/2) - угол при основании
            len_ray = a * math.sin(math.radians((180 - beta) / 2))     # и длину луча по соотношению сторон прям. треуг.
        xk = x + (r_sun + len_ray) * (math.cos(math.radians(alfa)))
        yk = y - (r_sun + len_ray) * (math.sin(math.radians(alfa)))
        alfa += step
        temp_point = points[-1]             # вставляем коорд. вершины луча между коорд. точек
        points[-1] = [round(xk, 2), round(yk, 2)]
        points.append(temp_point)
    return polygon(points)


def wave_painter(start_place, width):
    r = 35
    rb = 35
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