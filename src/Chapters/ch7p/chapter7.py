#1-3,6-8,11,12,16
from graphics import *
import math
def problem1():
    hours = int(input("How many hours did you work this week?"))
    wage = float(input("Enter your hourly wage"))

    if hours <= 40:
        print("You made {0:.2f} this week".format(hours*wage))
    else:
        print("You made {0:.2f} this week".format(40*wage + (1.5*(hours-40))*wage ))
        
def problem2():
    x = float(input("Enter the quiz score"))
    #get the input of the quiz score as a number

    #print it out as the corresponding letter grade
    if x == 5:
        print("A")
    elif x == 4:
        print("B")
    elif x == 3:
        print("C")
    elif x ==2:
        print("D")
    else:
        print("F")
        
def problem3():
    #get the score as a number
    x = float(input("Enter the quiz score"))
    
    #convert the number to a letter grade
    if x >=90:
        print("A")
    elif x>=80:
        print("B")
    elif x>=70:
        print("C")
    elif x >=60:
        print("D")
    else:
        print("F")

def problem6():
    limit = int(input("What is the speed limit?"))
    speed = float(input("What is your speed?"))
    fine = int(50)
    if speed>limit:
        fine = fine + 5*math.floor(speed-limit)
        if speed > 90:
            fine += 200
        print(fine)
    else:
        print("You were under the speed limit.  YAY!!")
    
def problem7():
    firsttime = input("enter the hour, minutes, and AM or PM seperated by commas\nExamples.\n9,22,AM (9:22 AM)\n12,22,AM (12:22 AM)\n").split(",")
    secondtime = input("enter the hour, minutes, and AM or PM seperated by commas").split(",")
    md = float(0);
    #account for PM
    for i in range(1):
        firsttime[i] = int(firsttime[i])
        secondtime[i] = int(secondtime[i])
    
    if firsttime[2][0]=="P":
        firsttime[0] += 12
    #account for PM
    if secondtime[2][0]=="P":
        secondtime[0] += 12
    
    if int(secondtime[0]) >= 21:
        #logic
        before9money =  ((int(21)-int(firsttime[0]))*60 + int(0)-int(firsttime[1]))/60
        after9 = ((int(secondtime[0])-int(21))*60 + int(secondtime[1])-int(0))/60
        print("You made ${0:3f}".format(before9money*2.5 + after9*1.75))
    else:
        #other logic
        md = (int(secondtime[0])-int(firsttime[0]))*60 + int(secondtime[1])-int(firsttime[1])
        print("You made ${0:3f}".format((md/60)*2.5))
    
def problem8():
    age = int(input("Input your age"))
    years = int(input("how many years have you been a US citizen"))
    if age>=30 and years>=9:
        print("you are eligible for the senate")
    if age>=25 and years>=7:
        print("you are eligible for the house")
    
def problem11():
    year = int(input("input the year"))
    if year%4==0 and (year-(year%100))%400==0:
        print("LEAP YEAR")
        return
    print("NOT LEAP YEAR")

def problem12():
    date = input("enter the date")
    date = date.split("/")
    for i in range(len(date)):
        date[i] = int(date[i])
    enddate = [31,28,31,30,31,30,31,31,30,31,30,31]
    if int(date[1]) <= int(enddate[date[0]-1]):
        print("Valid")
        return
    print("Invalid")
def problem16():
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
    totalval = int(0)
    for i in range(5):
        click = win.getMouse()
        howFar = distance(click.getX(),click.getY())
        if howFar < 120:
            totalval+=2
            if howFar < 100:
                totalval +=2
                if howFar <80:
                    totalval +=2
                    if howFar <60:
                        totalval+=2
                        if howFar < 40:
                            totalval+=2
    print(totalval)
#helper function for problem 16
def distance(x1,y1):
    return ((200-x1)**2 + (200-y1)**2)**(1/2)
    

############EXTRA CREDIT PROBLEMSw
def problem4():
    creds = int(input("input the number of credits"))
    if creds<7:
        print("Freshman")
    elif creds < 16:
        print("Sophmore")
    elif creds<26:
        print("Junior")
    else:
        print("senior")
def problem5():
    weight = int(input("Enter your weight"))
    height = int(input("Enter your height"))
    bmi = weight * (720/(height**2))
    if 19 <= bmi and bmi<=25:
        print("healthy")
        return
    print("unhealthy")
    
        
        
    
        
