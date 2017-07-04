sum = 0
a = 0
b = 1  #first two fibonacci numbers
c = 1
while c < 4000000:
    c = a + b
    a = b
    b = c #reassigns a and b to be the newest two terms in the sequence, in order of size
    if c%2 == 0:
        sum += c
    if b < 100:
        print a, b
print
print
print
print sum
