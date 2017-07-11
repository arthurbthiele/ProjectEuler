#this problem is to determine the number of ways to make up 200p with different coins
import time
t = time.time()
numberofways = 0

for twopounds in range (0, 2):
    for pound in range (0, (200 - 200 * twopounds)/100 + 1):
        for fiftypence in range (0, (200 - 200 * twopounds - 100 * pound)/50 + 1):
            for twentypence in range (0, (200 - 200 * twopounds - 100 * pound - 50 * fiftypence)/20 + 1):
                for tenpence in range (0, (200 - 200 * twopounds - 100 * pound - 50 * fiftypence - 20 * twentypence)/10 + 1):
                    for fivepence in range (0, (200 - 200 * twopounds - 100 * pound - 50 * fiftypence - 20 * twentypence - 10 * tenpence)/5 + 1):
                        for tuppence in range (0, (200 - 200 * twopounds - 100 * pound - 50 * fiftypence - 20 * twentypence - 10 * tenpence - 5 * fivepence)/2 + 1):
                            #the rest gets made up by pennies, so each point we've reached here is a way to make 2 pounds
                            numberofways += 1

print numberofways
print time.time() - t
#this is probably the solution of which I am most proud (n < 38)
