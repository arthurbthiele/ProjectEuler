def ispandig(n):
    a = str(n)
    b = sorted(a)
    c = ''.join(b)
    return c == '123456789'

def smallenuf(n):
    a = str(n)
    p = len(a)
    return p < 10

def uptothis(a, p): #returns the multiplication of a with each integer up to p, concatenated
    b = ''
    for count in range(1, p + 1):
        b = b + str(a*count)
    return int(b)

giantlist = []

for count in range(1, 10000):
    p = 2
    current = uptothis(count, p)
    while smallenuf(current):
        current = uptothis(count, p)
        if ispandig(current):
            giantlist.append(current)
        p = p + 1
print max(giantlist)
print giantlist

#gosh that was nice, got correct answer first time!
