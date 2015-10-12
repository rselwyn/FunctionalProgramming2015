#WRITE A FUNCTION THAT COMPUTES THE nth FIBONACCI NUMBER


def fib(hm):

    tnum1 = 0
    #first number is zero
    tnum2 = 1
    #second is 1
    store = 0
    #get the number of fibonnaci numbers, cast it to an int because we cant have
    #a loop iterate 1.23 times    
    for i in range(hm):
        store = tnum2
        #set another value equal to the second number
        tnum2 += tnum1
        #add the previous number to second
        tnum1 = store
        #set num1 equal to the previous num2
    print(tnum1)
    #print

hm = int(input("which fibonnaci number do you want to print?"))
fib(hm)
