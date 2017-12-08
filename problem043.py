pandigitals = []

def perms(sofar, listof):
    if len(listof) == 1:
        pandigitals.append(sofar + str(listof[0]))
        #print sofar + str(listof[0])
    else:
        for count in range(0, len(listof)):
            newlist = list(listof)
            del newlist[count]
            perms(sofar + str(listof[count]), newlist)
perms('', [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

weirdnums = []

for p in pandigitals:
    if int(p[1:4]) % 2 == 0:
        if int(p[2:5]) % 3 == 0:
            if int(p[3:6]) % 5 == 0:
                if int(p[4:7]) % 7 == 0:
                    if int(p[5:8]) % 11 == 0:
                        if int(p[6:9]) % 13 == 0:
                            if int(p[7:10]) % 17 == 0:
                                weirdnums.append(int(p))
print weirdnums
print sum(weirdnums)
