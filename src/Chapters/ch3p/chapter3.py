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
    C = int(input("year"))//100
    year = C*100
    epact = (8 +(C//4) - C + ((8*C+13)//25) + 11* (year%19))%30
    print(epact)
#WRITE PROBLEM 10
def problem10():
    x = float(input("angle measure"))
    h = float(input("enter the height of the house"))
    radians = math.pi/180 * x
    length = h/(math.sin(radians))
    print(length)
def problem11():
    x = int(input("how many natural numbers should printed"))
    y = 0
    for i in range(x):
        
        y = y+ i
    print(y)
    
def problem12():
    x = int(input("how many natural numbers should printed"))
    y = 0
    for i in range(x):
        
        y = y+ i**3
    print(y)
def problem13():
    #this program sums numbers given by a user
    nums = int(input("how many numbers is your series"))
    x = 0
    print("please enter each number in your series and press enter")
    for i in range(nums):
        x = x + float(input())
    print("the total value of your series of numbers is",x)    
def problem14():
    nums = int(input("how many numbers is your series"))
    x = 0
    print("please enter each number in your series and press enter")
    for i in range(nums):
        x = x + float(input())
    print("The average of the numbers in your series is", x/nums)
def problem15():
    x = int(input("to what precision do you want pi to be calculated to"))
    mu = 1
    adder = 1
    totalp = 0
    for i in range(x):
        totalp += mu * (4/adder)
        mu = mu * (-1)
        adder+=2
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
