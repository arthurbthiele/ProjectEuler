#pentagonal numbers

pents = []

maxnum = 10000

for n in range(1, maxnum):
    pents.append(n*(3*n - 1)/2)
print pents

listofpairs = []
differences = []
for j in range(0, maxnum - 1):
    for k in range(0, maxnum - 1 - j):
        if pents[j] + pents[k] in pents:
            if abs(pents[j] - pents[k]) in pents:
                diff = pents[j] - pents[k]
                #listofpairs.append([[pents[j], pents[k]])
                differences.append(diff)
print min(differences)
