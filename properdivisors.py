#this should return the proper divisors of any integer n in the form of a list, not including the number itself
import numpy as np
n = 200 #this is the number for which we want the proper divisors

divisors = [1]

for count in range (2, int(np.floor(np.sqrt(n)) + 1)):
    if n % count == 0:
        divisors += [count, n/count]

print divisors
