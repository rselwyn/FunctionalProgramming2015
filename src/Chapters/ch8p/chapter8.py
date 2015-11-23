#pe ch8 1,2,5,6,9,11

def problem1():
    hm = int(input("Enter the fibonnaci number you want"))
    #Get the input
    tnum1 = 0
    #first number is zero
    tnum2 = 1
    #second is 1
    store = 0
    #storage variable to store values   
    for i in range(hm):
        store = tnum2
        #set another value equal to the second number
        tnum2 += tnum1
        #add the previous number to second
        tnum1 = store
        #set num1 equal to the previous num2
    print(tnum1)
    #print

def problem2():
    for i in range(0,51):
        ##Run through the different windspeeds

        #####I is the windspeed
        if i % 5==0:
            print("THE WINDSPEED IS",i, " ",end="")
            for z in range(-20,60):
                #Z is temp
                if z%10==0:
                    ##PRINT
                    val = windVal(z,i)
                    print ("{0:4f}".format(val), " ", end="")
            print("")
######HELPER FUNCTION FOR PROBLEM2
def windVal(z,i):
    ##Use the formula from the book
    val = 35.74 + .6215 * z - (35.75 * (i)**(.16)) + .4275 * z * ((i)**(.16))
    return val

def problem5():
    ##Run an input through the isPrime check (below)
    if isPrime(int(input("ENTER A NUMBER"))):
        #print yes prime
        print("YES -- PRIME")
        return 
    ##not prime
    print("NOT PRIME")
##########HELPER OF problem5() and problem6()
import math
def isPrime(number):
    for i in range(2,math.ceil(number)):
        ##Check if it is prime by seeing if it is divisible by a number smaller than it
        if number % i == 0:
            return False
    return True
    
def problem6():
    num = int(input("Enter the number to print all the prime numbers less than"))
    ##Get the number
    #run through all the numbers
    for i in range(2,num):
        #if it is prime, print it
        if isPrime(i):
            print(i, "is prime")
    
def problem9():
    starting = int(input("Please enter the starting odometer reading"))
    keepGoing = True
    totalMPG = 0
    data = []
    tMPGcalc = []
    while keepGoing:
        newData = input("ENTER the Distance and Gallons of gas used seperated by a space\n<Enter> to quit")
        if newData == "":
            break
        data.append(newData)
        ##ADD The data to the list of data
        
    for i in range(len(data)):
        print("Leg 1 MPG", float(data[i].split()[0])/float(data[i].split()[1]))
        ##print the mpg

        #########Add that to total mpg
        tMPGcalc.append(float(data[i].split()[0])/float(data[i].split()[1]))
    for i in range(len(tMPGcalc)):
        totalMPG += tMPGcalc[i]
        #create the total mpg
    #print 
    print("TOTAL MPG:", totalMPG/len(tMPGcalc))
        
def problem11():
    numColDays = int(0)
    numWarmDays = int(0)
    print("PLEASE MAKE SURE YOU HAVE ADDED the data into problem11data.txt.\n Make sure that each temp is on its own line.")
    input("Pleae press enter to confirm")
    data = open("problem11data.txt","r")
    ##Open the file
    info = data.readlines()
    #Read the lines

    for i in range(len(info)):
        if int(info[i]) < 60:
            numWarmDays+=1
        elif int(info[i]) > 80:
            numColDays+=1
    ###Print the toal
    print("There were {} warming days and {} cooling days".format(numWarmDays,numColDays))
    #Close file
    data.close()
    
