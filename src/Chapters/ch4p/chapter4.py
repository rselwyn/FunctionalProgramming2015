from graphics import *
#2,3,5,6,9
#ec 7, 8, 10, 11
def test():
    #this isnt a problem
    win = GraphWin()
    shape = Circle(Point(50,50),20)
    shape.setOutline("Red")
    shape.setFill("Black")
    shape.draw(win)

def problem2():
    win = GraphWin("Archery", 400,400)

    
    white = Circle(Point(200,200),120)
    white.setOutline("Black")
    white.setFill("White")
    white.draw(win)
    
    black = Circle(Point(200,200),100)
    black.setOutline("White")
    black.setFill("Black")
    black.draw(win)
    
    blue = Circle(Point(200,200),80)
    blue.setOutline("Black")
    blue.setFill("Blue")
    blue.draw(win)

    red = Circle(Point(200,200),60)
    red.setOutline("Black")
    red.setFill("red")
    red.draw(win)
    
    yellow = Circle(Point(200,200),40)
    yellow.setOutline("Black")
    yellow.setFill("yellow")
    yellow.draw(win)
def problem3():
    #draw a face
    win = GraphWin("A Face", 400,400)
    #create window

    #create Face Background
    yellow = Circle(Point(200,200),80)
    yellow.setOutline("Black")
    yellow.setFill("yellow")
    yellow.draw(win)
    #add it

    #create the eyes
    blue = Circle(Point(175, 175),20)
    blue.setOutline("Black")
    blue.setFill("Blue")
    blue.draw(win)
    #add eye #1

    blue2 = Circle(Point(225, 175),20)
    blue2.setOutline("Black")
    blue2.setFill("Blue")
    blue2.draw(win)
    #add eye #2
    #finished the eyes

    #create the mouth
    mouth = Rectangle(Point(150,240),Point(250,245))
    mouth.setFill("Black")
    mouth.draw(win)
    #add it to the window
def problem5():
    
    win = GraphWin("Straight Dice", 400,400)
    for i in range(5):
        mouth = Rectangle(Point(30 + i*75,50),Point(80 +i*75,100))
        mouth.setFill("White")
        mouth.setOutline("Black")
        mouth.draw(win)
    #create all 5 dice
    
    bdot = Circle(Point(55,75),6)
    bdot.setFill("Black")
    bdot.draw(win)
    #add the dot to the dice

    

    
