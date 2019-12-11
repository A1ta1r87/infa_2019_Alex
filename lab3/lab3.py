from paint_module import *

windowSize(600, 600)
width, height = windowSize()
canvasSize(width, height)

brushColor(0, 255, 255)
penColor(0, 255, 255)
rectangle(0, 0, width, height*0.5)
brushColor(0, 0, 255)
penColor(0, 0, 255)
rectangle(0, height*0.5, width, height*0.75)
points = wave_painter(height*0.7, width)
brushColor(255, 255, 0)
penColor(255, 255, 0)
p = ([width, height], [0, height], [0, height*0.7])
points.append(p)
polygon(points)


sun_painter(width*0.8, height*0.2, 50, 50, 10)

penColor(192, 192, 192)
cloud_painter(15, 7, width/5, height/7)
cloud_painter([17, 20], 7, 2*width/5, height/7, form='ellipse')
cloud_painter([20, 17], 7, width/9, height/3, form='ellipse')

penColor('black')
boat_painter(width*0.4, height*0.05, width*0.6, height*0.57)
boat_painter(width*0.2, height*0.025, width*0.25, height*0.52)

beach_umbrella_painter(150, 200, width*0.2, height*0.55, [255, 69, 0])
beach_umbrella_painter(70, 105, width*0.4, height*0.65, [255, 69, 0])






run()