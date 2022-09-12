# Assume the availability of a function is_prime. Assume a variable n has been associated with positive integer. 
# Write the statements needed to compute the sum of the first n prime numbers. The sum should be associated with the variable total.
# Note: is_prime takes an integer as a parameter and returns True if and only if that integer is prime.

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
n = 4

total = 0
x = 0
i = 0
while not x == n:
    if is_prime(i):
        x += 1
        total += i
    i += 1

print(total)