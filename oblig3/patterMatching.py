def isConsecutiveFour(values):
    lastValue = 0
    count = 0
    for value in values:
        if count == 3:
            return True
        if value == lastValue:
            count += 1
        else:
            lastValue = value
            count = 0
    return False

userInput = input("Enter integers separated by spaces from one line: ")
userInput = [int(x) for x in userInput.split(" ")]

if isConsecutiveFour(userInput):
    print("The series has consecutive fours")
else:
    print("The series has no consecutive fours")

