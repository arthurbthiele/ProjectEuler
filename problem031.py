#this problem is to determine the number of ways to make up 200p with different coins

numberofways = 0

for penny in range (0, 201):
    for hapenny in range (0, 101):
        for fivepence in range (0, 41):
            for tenpence in range (0, 21):
                for twentypence in range (0, 11):
                    for fiftypence in range (0, 5):
                        for pound in range (0, 3):
                            for twopounds in range (0, 2):
                                if penny + 2 * hapenny + 5 * fivepence + 10 * tenpence + 20 * twentypence + 50 * fiftypence + 100 * pound + 200 * twopounds == 200:
                                    numberofways += 1
print numberofways
