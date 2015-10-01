from graphics import *

win = GraphWin("Here lies a house.", 500,500)
backing = Rectangle(Point(0,0), Point(500,500))
backing.setFill("blue")
backing.draw(win)
grass = Rectangle(Point(0,500),Point(500,250))
grass.setFill("green")
grass.draw(win)

housem = Rectangle(Point(100,400),Point(400,200))
housem.setFill("yellow")
housem.draw(win)

roof = Polygon(Point(170,75),Point(100,300), Point(400,300),Point(300,75))
roof.setFill("red")
roof.draw(win)
mainWin = Circle(Point(250,200),60)
mainWin.setFill("white")
mainWin.draw(win)


treeL = Rectangle(Point(30,200),Point(250,0))
treeL.setFill("green")
treeL.draw(win)

door = Rectangle(Point(120,400),Point(200,300))
door.setFill("white")
door.draw(win)

window = Rectangle(Point(300,300),Point(350,350))
window.setFill("white")
window.draw(win)

line = Line(Point(325,300), Point(325,350))
line.draw(win)

