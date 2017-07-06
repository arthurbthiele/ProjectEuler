#this will generate the primes up to n using the sieve of Sundaram

n = 200 #generates all primes below this value

q = (n-2)/2 #this is the peak value of i and j for the sieve

eliminations = [1]*q
primes = []

for i in range (0, q + 1):
    for j in range (0, q + 1 - i):
        if (i + j + 2*i*j < q):
            eliminations[i + j + 2*i*j] = 0

for i in eliminations:
    if i == 1:
        primes.append(2*i + 1)

print primes
