triangles = set()
pentagons = set()
for count in range(1, 1000000):
	triangles.add(count * (count + 1)/2)
	pentagons.add(count * (3 * count - 1) / 2)
print(triangles & pentagons)	
#in python 3 because sets are a bit easier
