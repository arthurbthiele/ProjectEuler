#gonna write one list of the number day that it is on any given day after 1st Jan 1900
import numpy as np

days = []


for year in range (1901, 2001):
    for month in range (1, 13):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            days += range(1, 32)
        if month in [4, 6, 9, 11]:
            days += range (1, 31)
        if month == 2:
            if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
                days += range (1, 30)
            else:
                days += range (1, 29)


count = 0

for i in range (0, len(days)):
    if i % 7 == 0 and days[i] == 1:
        count += 1

print count
