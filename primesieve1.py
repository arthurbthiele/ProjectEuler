#this will be a good prime sieve that can be used to get primes up to a value n

import numpy as np

n = 2000000
potentialprimes = range (0, n)
isprime = [1]*n
for p in potentialprimes[2:]:
    if p % 2 == 0:
        isprime[p] = 0
    elif isprime[p] == 1:
        for i in range (2, int(np.floor(n/p))+1):
            if p*i < len(isprime):
                isprime[p*i] = 0


primes = []
for i in range(2, n):
    if isprime[i] == 1:
        primes.append(potentialprimes[i])
print primes[0], primes[1]
