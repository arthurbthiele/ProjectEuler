#this finds all numbers that are equal to the sum of their factorials!
import time
import math
t = time.time()
'''
factorials = [1]
for count in range (2, 10):
    factorials.append(factorials[-1] * count)
print factorials
print factorials[9 - 1]
'''
specialnums = []
for count in range (3, 10000000):
    word = str(count)
    sum = 0
    for i in range (0, len(word)):
        sum += math.factorial(int(word[i]))
    if sum == count:
        specialnums.append(count)
print specialnums
print time.time() - t
#this is quite slow but got the job done in about a minute, will optimise later if necessary
