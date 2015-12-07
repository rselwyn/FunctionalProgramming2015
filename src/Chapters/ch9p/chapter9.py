#!/usr/bin/env python
##Ch 9 PE: 3, 4, 7, 8, 11, 12 (DUE: 12/9)

from random import random
#Import the random module

##########PROBLEM 3
def problem3():
    a,b,n = getProblem3Inputs()
    gamesOneA, gamesOneB = simNGames(a,b,n)
    if gamesOneA > gamesOneB:
        print("A")
        return
    print("B")

def simNGames(a,b,n):
    winsa = 0
    winsb = 0
    for i in range(n):
        scoreA, scoreB = simGame(a,b)
        if scoreA > scoreB:
            winsa +=1
        else:
            winsb +=1
    return winsa,winsb
def simGame(pa,pb):
    serving = "A"
    scorea = 0
    scoreb = 0
    while not someoneHasOneP3(scorea,scoreb):
        num = random()
        if serving == "A":
            if num < pa:
                scorea+=1
            else:
                serving == "B"
        else:
            if num > pa:
                scoreb +=1
            else:
                serving == "A"
    return scorea,scoreb
            #...
            
        
def someoneHasOneP3(a,b):
    return a == 15 or b == 15

def getProblem3Inputs():
    a = float(input("enter prob for a"))
    b = 1-a
    n = int(input("Enter the nubmer of games"))
    return a,b,n




#######END PROBLEM 3





###############PROBLEM 4
def problem4():
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
    if scorea>=25 and scorea-scoreb>=2:
        return True
    if scoreb>=25 and scoreb-scorea>=2:
        return True
    return False

def whoWon(scorea,scoreb):
    if scorea>scoreb:
        print("A")
        return
    print("B")


#######END PROBLEM 4


########PROBLEM 7
def problem7():
    iterations = 0
    wins = 0
    losses = 0
    for i in range(iterations):
        if playgame():
            wins+=1
        else:
            losses+=1
            
        
        
def playGame():
    roll = roll()
def roll():
    number = math.ceil(random()*12)
    while number<2:
        number = math.ceil(random()*12)
    return number





#####END PROBLEM 7




########PROBLEM 8
def problem8():
    ##P8
    dealerCardCount = 0
    hasAce = False
    while (dealerCardCount<17 and hasAce==False) or (dealerCardCount<7 and hasAce) or (dealerCardCount<17 and hasAce==True):
        num = chooseCard()
        if num == 14:
            hasAce=True
            dealerCardCount+=1
        else:
            dealerCardCount += num
    if dealerCardCount>21:
        print("BUST")
        return True
    print("ALL GOOD")
    return False
            
def testProblemEight():
    bustPercent = 0
    for i in range(1000):
        if problem8():
            bustPercent+=1
    print(bustPercent/1000)
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
    
#####END PROBLEM 8
