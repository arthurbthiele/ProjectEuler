known = {}
coins = (1,2,5,10,20,50,100,200)

def numberofways(p):
    if p==0:
        return 0
    elif p == 1:
        return 1
    else:
        if p in known:
            return known[p]
        else:
            total = 0
            for i in coins:
                if i<=p:
                    newp = p-i
                    x = numberofways(newp)
                    p += x
                    known[newp] = x
            return total

print numberofways(5)
