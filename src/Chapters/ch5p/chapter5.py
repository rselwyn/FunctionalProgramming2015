#programming for ch5
#problems 1-4, 6,9-12
# 8,15,16 e
def problem1():
    #citing https://pyformat.info for string formating
    day, month,year = eval(input("Enter the day, month, and year seperated by commas"))
    date1 = "{}/{}/{}".format(str(month), str(day), str(year))
    months = ["January","February","March","April","May","June","July","August","September","October", "November", "December"]
    strMonth = months[month-1]
    date2 = "{} {}, {}".format(strMonth,str(day),str(year))
    print("The date is",date1, "or", date2, ".")
def problem2():
    x = float(input("Enter the quiz score"))
    if x == 5:
        print("A")
    elif x == 4:
        print("B")
    elif x == 3:
        print("C")
    elif x ==2:
        print("D")
    else:
        print("F")
def problem3():
    x = float(input("Enter the quiz score"))
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
def problem4():
    ac = " " + input("Please enter the string that to make an acronym")
    final = ""
    for i in range(len(ac)):
        if ac[i] == " ":
            final = final + ac[i+1].capitalize()
    print(final)
    
            
        
