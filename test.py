from arthurtools import primes
import time
t = time.time()
primes = primes(1000000)
expended = time.time() - t
print primes
print expended
