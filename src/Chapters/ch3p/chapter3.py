#do 1,4 6-11, ec(12-17)
import math
import os
def problem1():
    #define pi
    pi = 3.14159265358979323846264338279502
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
    x1,y1 = input("Enter coordinate 1 sperated by commas")
    x2,y2 = input("enter coordinate 2 seperated by commas")
    print("the slope is", (y2-y1)/(x2-x1))
def problem7():
    x1,y1 = input("Enter coordinate 1 sperated by commas")
    x2,y2 = input("enter coordinate 2 seperated by commas")
    d = ((y2-y1)**2 + (x2-x1)**2)**(1/2)
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
                 
                  
