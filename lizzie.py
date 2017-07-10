factors = []
print "A"
number = 600851475143
print "B"
count = 2
while number != 1:
    while number % count == 0:
        print count
        factors.append(count)
        number /= count
    count = count + 1
print "C"
print factors
