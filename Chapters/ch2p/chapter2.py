def problem1():
    #include processes and inputs
    #here is the added introduction
    print("Wow! Isn't Europe cool, but the temperature is in Celsius?!?!")
    print("Use this program to convert celsius to fahrenheit")
    c = eval(input("celsius Temperature"))
    fahr = (9/5) * c +32
    print("The temperature is", fahr, "degrees Fahrenheit")
def problem2():
    print("this program prints the average of three scores")
    score1, score2, score3 = eval(input("Enter 3 scores sperated by commas"))
    average = (score1+score2+score3)/3
    print("The average is score is,", average)
def problem3():
    #include processes and inputs
    #here is the added introduction
    for i in range(5):
        c = eval(input("celsius Temperature"))
        fahr = (9/5) * c +32
        print("The temperature is", fahr, "degrees Fahrenheit")
def problem4():
    for i in range(100):
        if i%10 == 0:
            fahr = (9/5) * i +32
            print("The temperature is", fahr, "degrees Fahrenheit")
        
def problem5():
    years = eval(input("how many years for the investment"))
    apr = eval(input("interest rate"))
    principal = eval(input("principal"))
    for i in range(years):
        principal = principal * (1 +apr)

    print(principal)

    
    
    
    
