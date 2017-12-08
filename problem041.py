from arthurtools import primes
import numpy as np
permutations = []

def perms(sofar, listof):
    if len(listof) == 1:
        permutations.append(sofar + str(listof[0]))
        #print sofar + str(listof[0])
    else:
        for count in range(0, len(listof)):
            newlist = list(listof)
            del newlist[count]
            perms(sofar + str(listof[count]), newlist)
perms('', [7, 6, 5, 4, 3, 2, 1])

#time to write a prime checker!
#will need all primes up to sqrt (10 ** 10) = 10 ** 5

allprimes = primes(10 ** 5)

def primecheck(n, allprimes):
    limit = np.floor(np.sqrt(n))
    i = 0
    while allprimes[i] <= limit:
        if n % allprimes[i] == 0:
            return False
        i += 1
    return True

for count in range(0, len(permutations)):
    if primecheck(int(permutations[count]), allprimes):
        print permutations[count]
        break
