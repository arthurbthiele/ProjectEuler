#this program should add the diagonals of a spiral! that's pretty cool!


rednums = [1]

for count in range (1, 501):
    rednums += [rednums[-1] + 2 * count, rednums[-1] + 4 * count, rednums[-1] + 6 * count, rednums[-1] + 8 * count, ]

print rednums
print sum(rednums)
