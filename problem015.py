import numpy as np

def fact(n):
    if n == 0: #tfw you forget that recursive functions need a base case :()
        return 1
    return n*fact(n-1)

def combi(n, k):
    num = fact(n)/(fact(k)*fact(n-k))
    return num #tfw you forget a return statement

paths = 0
gridsize = 20
for i in range (0, gridsize + 1):
     paths += (combi(gridsize, i))**2
print paths

#I am so great, I am the greatest
