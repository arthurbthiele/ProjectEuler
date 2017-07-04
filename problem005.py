import numpy as np

'''
for n in range(0, 100000000, 10):
    divisiblesofar = True
    for i in range(1, 21):
        if n % i != 0:
            divisiblesofar = False
    if divisiblesofar:
        print n
'''
#doesnt seem to work because the number is super huge!
#gonna try something with prime factors instead

def factorial(input):
    if input == 0 or input == 1:
        return 1
    return input * factorial (input - 1)

print factorial(10)
'''
Possible prime factors: 2, 3, 5, 7, 11, 13, 17, 19
We want our number to have enough of each to make up each number less than 20. Will try this in this way:
'''
         # 4  2  1  1  1   1   1   1
primes = [2, 3, 5, 7, 11, 13, 17, 19]
counts = [0]*8

for count in range(1, 21):
    num = count
    for i in primes:
#in the end solved by using the list of numbers above, and thinking about the required number of prime factors to make up any number less than 20        
