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
