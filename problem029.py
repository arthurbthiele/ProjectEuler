#here, we're finding all distinct terms produced by a^b, with a and b between 2 and 100.
import time
t = time.time()
listofnums = []

for a in range (2, 101):
    for b in range (2, 101):
        listofnums.append(a ** b)

newlist = list(set(listofnums))

print len(newlist)
print time.time() - t
#that's gotta be a time record! finished that within  4 minutes! v. proud
#also that's a super fast algorithm, nice job Arthur!
