from arthurtools import primes

primes = primes(10 ** 6) + [2]
truncatable = []
for count in range (4, len(primes)):
    num = primes[count]
    word = str(num)
    trunc = True
    for i in range (1, len(word)):
        if not (int(word[i:]) in primes and int(word[:i]) in primes):
            trunc = False
    if trunc:
        truncatable.append(num)
        print
        print num
        print
    if count % 100 == 0:
        print num
    if len(truncatable) == 11:
        break
print sum(truncatable)
#so this took a *very* long time to run, almost 10 minutes. It *did* run though, so that's nice
