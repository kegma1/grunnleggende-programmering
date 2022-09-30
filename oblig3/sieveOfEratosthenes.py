def sieve(limit):
    limit -= 1
    primes = [True] * limit
    for i, elm in enumerate(primes, start=1):
        if elm:
            for j in range(i + i, limit, i + 1):
                primes[j] = False

    primesAsNum = []
    for i, elm in enumerate(primes):
        if elm:
            primesAsNum.append(i + 2)
    return primesAsNum

userLimit = int(input("Enter a limit bigger than 1: "))
print(sieve(userLimit))

