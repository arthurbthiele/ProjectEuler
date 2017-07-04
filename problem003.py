import numpy as np
def isprime(input):
    if input == 0 or input == 1:
        return False
    for counter in range (2, int(np.floor(np.sqrt(input))) + 1):
        if input % counter == 0:
            return False
    return True
'''
while True:
    number = input("Which number would you like to check for prime-ness? \n")

    if isprime(number) == True:
        print "That number is prime"
    else:
        print "Fuck you"

for counter in range (101):
    if isprime(counter):
        print counter
'''
num = 600851475143
for counter in range (2, int(np.floor(np.sqrt(num)))):
    if num % counter == 0:
        print counter
        if isprime(counter):
            print "MAYBE THIS ONE"
        print num/counter
        if isprime(num/counter):
            print "THIS ONE"
        print
#none of the cofactors were prime, so the largest prime factor was the largest of the factors below sqrt(num) which also were prime
