#this will find the circular primes below 1 000 000

from arthurtools import primes
primes = primes(10 ** 6)
circularprimes = []
circularno = 0

for count in range (0, len(primes)):
    circular = True
    num = primes[count]
    word = str(num)
    for i in range (0, len(word)):
        if not (int(word[i:] + word[:i]) in primes):
            circular = False
    if circular:
        circularno += 1
        circularprimes.append(num)
        print num
print circularno
print circularprimes
#this code literally finished in about 10 minutes but about 40 seconds in gave enough information for me to correctly determine the answer
#there are loads of simple optimisations which would improve this code, including:
#figure out how to add each permutation of the number when doing the first one, then skip the rest
#skip numbers that are permutations of earlier numbers which weren't circular
