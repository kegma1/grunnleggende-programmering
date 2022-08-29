from random import randrange


playerInput = int(input("Make your move!\nRock[0]  Paper[1]  Scissor[2]\n"))

def numToName(x):
    if x == 0:
        return "Rock"
    elif x == 1:
        return "Paper"
    elif x == 2:
        return "Scissor"

if playerInput > 3:
    print("You can only choose 0, 1 or 2")
    exit()

cpuChoice = randrange(0, 3)

if playerInput == cpuChoice:
    print("Its a Draw!!\nYou picked", numToName(playerInput), "\nThe cpu picked", numToName(cpuChoice))
    exit()

winCondition = [(0, 2), (1, 0), (2, 1)]
loseContition = [(0, 1), (1, 2), (2, 0)]

gameCondition = (playerInput, cpuChoice)

if gameCondition in winCondition:
    print("You won!!\nYou picked", numToName(playerInput), "\nThe cpu picked", numToName(cpuChoice))
    exit()

if gameCondition in loseContition:
    print("You lost!!\nYou picked", numToName(playerInput), "\nThe cpu picked", numToName(cpuChoice))
    exit()