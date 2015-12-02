##Ch 9 PE: 3, 4, 7, 8, 11, 12 (DUE: 12/9)

from random import random

###############PROBLEM 3
def problem3():
    scorea = 0
    scoreb = 0
    a,b,n = getInputs()

    for i in range(n):
        while not someoneHasWon(scorea,scoreb):
        #Sim game
            if simulate(a,b):
                scorea+=1
            else:
                scoreb+=1
        whoWon(scorea,scoreb)
        scorea=0
        scoreb=0
def getInputs():
    a = float(input("Prob player 1 wins the serve"))
    b = 1-a
    n = int(input("Number of games to simulate"))
    return a,b,n
def simulate(a,b):
    number = random()
    if number<a:
        return True
    return False

def someoneHasWon(scorea,scoreb):
    if scorea>=15 and scorea-scoreb>=2:
        return True
    if scoreb>=15 and scoreb-scorea>=2:
        return True
    return False

def whoWon(scorea,scoreb):
    if scorea>scoreb:
        print("A")
        return
    print("B")


#######END PROBLEM 3



def problem8():
    ##P8
    dealerCardCount = 0
    hasAce = False
    while (dealerCardCount<17 and hasAce==False) or (dealerCardCount<7 and hasAce):
        num = chooseCard()
        if num == 14:
            hasAce=True
            dealerCardCount+=1
        else:
            dealerCardCount += num
    if dealerCardCount>21:
        print("BUST")
        return
    print("ALL GOOD")
            

def chooseCard():
    import math
    number = 0
    while 1>number:
        number = math.ceil(random()*14)
    if number>10 and (not number==14) :
        number = 10
    if number<=10:
        return number
    if number==14:
        return 14
    
    
    
