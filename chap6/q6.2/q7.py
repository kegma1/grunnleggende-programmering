# Define a function is_prime that receives an integer argument and returns True if the 
# argument is a prime number and otherwise returns False. (An integer is prime if it is greater 
# than 1 and cannot be divided evenly [with no remainder] other than by itself and one. For example, 
# 15 is not prime because it can be divided by 3 or 5 with no remainder. 13 is prime because only 1 and 13 divide it with no remainder.)

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

for i in range(100_000_000):
    print(i, is_prime(i))