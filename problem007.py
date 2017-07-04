primes = []
primes.append(2)
count = 1
counter = 3
while count < 10001:
    isprime = True
    for p in primes:
        if (counter % p == 0):
            isprime = False
    if isprime:
        primes.append(counter)
        count += 1
    counter += 1
    if count % 100 == 0:
        print count
print primes[10000]

#this is pretty slow, Angus is suggesting a cool prime sieve method which I should try out
