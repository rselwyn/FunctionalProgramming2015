#chapter 6 programmng assignments
#4,6,7,9-13
#bonus 3,9,14-17



############## PROBLEM 4 ###################

#WRITE A PROGRAM THAT SUMS THE FIRST n NATURAL NUMBERS
#WRITE A PROGRAM THAT SUMS THE CUBE OF THE FIRST n NATURAL NUMBERS

def sumN(x):
    #prints natural numbers
    #x is the number of natural numbers
    y = 0
    #y is the value where the numbers get accumulated
    for i in range(int(x+1)):
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
print("PROBLEM 4")
sumN(int(input("ENTER THE NUMBER OF NATURAL NUMBERS TO BE ADDED")))

sumNCubes(int(input("ENTER THE NUMBER OF NATURAL NUMBERS TO BE CUBED AND THEN ADDED")))


#END PROBLEM 4

########## PROBLEM #6 ####################

#WRITE A FUNCTION THAT COMPUTES THE AREA OF A TRIANGLE GIVEN THE LENGTH
#OF ITS THREE SIDES AS PARAMETERS


print("PROBLEM 6")

a = float(input("enter the value of side 1"))
b = float(input("enter the value of side 2"))
c = float(input("enter the value of side 3"))

def area(a,b,c):
    #get side lengths value
    #calculate the value of (a+b+c)/2
    s = (a+b+c)/2
    #use the formula provided in the book to find the area
    area = (s*(s-a)*(s-b)*(s-c))**(1/2)
    print("the area is", area)
    

area(a,b,c)

############# END PROBLEM 6


############## PROBLEM 7 ##############

#WRITE A FUNCTION THAT COMPUTES THE nth FIBONACCI NUMBER


print("PROBLEM 7")
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


####### END PROBLEM 7

#######PROBLEM 9 ##############

print("PROBLEM 9")
def grade(x):
    #get the score as a number
    #convert the number to a letter grade
    if x >=90:
        print("A")
    elif x>=80:
        print("B")
    elif x>=70:
        print("C")
    elif x >=60:
        print("D")
    else:
        print("F")

x = float(input("Enter the quiz score"))
grade(x)


###### END PROBLEM 9

######### Problem 10

print("PROBLEM 10")
ac = " " + input("Please enter the string that to make an acronym")
def acronym(ac):
    final = ""
    #initialize the final acronym string

    #the algorithim runs through the string. If there is a space, it takes the next letter and capitalizes it and adds it to the final string.
    for i in range(len(ac)):
        if ac[i] == " ":
            final = final + ac[i+1].capitalize()
    #print out the final acronym
    print(final)
    
acronym(ac)
####END Problem 10

######PROBLEM 11

print("PROBLEM 11")
def squareEach(nums):
    for i in range(len(nums)):
        #print(type(nums[i]))
        nums[i] = float(nums[i])   
        nums[i] = nums[i]**2
        
    print(nums)

squareEach(input("EENTER A LIST OF NUMBERS SEPERATED BY COMMAS, NO NEED FOR BRACKETS").split(","))

##END

###PROBLEM 12
print("PROBLEM 12")
def sumList(nums):
    total = float(0)
    for i in range(len(nums)):
        #print(type(nums[i]))
        nums[i] = float(nums[i])   
        total = total + nums[i]
        
    print(total)

sumList(input("ENTER A LIST OF NUMBERS SEPERATED BY COMMAS. NO NEED FOR BRACKETS").split(","))

##END

###PROBLEM 13

##MY sumList() function works for problems 12 and 13
print("PROBLEM 13")
def sumList(nums):
    total = float(0)
    for i in range(len(nums)):
        #print(type(nums[i]))
        nums[i] = float(nums[i])   
        total = total + nums[i]
        
    print(total)

sumList(input("ENTER A LIST OF NUMBERS SEPERATED BY COMMAS. NO NEED FOR BRACKETS").split(","))


