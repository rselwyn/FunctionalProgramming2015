##Ch 9 PE: 3, 4, 7, 8, 11, 12 (DUE: 12/9)


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
    from random import random
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


