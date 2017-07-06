from arthurtools import divisors

def abundant(n): #returns all abundant numbers less than n
    abundants = []
    for count in range (12, n):
        if sum(divisors(count)) > count:
            abundants.append(count)
    return abundants
abundants = abundant(28123)
print abundants

#this list of booleans will be set to 0 if they can be made as the sum of two abundant numbers
bools = [1]*28124
for i in range (0, len(abundants)):
    for j in range (0, len(abundants) - i):
        if abundants[i] + abundants[j] < len(bools):
            bools[abundants[i] + abundants[j]] = 0

deficients = []
for count in range (0, len(bools)):
    if bools[count] == 1:
        deficients.append(count)

print sum(deficients)
