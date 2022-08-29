from random import randint
RANGE = 10
ROUNDS = 5
score = 0
for _ in range(ROUNDS):
    num1 = randint(-RANGE, RANGE)
    num2 = randint(-RANGE, RANGE)
    solution = num1 + num2
    answer = int(input("What is the solution to " + str(num1) + " + " + str(num2) + " = "))
    if answer == solution:
        print("Correct!!\n")
        score += 1
    else:
        print("Wrong!!\n")
print("Your score is", str(score) + "/" + str(ROUNDS))
