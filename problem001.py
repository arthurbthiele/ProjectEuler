sum = 0 #sum so far of numbers that are multiples of 3 or 5
for counter in range (1, 1000):
    if counter % 3 == 0 or counter % 5 == 0: #asks if the number is divisible by 3 or 5
        sum = sum + counter

print sum
