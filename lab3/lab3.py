from graph import *
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


run()