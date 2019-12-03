from graph import *
from paint_module import *

width, height = windowSize()

brushColor(0, 255, 255)
penColor(0, 255, 255)
rectangle(0, -height, width, height/2)
brushColor(0, 0, 255)
penColor(0, 0, 255)
rectangle(0, height/2, width, (2 * height / 3))
brushColor(255, 255, 0)
penColor(255, 255, 0)
rectangle(0, (2 * height / 3), width, height)
circle((width - 100), height/5, 50)
penColor(192, 192, 192)
brushColor(255, 255, 255)
r = 10
for i in range(7):
    if i % 2 == 0:
        circle((i+10)*8, height/5, r)
    else:
        circle((i+10)*8, height/5.5, r)

inclined_rectangle(5, 100, 0, (width/2 + 20), (height/2 - 70), 'black')
inclined_rectangle(150, 30, 0, (width/2 - 30), (height/2 + 30), 'brown')
triangle_painter(70, 30, 90, (width/2 + 120), (height/2 + 30), 0, 'brown')
quarter_circle(30, 'SW', (width/2 - 30), (height/2 + 30), 'brown')
sail_ac = math.hypot(50, 15)
sail_ab = math.hypot(50, 50)
sail_bax = round(math.degrees(math.acos(50/sail_ab)))
yac = round(math.degrees(math.acos(50/sail_ac)), 2)
sail_cab = 90 - (yac + sail_bax)
triangle_painter(sail_ab, sail_ac, sail_cab, (width/2 + 25), (height/2 - 70), sail_bax, [245, 245, 220])
sail_bax = -sail_bax
sail_cab = -sail_cab
triangle_painter(sail_ab, sail_ac, sail_cab, (width/2 + 25), (height/2 + 30), sail_bax, 'beige')
brushColor('black')
circle((width/2 + 135), (height/2 + 42), 9)
brushColor('white')
circle((width/2 + 135), (height/2 + 42), 7)
ab = 60
x = width/5
y = height/2 + 50
triangle_painter(ab, ab, 120, x, y, 30, [255, 69, 0])
x1 = x - round(ab * (math.cos(math.radians(30))), 1)
y1 = y + round(ab * (math.sin(math.radians(30))), 1)
bc = 2 * ab * math.sin(math.radians(60))
triangle_hatching(bc, x, y, x1, y1, 8)
inclined_rectangle(5, 150, 0, x-2, y, [255, 69, 0])






run()