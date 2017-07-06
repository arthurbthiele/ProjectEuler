fibs = [0, 1]

while len(str(fibs[-1])) < 1000:
    fibs.append(fibs[-1] + fibs[-2])
print fibs[-1]
print len(fibs)
