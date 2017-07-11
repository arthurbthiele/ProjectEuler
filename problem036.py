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

goodnums = []
for count in range (1, 10 ** 6):
    if ispalindrome(count) and ispalindrome(str(bin(count))[2:]):
        goodnums.append(count)
print goodnums
print sum(goodnums)
