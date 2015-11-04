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
                    val = 35.74 + .6215 * z - (35.75 * (i)**(.16)) + .4275 * z * ((i)**(.16))
                    print ("{0:4f}".format(val), " ", end="")
            print("")
            
def problem5():
    if isPrime(int(input("ENTER A NUMBER"))):
        print("YES -- PRIME")
        return 
    
    print("NOT PRIME")

##########HELPER OF problem5() and problem6()
import math
def isPrime(number):
    for i in range(2,math.ceil(number)):
        if number % i == 0:
            return False
    return True
    
def problem6():
    num = int(input("Enter the number to print all the prime numbers less than"))
    for i in range(2,num):
        if isPrime(i):
            print(i, "is prime")
    
def problem9():
    starting = int(input("Please enter the starting odometer reading"))
    keepGoing = True
    totalMPG = 0
    data = []
    tMPGcalc = []
    while keepGoing:
        newData = input("ENTER the Distance and Gallons of gas used seperated by a space")
        if newData == "":
            break
        data.append(newData)
    for i in range(len(data)):
        print("Leg 1 MPG", float(data[i].split()[0])/float(data[i].split()[1]))
        tMPGcalc.append(float(data[i].split()[0])/float(data[i].split()[1]))
    for i in range(len(tMPGcalc)):
        totalMPG += tMPGcalc[i]
    print("TOTAL MPG:", totalMPG/len(tMPGcalc))
        
def problem11():
    numColDays = int(0)
    numWarmDays = int(0)
    print("PLEASE MAKE SURE YOU HAVE ADDED the data into problem11data.txt.\n Make sure that each temp is on its own line.")
    input("Pleae press enter to confirm")
    data = open("problem11data.txt","r")
    info = data.readlines()
    for i in range(len(info)):
        if int(info[i]) < 60:
            numWarmDays+=1
        elif int(info[i]) > 80:
            numColDays+=1
    print("There were {} warming days and {} cooling days".format(numWarmDays,numColDays))
    data.close()
    
