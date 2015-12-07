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



def problem6():
    return

def problem7():
    print(innerProd([1,2,3],[3,2,1]))
    
def innerProd(x,y):
    num = 0
    for i in range(len(x)):
        num += x[i]*y[i]
    return num





