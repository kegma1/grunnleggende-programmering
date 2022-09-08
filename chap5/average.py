# Write a program that reads an unspecified number of integers, determines how many positive and negative values have been read, 
# and computes the total and average of the input values (not counting zeros). Your program ends with the input 0. Display the 
# average as a floating-point number.

# Sample Run 1
# Sample Output 1:
# Enter an integer, the input ends if it is 0: 1 
# Enter an integer, the input ends if it is 0: 2 
# Enter an integer, the input ends if it is 0: -1 
# Enter an integer, the input ends if it is 0: 3 
# Enter an integer, the input ends if it is 0: 0 
# The number of positives is 3
# The number of negatives is 1
# The total is 5
# The average is 1.25
# Sample Run 2
# Sample Output 2:
# Enter an integer, the input ends if it is 0: 0 
# No numbers are entered except 0

listOfInputValues = []


while True:
    userValue = int(input("Enter an integer, the input ends if it is 0: "))

    if len(listOfInputValues) == 0 and userValue == 0:
        print("No numbers are entered except 0")
        exit()

    if userValue == 0:
        break
    else:
        listOfInputValues.append(userValue)

# count positives and negatives
pos = 0
neg = 0
for x in listOfInputValues:
    if x < 0:
        neg += 1
    else:
        pos += 1
print(f"The number of positives is {pos}")
print(f"The number of negatives is {neg}")
print(f"The total is {sum(listOfInputValues)}")
print(f"The average is {sum(listOfInputValues) / len(listOfInputValues)}")