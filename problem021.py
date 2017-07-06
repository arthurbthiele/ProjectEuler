from arthurtools import divisors

amicable = []
for count in range (1, 10000):
    if sum(divisors(sum(divisors(count)))) == count and sum(divisors(count)) != count:
        amicable.append(count)

print amicable
print sum(amicable)
