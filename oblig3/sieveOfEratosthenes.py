def sieve(limit):
    primes = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if primes[p]:
            for j in range(p * p, limit + 1, p):
                primes[j] = False
        p += 1

    for i in range(2, limit+1):
        if primes[i]:
            print(i)

userLimit = int(input("Enter a limit bigger than 1: "))
sieve(userLimit)

