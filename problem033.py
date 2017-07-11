#this program will find the non-trivial fractions that can be 'incorrectly cancelled' to give their actual result
#fractions will be of form j/i, where both i and j are two digit numbers
product = float(1)
for i in range (10, 100):
    for j in range (10, i):
        if str(i)[1] != "0":
            if str(i)[0] == str(j)[1] and float(j)/float(i) == float(str(j)[0])/float(str(i)[1]):
                print i, j
                product *= float(j)/float(i)
print product 
