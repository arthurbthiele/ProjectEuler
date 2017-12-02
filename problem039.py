#we need to find loads of pythagorean triads. so:
perimeters = [0]*1000
pythags = [[]]
for c in range(1, 1000):
    for b in range(1, 1000 - c):
        for a in range(1, 1000 - b - c):
            if a**2 + b**2 == c**2:
                pythags.append([a, b, c])
                perimeters[a+b+c] += 1


print perimeters.index(max(perimeters))
