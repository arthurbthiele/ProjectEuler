import numpy as np

#triangular numbers!

def tri(n):
    return n*(n+1)/2


'''
for finding if they can be square:
for count in range (1, 30000):
    a = tri(count)
    if np.sqrt(a) == np.floor(np.sqrt(a)):
        print a
'''

def divs(n):
    factors = 0
    sqrt = np.sqrt(n)
    for count in range (1, int(np.floor(sqrt) + 1)):
        if n % count == 0:
            factors += 2
    if sqrt == np.floor(sqrt):
        factors = factors - 1
    return factors
#for testing divs function
'''
for n in range (1, 20):
    print n, divs(n)
'''
'''
for count in range (1, 20000):
    if count % 20 == 0:
        print count, tri(count)
    if(divs(tri(count))) > 500:
        print count, tri(count)
        break
'''
print divs(76576500)

#it works! it's alive!
