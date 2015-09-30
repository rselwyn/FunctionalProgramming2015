from graphics import *
win = GraphWin('Animate')
center = Point(100,100)
for i in range(91):
    circle = Circle(center,i)
    circle.draw(win)
    circle.undraw()
for i in range(90,-1,-1):
	circle = Circle(center,i)
	circle.setFill('blue')
	circle.draw(win)
	circle.undraw()
