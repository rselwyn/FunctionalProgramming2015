#MOST OF NOTES ARE IN README
def problem1():
    # the assignment was to print the different literals and expressions requested by the book
    #There are no inputs, the outputs are what is printed by all the print statements below
    print("hello, world!")
    print("hello", "world")
    print(3)
    print(3.0)
    print(2+3)
    print(2.0+3.0)
    print("2" + "3")
    print("2 + 3 =", 2+3)
    print(2*3)
    print(2**3)
    print(2/3)
    print(2.0/3.0)
    
def problem2():
    #This program takes in a value (x), this is iterated on 10 times
    #the output is the value of x = 3.9 * x * (1-x) where x is the entered value
    #the output value is changed because x is changed every time with the condition x = 3.9 * x * (1-x)
    #for this problem, the question just said to copy the code from the book
    print("This is a chaotic function")
    x = float(input("Enter a number between 0 and 1"))
    for i in range(10):
        x = 3.9 * x * (1-x)
        print (x)
def problem3():
      #This program takes in a value (x), this is iterated on 10 times
     #the output is the value of x = 3.9 * x * (1-x) where x is the entered value
    #the output value is changed because x is changed every time with the condition x = 3.9 * x * (1-x)
    #for this problem, the question just said to copy the code from the book, except change 3.8 to 2.0
    print("This is a chaotic function")
   
    x = float(input("Enter a number between 0 and 1"))
    for i in range(10):
        #The multiplier was changed from 3.8 to 2.0
        x = 2.0 * x * (1-x)
        print (x)
def problem4():
    print("This is a chaotic function")
     #This program takes in a value (x), this is iterated on 20 times
    # more notes  in readme
    x = float(input("Enter a number between 0 and 1"))
    for i in range(20):
        #The in range() was changed to range(20) instead of 10
        x = 3.9 * x * (1-x)
        print (x)
        
def problem5():
    print("This is a chaotic function")
    #This program takes in a value (y) and (x)
    #y is the number of iterations
    #x is the value being changed in each iteration
    x = float(input("Enter a number between 0 and 1"))
    y = int(input("How many iterations"))
    # y is casted to an int because the function range() requires an int
    for i in range(y):
        #iterates y times
        x = 3.9 * x * (1-x)
        print (x)
        
def problem7():
    #notes in readme
    print("This is a chaotic function")
    x = float(input("Enter a number between 0 and 1"))
    y = float(input("Enter another number between 0 and 1"))
    print("input   ",x, "  ", y)
    print("-----------------")
    for i in range(10):
        
        x = 3.9 * x * (1-x)
        y = 3.9 * y * (1-y)
        print (x,"--",y)
 
        


        
