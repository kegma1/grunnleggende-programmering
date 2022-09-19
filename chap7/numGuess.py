from re import T


print("Choose a number between 0-100!")

isFound = False
tries = 0
highest = 100
lowest = 0
cpuGuess = 50

while not isFound:
   
    answer = input(f"is yor number {cpuGuess}? [yes/higher/lower]: ")

    if answer == "yes":
        print(f"Excellent!! It took {tries} tries to guess")
        isFound = True
    elif answer == "higher":
        lowest = cpuGuess
        cpuGuess = (highest + lowest) // 2
    elif answer == "lower":
        highest = cpuGuess
        cpuGuess = (highest + lowest) // 2
    else:
        print("invalid answer.")
    tries += 1
    

    

