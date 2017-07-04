import numpy as np
#finding the sum of primes less than two MILLION!
#gonna use a PRIME SIEVE which is heaps cool
#primes up to n:

n = 2000000
potentialprimes = range (0, n)
isprime = [1]*n

for p in potentialprimes[2:]:
    if isprime[p] == 1:
        for i in range (2, int(np.floor(n/p))+1):
            if p*i < len(isprime):
                isprime[p*i] = 0


primes = []
for i in range(0, n):
    if isprime[i] == 1:
        primes.append(potentialprimes[i])
print primes
print len(primes)
