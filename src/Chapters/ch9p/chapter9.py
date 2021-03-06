#!/usr/bin/env python
##Ch 9 PE: 3, 4, 7, 8, 11, 12 (DUE: 12/9)

from random import random
#Import the random module

##########PROBLEM 3

########MOST OF THE CODE WAS TAKEN FROM THE TEXTBOOK; THEREFORE, it doesnt have too many comments
def problem3():
    a,b,n = getProblem3Inputs()
    #Get the inputs

    #sim the games
    gamesOneA, gamesOneB = simNGames(a,b,n)
    if gamesOneA > gamesOneB:
        #If a has ore wins, they have one
        print("A " + str(gamesOneA + "were won"))
        return
    print("B " + str(gamesOneB + "were won"))

#Run n simulations
def simNGames(a,b,n):
    winsa = 0
    winsb = 0
    for i in range(n):
        scoreA, scoreB = simGame(a,b)
        if scoreA > scoreB:
            winsa +=1
        else:
            winsb +=1
    #returns num of wins each
    return winsa,winsb
def simGame(pa,pb):
    ##One simulation - p(a) and p(b) are inputs
    serving = "A"
    scorea = 0
    scoreb = 0
    #While someone hasnt won, simulate
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

########MOST OF THE CODE WAS TAKEN FROM THE TEXTBOOK; THEREFORE, it doesnt have too many comments
#####SEE PROBLEM 3 for documentation.  This problem is very similar
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
    #He doesnt have an ae

    #While the dealer should still draw
    while (dealerCardCount<17 and hasAce==False) or (dealerCardCount<7 and hasAce) or (dealerCardCount<17 and hasAce==True):
        num = chooseCard()
        #Choose a card
        #If it an ace, set the value
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

##WHAT YOU CAN USE TO TEST PROBLEM 8
def testProblemEight():
    bustPercent = 0
    for i in range(1000):
        if problem8():
            bustPercent+=1
    print(bustPercent/1000)

    #CHOOSE CARD
def chooseCard():
    import math
    number = 0
    #CHOOSE A NUMBER
    while 1>number:
        number = math.ceil(random()*14)
    if number>10 and (not number==14) :
        #IF IT IS A FACE CARD, just return 10
        number = 10
    if number<=10:
        #If regular, just return num
        return number
    if number==14:
        #if ace, return 14
        return 14
    
#####END PROBLEM 8


#####PROBLEM11
def problem11():
    #Run 1mil iterations
    iterations = 1000000
    #count of 5 in a rows
    fiveInARow = 0
    #run iteration times
    for i in range(iterations):
        #if it rolls a five in a row
        if runOnce():
            #add to the number
            fiveInARow +=1
    print("THE probability is"+ str(fiveInARow/iterations))

def rollP11():
    #one roll
    import math
    #will return a 1-6
    number = math.ceil(random()*6)
    return number

def runOnce():
    nums = []
    #numbers
    for i in range(6):
        nums.append(rollP11())
        #add to the array
        if (i != 0):
            #If the num is equal to thre previous one, keep adding
            if nums[i] == nums[i-1]:
                continue
            return False
    return True
            
        

###END PROBLEM 11


####PROBLEM 12
def problem12():
    iters = 100
    #A hundred iterations
    num = 0
    #nums is the total steps
    for i in range(iters):
        num += runOnce12()
    print(num/iters, end="")
    #Calculate the average ^^^^
    #Print the rest of the message below
    print(" is the average steps among 100 iterations of 1000 step walks (1mil iters total)")
        
    
def runOnce12():
    n = 1000
    #^^ One thousands steps
    num = 0
    #Current Steps ^^
    for i in range(n):
        #If step is true, go forward 1
        if step():
            num+=1
        #Else go back one
        else:
            num = num -1
 #   print(num)
    return num

def step():
    #Return steps as boolean
    if random() > .5:
        return True
    return False


###End problem 12

