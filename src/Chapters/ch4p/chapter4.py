import graphics
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
