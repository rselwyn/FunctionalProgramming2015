#1-3,6-8,11,12,16
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
    

