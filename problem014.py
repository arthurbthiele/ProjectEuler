'''
10 5 16 8 4 2 1
11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
3 10 5 16 8 4 2 1 = 7

'''
#Collatz sequences!
top = 1000000
colls = [0]*top
colls[1] = 1
def next(input):
    if input % 2 ==0:
        return input/2
    else:
        return 3*input + 1


def collatzlength(input):
    length = 0
    a = input
    while a != 1:
        length += 1
        a = next(a)
    return length

for count in range (1, 1000000):
    if count % 100 == 0:
        print count
    colls.append(collatzlength(count))

print colls.index(max(colls)) + 1

'''
#worked, but can be optimised massively
for count in range (1, top):
    if colls[count] == 0: #then this number hasn't been done yet
        path = [count]
        nexted = next(path[-1])
        while True:
            if nexted < top:
                if colls[nexted] != 0:
                    break
            path.append(nexted)
            nexted = next(path[-1])
        totlength = len(path) + colls[nexted]
        for num in range (0, len(path)):
            if path[num] < top:
                if colls[path[num]] == 0:
                    colls[path[num]] = totlength - num
print colls.index(max(colls))
#angus helped out on bugfixing for this one, and gave me the idea for the optimisation, and then did the troubleshooting. still a good effort on the optimisation
'''
