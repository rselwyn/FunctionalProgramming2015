#WRITE A PROGRAM THAT SUMS THE FIRST n NATURAL NUMBERS
#WRITE A PROGRAM THAT SUMS THE CUBE OF THE FIRST n NATURAL NUMBERS

def sumN(x):
    #prints natural numbers
    #x is the number of natural numbers
    y = 0
    #y is the value where the numbers get accumulated
    for i in range(x+1):
        #assuming that the set of natural numbers is all integers
        #(0, infinity) in interval notation
        #add one to nuber of iterations because natural numbers don't include zero
        #add the current number the loop is on to the total
        y = y+ i
    #print the total
    print(y)

def sumNCubes(x):
    #x is the number of natural numbers)
    y = 0
    #y is the accumulator
    for i in range(x+1):
        #assuming that the set of natural numbers is (0, infinity) in interval notation
        #add one because natural numbers dont include zero
        
        #add the cube of the current number to the total
        y = y+ i**3
    #print the accumulated value
    print(y)

#INVOKE THE FUNCTIONS

sumN(input("ENTER THE NUMBER OF NATURAL NUMBERS TO BE ADDED"))

sumNCubes(input("ENTER THE NUMBER OF NATURAL NUMBERS TO BE CUBED AND THEN ADDED"))


