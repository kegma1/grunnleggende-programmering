# Given that n refers to a positive integer, use a while loop to compute 
# the sum of the cubes of the first n counting numbers, and associate this 
# value with total. Use no variables other than n, k, and total.

n = 50
k = 1
total = 0
while k < n:
    total += k * k
    k += 1
