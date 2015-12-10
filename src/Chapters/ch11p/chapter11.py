#Ch11
#########5-8, 10, and 11


#######PROBLEM 5
def problem5():
    print("The functions are reverse(myList), count(myList, numberToCOunt), index(myList,lookFor), sort(list),isin()")
    #PRint intro and exit
    return
    
def reverse(myList):
    #initialize list
    newList = []
    #Get the length -1 
    lend = len(myList)-1
    #Run a pretty much backwards for loop and it to the list
    while lend>=0:
        newList.append(myList[lend])
        lend = lend-1
    #Return the list
    return newList

def count(myList, num):
    ##init the count
    count = 0
    #iterate through the list looking for the number
    for i in myList:
        if num == int(i):
            #If found. add one to count
            count+=1
    #return the count
    return count

def index(myList, lookFor):
    for i in range(len(myList)):
        #iterate through and lookFor the value
        if myList[i] == lookFor:
            #If found, return the index 
            return i
def sort(liste):
    myList = liste[:]
    #init the list
    while not inOrder(myList):
        #While not in order, exchange
        myList = exchange(myList)
    print(myList)


def exchange(myList):
    ##BUBLE Sort implementation
    elem = len(myList)-1
    for i in range(elem):
        if (myList[i] > myList[i+1]):
            myList[i],myList[i+1] = myList[i+1],myList[i]
    return myList

def inOrder(myList):
    #Check if the list is in order (for the entire list, myList[i] < myList[i+1])
    for i in range(len(myList)-1):
        if (myList[i] < myList[i+1]):
            continue
        else:
            return False
    return True
def isin(myList,lookFor):
    #Look for the value 
    for i in myList:
        if i == lookFor:
            #If found, return true, else false
            return True
    return False

####END PROBLEM 5
from random import *
def shuffle(arr):
    #Help from http://code.activestate.com/recipes/360461-fisher-yates-shuffle/ and https://en.wikipedia.org/wiki/Fisher–Yates_shuffle
    #Implementation of Fisher-Yates shuffle
    a=len(arr)
    #Init the value
    less=a-1
    #Subtract one
    for d in range(less,0,-1):
    #Loop through and switch values
      e=randint(0,d)
      if e == d:
            continue
        #Swap the values
      arr[d],arr[e]=arr[e],arr[d]
      #return it
    return arr

def problem6():
    ####get input
    arr = [int(i) for i in input("ENTER numbers seperated by commas").split(",")]
    print(shuffle(arr))

def problem7():
    ##EX: Printing the inner product of the two arrays below
    print("THIS IS AN EXAMPLE calculation, see code for more details")
    print(innerProd([1,2,3],[3,2,1]))
    
def innerProd(x,y):
    #calc the inner product using its formula
    num = 0
    for i in range(len(x)):
        num += x[i]*y[i]
    return num

def problem8():
    
    somelist = [int(i) for i in input("ENTER numbers seperated by commas").split(",")]
    #get values

    #Print the removed dupes version
    print(removeDuplicates(somelist))

def removeDuplicates(liste):
    newList = []
    for i in liste:
        #go through the old list
        if i not in newList:
            #if it isnt in the list, add it
            newList.append(i)
    #return it
    return newList
        
def problem10():
    #Get the num to which the primes will be found
    n = int(input("Enter the number"))

    #Initialize the list of blackout numbers
    badnums = []
    #list of primes
    primes = []
    for i in range(2,n+1):
        #Iterate through the nums

        #if it isnt a bad number, add it
        if i not in badnums:
            print(i)
            primes.append(i)
            #make it and its multiple bad numbers as for the formula
            for b in range(i,n+1):
                if b%i==0:
                    badnums.append(b)
    #print out the primes
    print(primes)
        

def problem11():
    swearWords = []
##Swear words go in there
    #The file loc
    fileLoc = "problem11.txt"
    #The words
    totalWords = []
    with open(fileLoc,'r') as f:
        #open the file
        for line in f:
            #in each line
            for word in line.split():
                #If the word is a swear, fix it
                if word.lower() in swearWords:
                    print ("****")
                    totalWords.append("****")
                else:
                    #Just add it regularly if it isnt a swear
                    print(word)
                    totalWords.append(word)
        #close the file
        f.close()
    #open the file again
    with open(fileLoc, 'w') as f:
        for words in totalWords:
            #print out all the words into the file
            f.write(words+" ")
        #close it again
        f.close()
            
