# Assume there is a variable, h already associated with a positive integer value. 
# Write the code necessary to count the number of perfect squares whose value is less than h, starting with 1. 
# (A perfect square is an integer like 9, 16, 25, 36 that is equal to the square of another integer 
# (in this case 3*3, 4*4, 5*5, 6*6 respectively).) Assign the sum you compute to a variable q. For example, if his 19, 
# you would assign 4 to q because there are perfect squares (starting with 1) that are less than h are:1, 4, 9, 16.

h = 19
from math import sqrt

listOfSqrt = []
teller = 1
while teller != h:
    root = sqrt(teller)
    if int(root + 0.5) ** 2 == teller:
        listOfSqrt.append(teller)
    else:
        pass
    teller += 1

q = len(listOfSqrt)
print(q)