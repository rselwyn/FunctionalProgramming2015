#WRITE A FUNCTION THAT COMPUTES THE AREA OF A TRIANGLE GIVEN THE LENGTH
#OF ITS THREE SIDES AS PARAMETERS



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
