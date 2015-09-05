def type1():
    #this uses the formula 3.9 * x * (1-x)
    print("This is a chaotic function")
    x = float(input("Enter a number between 0 and 1"))
    for i in range(10):
        x = 3.9 * x * (1-x)
        print (x)
def type2():
    #this uses the formula 3.9 * (x-x*x)
    print("This is a chaotic function")
    x = float(input("Enter a number between 0 and 1"))
    for i in range(10):
        x = 3.9 * (x-x*x)
        print (x)
def type1():
    #this uses the formula 3.9 * x - 3.9*x*x
    print("This is a chaotic function")
    x = float(input("Enter a number between 0 and 1"))
    for i in range(10):
        x = 3.9 * x - 3.9*x*x
        print (x)
