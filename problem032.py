#this problem is to find all pandigital products for digits 1 through 9
import numpy as np
def divisors(n):
    divisors = []
    for count in range (2, int(np.ceil(np.sqrt(n)))):
        if n % count == 0:
            divisors.append([count, n / count])
    return divisors

alldigits = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

pandigital = set([])

for count in xrange (1000, 10000):
    listofdivs = divisors(count)
    #digits = set([int(str(count)[0]), int(str(count)[1]), int(str(count)[2]), int(str(count)[3])])
    for i in range (0, len(listofdivs)):
        if len(str(listofdivs[i][0])) + len(str(listofdivs[i][1])) == 5:
            word = str(listofdivs[i][0]) + str(listofdivs[i][1])
            digits = set([int(str(count)[0]), int(str(count)[1]), int(str(count)[2]), int(str(count)[3])])
            for j in range (0, len(word)):
                digits.add(int(word[j]))
            if digits == alldigits:
                pandigital.add(count)
                print count, "=", listofdivs[i][0], "x", listofdivs[i][1]
print sum(pandigital)
