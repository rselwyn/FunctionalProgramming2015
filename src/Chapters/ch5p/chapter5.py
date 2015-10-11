#programming for ch5:
#problems 1-4, 6,9-12
# 8,15,16 e
def problem1():
    #get the date
    day, month,year = eval(input("Enter the day, month, and year seperated by commas"))
    #use string formatting to put together the easy format
    date1 = "{}/{}/{}".format(str(month), str(day), str(year))

    months = ["January","February","March","April","May","June","July","August","September","October", "November", "December"]
    #catalog all the months for reference
    
    #use the cataloged array to get the string format of the month number
    strMonth = months[month-1]

    date2 = "{} {}, {}".format(strMonth,str(day),str(year))
    #format into a string

    #print it
    print("The date is",date1, "or", date2, ".")
def problem2():
    x = float(input("Enter the quiz score"))
    #get the input of the quiz score as a number

    #print it out as the corresponding letter grade
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
    #get the score as a number
    x = float(input("Enter the quiz score"))
    
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
def problem4():
    ac = " " + input("Please enter the string that to make an acronym")
    #get the string

    final = ""
    #initialize the final acronym string

    #the algorithim runs through the string. If there is a space, it takes the next letter and capitalizes it and adds it to the final string.
    for i in range(len(ac)):
        if ac[i] == " ":
            final = final + ac[i+1].capitalize()
    #print out the final acronym
    print(final)
    
def problem6():
    #see readme for line by line explanation
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
    #get a piece of text
    text = text.split()
    #split the text up into words
    #because each index of the array is a word, I can calculate the number of words with len()
    print("THere are ", len(text), "words in your entry")
def problem10():
    text = input("Enter a string of text for which I can calculate the average length of the words.")
    #get the string of text
    length = text.split()
    #split the text into an array of the words
    numOfWords = len(length)
    #calculate the number of words in the text
    numOfLetters = 0
    for i in range(len(text)):
    
        if text[i] != " ":
            #if the character isn't a space, add 1 to the letters
            numOfLetters+=1
    #print the average length of words
    print(numOfLetters/numOfWords)

def problem11():
    print("This is a chaotic function")
    x = float(input("Enter a number between 0 and 1"))
    y = float(input("Enter another number between 0 and 1"))
    iterations = int(input("Enter the number of iterations of the chaotic loop"))
    #get all the info
    

    print("Index   ",x, "    ", y)
    print("-----------------------------")
    #print the top bar
    for i in range(iterations):
    	#calculate the next val in the series
        x = 3.9 * x * (1-x)
        y = 3.9 * y * (1-y)
	#format it into a string -- the second argument has .4f to round to the 10K digit
        print ("{0}         {1:0.4f}    {2:0.4f}".format(i,x,y)      )
 
def problem12():
    principal = float(input("Enter the principal"))
    apr = float(input("Enter the apr"))
    years = int(input("Enter the years"))
    print("Year    Value")
    print("-----------------")
    for i in range(years+1):
        if i < 10:
            print("{0}       {1:0.2f}".format(i, principal))
            principal = principal*(1+apr)
        elif i < 100:
            print("{0}      {1:0.2f}".format(i, principal))
            principal = principal*(1+apr)
        
    
