def problem1():
    #here is the added introduction
    print("Wow! Isn't Europe cool, but the temperature is in Celsius?!?!")
    #the rest is just copying from textbook
    print("Use this program to convert celsius to fahrenheit")
    c = eval(input("celsius Temperature"))
    fahr = (9/5) * c +32
    print("The temperature is", fahr, "degrees Fahrenheit")
def problem2():
    print("this program prints the average of three scores")
    #taking in three scores
    score1, score2, score3 = eval(input("Enter 3 scores sperated by commas"))
    #calculating average
    average = (score1+score2+score3)/3
    #printing the output
    print("The average is score is,", average)
def problem3():
    #runs the previous code 5 times, takes in a new input each time
    for i in range(5):
        #same code as problem 1
        c = eval(input("celsius Temperature"))
        #input
        fahr = (9/5) * c +32
        print("The temperature is", fahr, "degrees Fahrenheit")
        #output
def problem4():
    
    # the loop runs 100 times
    for i in range(100):
        # i%10 checks to see if the remainder after being divided by 10 is 0, definition of being divisible by 10
        if i%10 == 0:
            #using variable i from before, convert it to fahrenheit
            fahr = (9/5) * i +32
            #output the temperature in F
            print("The temperature is", fahr, "degrees Fahrenheit")
        
def problem5():
    years = eval(input("how many years for the investment"))
    #get the years for investment
    apr = eval(input("interest rate"))
    #get the apr
    principal = eval(input("principal"))
    #get the principal

    #iterate the loop for the number of years
    for i in range(years):

        #each year, multiply the principal times the investment rate (this loop is basically the compound interest formula)
        #we need to add 1 to convert the percent to a decimal
        principal = principal * (1 +apr)
    #the output
    print(principal)

    
    
    
    
