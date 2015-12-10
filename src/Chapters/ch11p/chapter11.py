#Ch11
#########5-8, 10, and 11

def problem5():
    print("The functions are reverse(myList), count(myList, numberToCOunt)")
    return
    
    
def reverse(myList):
    newList = []
    lend = len(myList)-1
    while lend>=0:
        newList.append(myList[lend])
        lend = lend-1
    return newList

def count(myList, num):
    count = 0
    for i in myList:
        if num == int(i):
            count+=1
    return count

def index(myList, lookFor):
    for i in range(len(myList)):
        if myList[i] == lookFor:
            return i
def sort():
    myList = [3,25,7,10]
    while not inOrder(myList):
        myList = exchange(myList)
    print(myList)
    
def exchange(myList):
    elem = len(myList)-1
    for i in range(elem):
        if (myList[i] > myList[i+1]):
            myList[i],myList[i+1] = myList[i+1],myList[i]
    return myList

def inOrder(myList):
    for i in range(len(myList)-1):
        if (myList[i] < myList[i+1]):
            continue
        else:
            return False
    return True
def isin(myList,lookFor):
    for i in myList:
        if i == lookFor:
            return True
    return False
from random import *
def shuffle(arr):
    #Help from http://code.activestate.com/recipes/360461-fisher-yates-shuffle/ and https://en.wikipedia.org/wiki/Fisher–Yates_shuffle
    #Implementation of Fisher-Yates shuffle
    a=len(arr)
    less=a-1
    for d in range(less,0,-1):
      e=randint(0,d)
      if e == d:
            continue
      arr[d],arr[e]=arr[e],arr[d]
    return arr


def problem6():
    return

def problem7():
    print(innerProd([1,2,3],[3,2,1]))
    
def innerProd(x,y):
    num = 0
    for i in range(len(x)):
        num += x[i]*y[i]
    return num

def problem8():
    somelist = [0,1,2,3,4,2,3,1,2]
    print(removeDuplicates(somelist))

def removeDuplicates(liste):
    newList = []
    for i in liste:
        if i not in newList:
            newList.append(i)
    return newList
        
def problem10():
    n = int(input("Enter the number"))
    badnums = []
    primes = []
    for i in range(2,n+1):
        if i not in badnums:
            print(i)
            primes.append(i)
            for b in range(i,n+1):
                if b%i==0:
                    badnums.append(b)
    print(primes)
        

def problem11():
    fileLoc = "problem11.txt"
    totalWords = []
    with open(fileLoc,'r') as f:
        for line in f:
            for word in line.split():
                if word.lower() in swearWords:
                    print ("****")
                    totalWords.append("****")
                else:
                    print(word)
                    totalWords.append(word)
        f.close()
    with open(fileLoc, 'w') as f:
        for words in totalWords:
            f.write(words+" ")
        f.close()
            
