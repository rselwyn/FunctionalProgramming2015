#1-3,6-8,11,12,16
from graphics import *
import math
def problem1():
    hours = int(input("How many hours did you work this week?"))
    wage = float(input("Enter your hourly wage"))

    if hours <= 40:
        #in the case that they work less than 40 hours (or equal)
        print("You made {0:.2f} this week".format(hours*wage))
    else:
        #Overtime
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
    ##Get the speed limit
    speed = float(input("What is your speed?"))
    ####Get the speed
    fine = int(50)
    if speed>limit:
        #In the case you are speeding
        fine = fine + 5*math.floor(speed-limit)
        ###add $5 to the fine for every mph
        if speed > 90:
            #add the additional fine for being over 90 mph
            fine += 200
        print(fine)
    else:
        #If you aren't speeding
        print("You were under the speed limit.  YAY!!")
    
def problem7():
    firsttime = input("enter the hour, minutes, and AM or PM seperated by commas\nExamples.\n9,22,AM (9:22 AM)\n12,22,AM (12:22 AM)\n").split(",")
#get the first and second time and split them using commas as delimeter
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
        #If the second time isn't after 9
        md = (int(secondtime[0])-int(firsttime[0]))*60 + int(secondtime[1])-int(firsttime[1])
        print("You made ${0:3f}".format((md/60)*2.5))
    
def problem8():
    age = int(input("Input your age"))
    years = int(input("how many years have you been a US citizen"))
    ##Get the inputs
    if age>=30 and years>=9:
        print("you are eligible for the senate")
    ##IF meets the conditions in the book, print stuff out
    if age>=25 and years>=7:
        print("you are eligible for the house")
    
def problem11():
    year = int(input("input the year"))
    ####if the year is divisible by zero and the year is divisible by zero
    if year%4==0 and (year-(year%100))%400==0:
        
        print("LEAP YEAR")
        return
    print("NOT LEAP YEAR")

def problem12():
    date = input("enter the date")

    #Split the date
    date = date.split("/")
    for i in range(len(date)):
        ###Convert the entire date to ints
        date[i] = int(date[i])

    #Array with lengths of the months
    enddate = [31,28,31,30,31,30,31,31,30,31,30,31]
    if int(date[1]) <= int(enddate[date[0]-1]):
        ###If the date is withing range of the days of that month, continue and print valid
        print("Valid")
        return
        ##Break out of the function if we are done
    #IF the input is out of range, print invalid
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
        #Run this 5 times
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
    

############EXTRA CREDIT PROBLEMS
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
    
def problem9():
    year = int(input("Enter the year"))
    #get the year
    #validate the year
    if year <= 1982 or year>=2048:
        print("invaid year")
        return
    #######THIS IS THE FORMULA FROM THE BOOK
    a = year%19
    b = year%4
    c = year%7
    d = (19 * a +24)%30
    e = (2*b + 4*c + 6*d +5)%7
    if 22 + d + e <= 31:
        print("Easter is on March "+str(22+d+e))
        return
    print("Easter is on April "+str(-9+d+e))
def problem10():
    year = int(input("Enter the year"))
    #get the year
    #validate the year
    if year <= 1900 or year>=2099:
        print("invaid year")
        return
    #######THIS IS THE FORMULA FROM THE BOOK
    a = year%19
    b = year%4
    c = year%7
    d = (19 * a +24)%30
    e = (2*b + 4*c + 6*d +5)%7

    exceptionYears = [1954,1981,2049,2076]
    
    if year in exceptionYears:
        if 22 + d + e -7 <= 31:
            print("Easter is on March "+str(22+d+e-7))
            return
        print("Easter is on April "+str(-9+d+e-7))
        return
    
    if 22 + d + e <= 31:
        print("Easter is on March "+str(22+d+e))
        return
    print("Easter is on April "+str(-9+d+e))
    
