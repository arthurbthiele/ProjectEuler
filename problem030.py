#this program should find the sum of all numbers which can be expressed as the sum of their nth powers!


#first we can check 3 digit numbers to establish the pattern:
n = 5
nticnumbers = []

for count in range (100, 1000):
    if int(str(count)[0]) ** n + int(str(count)[1]) ** n + int(str(count)[2]) ** n == count:
        nticnumbers.append(count)

#now for the 4 digit numbers

for count in range (1000, 10000):
    if int(str(count)[0]) ** n + int(str(count)[1]) ** n + int(str(count)[2]) ** n + int(str(count)[3]) ** n == count:
        nticnumbers.append(count)

#now for 5 digit numbers:
for count in range (10000, 100000):
    if int(str(count)[0]) ** n + int(str(count)[1]) ** n + int(str(count)[2]) ** n + int(str(count)[3]) ** n + int(str(count)[4]) ** n == count:
        nticnumbers.append(count)
#and 6 digit numbers:

for count in range (100000, 1000000):
    if int(str(count)[0]) ** n + int(str(count)[1]) ** n + int(str(count)[2]) ** n + int(str(count)[3]) ** n + int(str(count)[4]) ** n + int(str(count)[5]) ** n== count:
        nticnumbers.append(count)


print sum(nticnumbers)
