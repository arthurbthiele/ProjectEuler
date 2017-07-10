import numpy as np

#this should return the proper divisors of any integer n in the form of a list, not including the number itself
import numpy as np
def divisors(n): #this is the number for which we want the proper divisors
    divisors = [1]
    for count in range (2, int(np.floor(np.sqrt(n)) + 1)):
        if n % count == 0:
            if count != n/count:
                divisors += [count, n/count]
            elif True:
                divisors.append(count)
    return divisors

def primes(n): #returns primes up to n
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
    return primes

def fib(n): #returns nth fibonacci number
    sqrf = np.sqrt(5)
    return (1/sqrf)((1 + sqrf)/2) ** n + (1/sqrf)((1 - sqrf)/2) ** n
