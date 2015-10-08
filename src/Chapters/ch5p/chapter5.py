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
    
def problem6():
    #minor help from http://stackoverflow.com/questions/3847472/get-index-of-character-in-python-list
    text = input("enter a name to calculate the value of")
    total = int(0)
    charray = [" ", "A","B","C","D","E","F","G","H","I", "J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    capital = ""
    for i in range(len(text)):
        capital = text[i].capitalize()
        for i in charray:
            if capital == i:
                total = total + int(charray.index(capital))
    print(total)
def problem9():
    text = input("Enter some text for which I can calculate the number of words.")
    text = text.split()
    print("THere are ", len(text), "words in your entry")
def problem10():
    text = input("Enter a string of text for which I can calculate the average length of the words.")
    text = text.split()
    tls = 0
    numw = len(text)
    for i in range(len(text)):
        tls += len(text[i])
    print(tls/numw)
    
