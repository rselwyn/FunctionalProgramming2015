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
            
