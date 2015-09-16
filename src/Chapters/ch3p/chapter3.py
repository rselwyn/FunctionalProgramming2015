#do 1,4 6-11, ec(12-17)
import math
import os
def problem1():
    #define pi
    pi = math.pi
    print("This program calculates the volume and surface area of a sphere")
    # get input, float input so no error
    rad = float(input("what is the radius"))
    #surface area
    sa = 4 * pi * rad**2
    #volume
    vol = (4/3)*pi*rad**3
    print("The volume is", vol, "and the surface area is", sa)
def problem4():
    #this program prints distance to a lightning strike based on time elapsed
    li = input("Time elapsed between lightening flash and thunder")
    print("You are", 1100*li, "ft")
def problem6():
    #prints the slope of the line containing both points
    
    x1,y1 = input("Enter coordinate 1 sperated by commas")
    #get points 1 and 2
    x2,y2 = input("enter coordinate 2 seperated by commas")

    #print using slope formula (Change in y over change in x)
    print("the slope is", (y2-y1)/(x2-x1))
def problem7():
    #get the two coordinates 
    x1,y1 = input("Enter coordinate 1 sperated by commas")
    x2,y2 = input("enter coordinate 2 seperated by commas")
    #plug into the distance formula
    d = ((y2-y1)**2 + (x2-x1)**2)**(1/2)

    #print
    print("The distance between the coordinates is",d)
def problem8():
    #this program has me plug values into the formula in the book
    C = int(input("year"))//100
    #get the year and int divide it by 100
    year = C*100
    #create other value
    epact = (8 +(C//4) - C + ((8*C+13)//25) + 11* (year%19))%30
    #plug in into formula
    print(epact)

#WRITE PROBLEM 9
def problem9():
    #get side lengths value
    a = float(input("enter the value of side 1"))
    b = float(input("enter the value of side 2"))
    c = float(input("enter the value of side 3"))
    #calculate the value of (a+b+c)/2
    s = (a+b+c)/2
    #use the formula provided in the book to find the area
    area = (s*(s-a)*(s-b)*(s-c))**(1/2)
    print("the area is", area)
    
def problem10():
    x = float(input("angle measure"))
    #get the angle measure formed by the fround and ladder
    h = float(input("enter the height of the house"))
    radians = math.pi/180 * x
    #convert to radians so we can use math.sin
    length = h/(math.sin(radians))
    #calculate the length of the ladder using a formula from book
    print(length)
    #print the length of the ladder
def problem11():
    #prints natural numbers
    x = int(input("how many natural numbers should be summed?"))
    #x is the number of number to be summed
    y = 0
    #y is the value where the numbers get accumulated
    for i in range(x+1):
        #assuming that the set of natural numbers is (0, infinity) in set notation
        #add one to nuber of iterations because natural numbers don't include zero
        #add the current number the loop is on to the total
        y = y+ i
    #print the total    
    print(y)
    
def problem12():
    x = int(input("how many cubes of natural numbers do you want to sum"))
    y = 0
    #y is the accumulator
    for i in range(x+1):
        #assuming that the set of natural numbers is (0, infinity) in set notation
        #add one because natural numbers dont include zero

        #add the cube of the current number to the total
        y = y+ i**3
    #print the accumulated value    
    print(y)
def problem13():
    #this program sums numbers given by a user
    nums = int(input("how many numbers is your series?"))
    x = 0
    #x is the accumulated value of the sums
    print("please enter each number in your series and press enter")
    for i in range(nums):
        # get input (nums) times

        #add the input to the accumulator
        x = x + float(input())
    print("the total value of your series of numbers is",x)
    #print the value of the set
def problem14():
    nums = int(input("how many numbers are in your series"))
    #ge the number of numbers in the series
    x = 0
    #z is accumulator variable
    print("please enter each number in your series and press enter")
    for i in range(nums):
        #loop iterates (nums) times
        
        #add the input to the accumulator
        x = x + float(input())
        #print the average
    print("The average of the numbers in your series is", x/nums)
def problem15():
    x = int(input("to what precision do you want pi to be calculated to"))
    #get the iterations of the pi calculator
    mu = 1
    #mu gets set to 1 or -1 that gets multiplied by 4/(a value) because the
    #formula switches between adding and subtracting
    
    adder = 1
    #this increases by 2 each time for the formula
    
    totalp = 0
    #totalp is accumulator
    for i in range(x):
        totalp += mu * (4/adder)
        #add the value to the accumulator
        
        mu = mu * (-1)
        #flips mu for the formula
        
        adder+=2
        #add 2 to the adder for the formula
    print(totalp)                 
def problem16():
    hm = int(input("how many fibonnaci numbers?"))
    num1 = 0
    num2 = 1
    store = 0
    
    for i in range(hm):
        store = num2
        num2 += num1
        num1 = store
        
    print(num1)
