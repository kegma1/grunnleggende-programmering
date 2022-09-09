# Assume the availability of a function is_prime. Assume a variable n has been associated with positive integer. 
# Write the statements needed to find out how many prime numbers (starting with 2 and going in 
# increasing order with successively higher primes [2,3,5,7,11,13,...]) can be added before the total exceeds n. 
# Associate this number with the variable k.
k = 0
temp = 0
for i in range(2, n + 1):
    if not is_prime(i):
        continue
    
    temp += i
    if temp > n:
        break
    k += 1

# bruh dette som how fungere