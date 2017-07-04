import numpy as np

def ispalindrome(input):
    word = str(input)
    if len(word) % 2 == 0:
        middle = len(word)/2
        firsthalf = word[:middle]
        secondhalf = word [middle:]
        if firsthalf == secondhalf[::-1]:
            return True
        else:
            return False
    else:
        middle = int(np.floor(len(word)/2))
        firsthalf = word[:middle]
        secondhalf = word[middle + 1:]
        if firsthalf == secondhalf[::-1]:
            return True
        else:
            return False
'''
while True:
    request = input("Which number do you think might be a palindrome? ")
    print ispalindrome(request)
    print
'''
maxint = 0
for i in range(1000, 100, -1):
    for j in range(1000, 100, -1):
        if ispalindrome(i * j):
            print i
            print j
            if (i * j) > maxint:
                maxint = i * j
            print maxint
#cause I'm lazy I didn't want to make i and j print for the appropriate maxint, so i had to comb through the entire printout. Not a great method, but it worked :) :) :) 
