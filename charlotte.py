fibs = [0, 0, 1]

for count in range  (1, 100):
    fibs.append(fibs[-1] + fibs[-2] + fibs[-3])

print fibs
