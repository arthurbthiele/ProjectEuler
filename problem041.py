permutations = []

def perms(sofar, listof):
    if len(listof) == 1:
        permutations.append(sofar + str(listof[0]))
        print sofar + str(listof[0])
    else:
        for count in range(0, len(listof)):
            newlist = list(listof)
            del newlist[count]
            perms(sofar + str(listof[count]), newlist)
perms('', [4, 3, 2, 1])
print permutations
