import time
import math
t = time.time()
s = 0
n = 10
while n < 10 ** 7:
	nlist = map(int, list(str(n)))
	digfactsum = 0
	for dig in nlist:
		digfactsum += math.factorial(dig)
	if n == digfactsum:
		s += n
		print n, s
	n += 1
print time.time() - t
# Turns out there are only two numbers this holds for. Could be interesting to think about how to prove there aren't more?
