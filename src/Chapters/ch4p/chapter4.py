from graphics import *
import math
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
    #create window
    
    white = Circle(Point(200,200),120)
    white.setOutline("Black")
    white.setFill("White")
    white.draw(win)
    #create and draw the white circle
    
    black = Circle(Point(200,200),100)
    black.setOutline("White")
    black.setFill("Black")
    black.draw(win)
    #create and draw the black circle
    
    blue = Circle(Point(200,200),80)
    blue.setOutline("Black")
    blue.setFill("Blue")
    blue.draw(win)
        #create and draw the blue circle
    

    red = Circle(Point(200,200),60)
    red.setOutline("Black")
    red.setFill("red")
    red.draw(win)
    #create and draw the red circle
    
    yellow = Circle(Point(200,200),40)
    yellow.setOutline("Black")
    yellow.setFill("yellow")
    yellow.draw(win)
    #create and draw the yellow circle
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

    nose = Line(Point(200,195),Point(200,230))
    nose.draw(win)
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
    
    #THE REST OF THE CODE FOR THIS PROBLEM DRAWS THE DOTS ON THE DICE
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
    #end dot drawing

def problem6():
 #   principal = 1000
 #   apr = .05
    correct =1
    win = GraphWin("Chart", 420,240)
    #create window
    win.setBackground("white")

    #add entry boxes
    pin = Entry(Point(300,50),20)
    aprin = Entry(Point(300,75),20)
    pin.draw(win)
    aprin.draw(win)
    #draw them
    
    Text(Point(310,10), "Top box is principal - Bottom is apr").draw(win)
    submit = Rectangle(Point(300,100),Point(350,135))
    submit.setFill("red")
    submit.draw(win)
    Text(Point(325,110), "Submit").draw(win)
    win.getMouse()

    #use try catch to block any errors
    try:
        
        principal = float(eval(pin.getText()))
        apr = float(eval(aprin.getText()))
        correct = 1
    except:
        win.close()
        correct = 0
        print("Error: Please type in a valid value --\n You may reinvoke this function with the command problem6()")
    #if input is succesful, run the rest of the code from the book
    if correct == 1:
        Text(Point(20,230), '0.0K').draw(win)
        Text(Point(20,180), '2.5K').draw(win)
        Text(Point(20,130), '5.0K').draw(win)
        Text(Point(20,80), '7.5K').draw(win)
        Text(Point(20,30), '10.0K').draw(win)
        height = principal*.02
        bar = Rectangle(Point(40,230), Point(65,230-height))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)
        for year in range(1,11):
            principal = principal *(1+apr)
            x11 = year * 25 +40
            height = principal *.02
            bar = Rectangle(Point(x11,230), Point(x11+25, 230-height))
            bar.setFill("green")
            bar.setWidth(2)
            bar.draw(win)
                
    input("Please press enter to close")
    win.close()        

def problem8():
    #this is ec
    win = GraphWin("Click two points to create a line", 400, 400);
    p = win.getMouse()
    x1,y1 = p.getX(), p.getY()
    #get the mouse and assign it to variables
    p2 = win.getMouse()
    x2,y2 = p2.getX(), p2.getY()
    #get the mouse and assign to variables
    point1 = Point(x1,y1)
    point2 = Point(x2,y2)
    #create point objects out of the variables
    line = Line(point1,point2).draw(win)
    #draw the line with the points
    midpoint = Point(((x1+x2)/2),((y2+y1)/2))
    #calculate the midpoint of the line
    midp = Circle(midpoint ,3)
    #create midpoint object
    midp.setFill("cyan")
    midp.draw(win)
    #set fill and draw midpoint
    length = ((x2 - x1)**2 + (y2-y1)**2)**(1/2)
    #calc distance with distance formula
    val = "The slope " + str(round((x2-x1)/(y2-y1),3)) +" and the distance is " + str(round(length,3))
    Text(Point(170,30), val).draw(win)
    #output distance and slope
def problem9():
    win = GraphWin("Click to create a rectangle", 300, 300)
    #create the window
    
    p = win.getMouse()
    #get the mouse click

    
    x1,y1 = p.getX(), p.getY()
    #assign mouse click values to variables

    #get another mouse click and assign it to variables
    p2 = win.getMouse()
    x2,y2 = p2.getX(), p2.getY()

    #create points that can be displayed
    point1 = Point(x1,y1)
    point2 = Point(x2,y2)
    #create and display a rectangle from the points
    rect = Rectangle(point1,point2)
    rect.setFill("red")
    rect.draw(win)
    #calculate width and height
    height = abs(x1-x2)
    width = abs(y1-y2)
    #create the string to be displayed
    val = "The perimeter is " + str(2*(height + width)) +" and the area is " + str(height*width)
    #display it
    Text(Point(150,30), val).draw(win)
    
