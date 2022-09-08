# Assume there are two variables, k and m, each already associated with a positive integer value and further 
# assume that k's value is smaller than m's. Write the code necessary to compute the number of perfect squares 
# between k and m. (A perfect square is an integer like 9, 16, 25, 36 that is equal to the square of another integer 
# (in this case 3*3, 4*4, 5*5, 6*6 respectively).) Associate the number you compute with the variable q. For example, 
# if k and m had the values 10 and 40 respectively, you would assign 3 to q because between 10 and 40 there are these perfect 
# squares: 16, 25, and 36,.

k = 10
m = 40

from math import sqrt

listOfSqrt = []
teller = k
while teller != m:
    root = sqrt(teller)
    if int(root + 0.5) ** 2 == teller:
        listOfSqrt.append(teller)
    else:
        pass
    teller += 1

q = len(listOfSqrt)
print(q)