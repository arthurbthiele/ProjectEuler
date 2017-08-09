#this problem is to determine the number of ways to make up 200p with different coins
import time
t = time.time()
numberofways = 0
#adding in variables because Allen wanted to
p = 200
for twopounds in range (0, p/200):
    for pound in range (0, (p - 200 * twopounds)/100 + 1):
        for fiftypence in range (0, (p - 200 * twopounds - 100 * pound)/50 + 1):
            for twentypence in range (0, (p - 200 * twopounds - 100 * pound - 50 * fiftypence)/20 + 1):
                for tenpence in range (0, (p - 200 * twopounds - 100 * pound - 50 * fiftypence - 20 * twentypence)/10 + 1):
                    for fivepence in range (0, (p - 200 * twopounds - 100 * pound - 50 * fiftypence - 20 * twentypence - 10 * tenpence)/5 + 1):
                        for tuppence in range (0, (p - 200 * twopounds - 100 * pound - 50 * fiftypence - 20 * twentypence - 10 * tenpence - 5 * fivepence)/2 + 1):
                            #the rest gets made up by pennies, so each point we've reached here is a way to make 2 pounds
                            numberofways += 1
                            if numberofways % 1000 == 0:
                                print numberofways

print numberofways
print time.time() - t
#this is probably the solution of which I am most proud (n < 38)
#500: 1.55 seconds with 6290871 possibilities ~= 6e5
#1000: 80 seconds with 321335885 possibilities ~= 3e8
#1200: 244 seconds with 967084976 possibilities ~= 9e8
#1300: 352 seconds with 1580547345 possibilities ~= 1.5e9
#excel graph time while the 1400 graph runs
#1400: 574 seconds with 2500342871 possibilities ~= 2.5e9
