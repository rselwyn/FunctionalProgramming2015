#Ch11
#########5-8, 10, and 11

def problem5():
    liste = [0,3,10,2]
    liste = reverse(liste)
    print(liste)
    
def reverse(myList):
    newList = []
    lend = len(myList)-1
    while lend>=0:
        newList.append(myList[lend])
        lend = lend-1
    return newList
