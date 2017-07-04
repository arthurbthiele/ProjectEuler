#problem 1: make a list of all sets of 3 numbers which sum to 1000

#gonna try with 10 first

#gonna try with 2 numbers summing to ten first cause im dumb
'''
metalist = [[]]
for a in range(1, 10):
    b = 10 - a
    metalist.append([a, b])

print metalist
'''
#so that worked, now time to try with 3 numbers! up to twenty at first again
'''
metalist = [[]]
for a in range (1, 19):
    for b in range (a + 1, 19 - a):
        c = 20 - a - b
        if c > b:
            metalist.append([a, b, c])

print metalist
'''
#yeah baby! now it's time to make sure that each triple is actually a pythagorean one!

for a in range (1, 999):
    for b in range (a + 1, 999 - a):
        c = 1000 - a - b
        if (a**2 + b**2 == c**2) and (c > b):
            print a, b, c
            print a*b*c
#sweet!
