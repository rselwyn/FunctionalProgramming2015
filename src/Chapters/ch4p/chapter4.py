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
    
    win = GraphWin("Straight Dice", 400,200)
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

    #add dots to dice 2
    bdot2 = Circle(Point(119.33,75),6)
    bdot2.setFill("Black")
    bdot2.draw(win)
    bdot3 = Circle(Point(141.66,75),6)
    bdot3.setFill("Black")
    bdot3.draw(win)
    
    
    bdot4 = Circle(Point(119.33+75,85),6)
    bdot4.setFill("Black")
    bdot4.draw(win)
    bdot5 = Circle(Point(141.66+75,85),6)
    bdot5.setFill("Black")
    bdot5.draw(win)
    bdot6 = Circle(Point(205.4,65),6)
    bdot6.setFill("Black")
    bdot6.draw(win)
    
    bdot4 = Circle(Point(119.33+75*2,65),6)
    bdot4.setFill("Black")
    bdot4.draw(win)
    bdot5 = Circle(Point(141.66+75*2,65),6)
    bdot5.setFill("Black")
    bdot5.draw(win)
    bdot4 = Circle(Point(119.33+75*2,85),6)
    bdot4.setFill("Black")
    bdot4.draw(win)
    bdot5 = Circle(Point(141.66+75*2,85),6)
    bdot5.setFill("Black")
    bdot5.draw(win)



    bdot4 = Circle(Point(119.33+75*3 -3,65-3),6)
    bdot4.setFill("Black")
    bdot4.draw(win)
    bdot5 = Circle(Point(141.66+75*3 +3,65-3),6)
    bdot5.setFill("Black")
    bdot5.draw(win)
    bdot4 = Circle(Point(119.33+75*3 -3 ,85+3),6)
    bdot4.setFill("Black")
    bdot4.draw(win)
    bdot5 = Circle(Point(141.66+75*3 +3,85+3),6)
    bdot5.setFill("Black")
    bdot5.draw(win)
    bFINAL =  Circle(Point((119.33+75*3 + 141.66+75*3 )/2 ,85-8),6)
    bFINAL.setFill("Black")
    bFINAL.draw(win)

def problem6():
    win = GraphWin("",320,240)
    principal =100;
    apr = .01;
    win.setBackground("white")
    Text(Point(20,230), '0.0K').draw(win)
    Text(Point(20,180), '2.5K').draw(win)
    Text(Point(20,130), '5K').draw(win)
    Text(Point(20,80), '7.5K').draw(win)
    Text(Point(20,30), '10K').draw(win)
    
    height = principal * .02

    bar = Rectangle(Point(40,230), Point(65, 230-height))
    bar.setFill("Green")
    bar.setWidth(2)
    bar.draw(win)

    for year in range(1,11):
        principal = principal*(1+apr)
        x11 = year *25 +40
        height = principal * .02
        bar = Rectangle(Point(x11,230), Point(x11 +25,230-height))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)
    input("press enter to quit")
    win.close()
