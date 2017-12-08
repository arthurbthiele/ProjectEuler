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


    primes = [2]
    for i in range(2, n):
        if isprime[i] == 1:
            primes.append(potentialprimes[i])
    return primes

def primecheck(n, allprimes): #takes an input of the primes up to the sqrt of the number to check
    limit = np.floor(np.sqrt(n))
    i = 0
    while allprimes[i] <= limit:
        if n % allprimes[i] == 0:
            return False
        i += 1
    return True


def fib(n): #returns nth fibonacci number
    sqrf = np.sqrt(5)
    return (1/sqrf)((1 + sqrf)/2) ** n + (1/sqrf)((1 - sqrf)/2) ** n

def perms(sofar, listof): #this adds all the permutations of some set to a already created list called listname
    if len(listof) == 1:
        listname.append(sofar + str(listof[0]))
        #print sofar + str(listof[0])
    else:
        for count in range(0, len(listof)):
            newlist = list(listof)
            del newlist[count]
            perms(sofar + str(listof[count]), newlist)
