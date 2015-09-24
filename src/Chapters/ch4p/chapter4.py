import graphics
#2,3,5,6,9
#ec 7, 8, 10, 11
def test():
    #this isnt a problem
    win = graphics.GraphWin()
    shape = graphics.Circle(graphics.Point(50,50),20)
    shape.setOutline("Red")
    shape.setFill("Black")
    shape.draw(win)

def problem2():
    win = graphics.GraphWin("Archery", 400,400)

    
    white = graphics.Circle(graphics.Point(200,200),120)
    white.setOutline("Black")
    white.setFill("White")
    white.draw(win)
    
    black = graphics.Circle(graphics.Point(200,200),100)
    black.setOutline("White")
    black.setFill("Black")
    black.draw(win)
    
    blue = graphics.Circle(graphics.Point(200,200),80)
    blue.setOutline("Black")
    blue.setFill("Blue")
    blue.draw(win)

    red = graphics.Circle(graphics.Point(200,200),60)
    red.setOutline("Black")
    red.setFill("red")
    red.draw(win)
    
    yellow = graphics.Circle(graphics.Point(200,200),40)
    yellow.setOutline("Black")
    yellow.setFill("yellow")
    yellow.draw(win)
def problem3():
    #draw a face
    win = graphics.GraphWin("Archery", 400,400)

    yellow = graphics.Circle(graphics.Point(200,200),80)
    yellow.setOutline("Black")
    yellow.setFill("yellow")
    yellow.draw(win)

    
    blue = graphics.Circle(graphics.Point(175, 175),20)
    blue.setOutline("Black")
    blue.setFill("Blue")
    blue.draw(win)

    blue2 = graphics.Circle(graphics.Point(225, 175),20)
    blue2.setOutline("Black")
    blue2.setFill("Blue")
    blue2.draw(win)

#    line = graphics.Line(graphics.Point(100,2), graphics.Point(3,2))
#    line.draw(win)
