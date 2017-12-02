bigstring = '0'
for count in range(1, 10 ** 6):
    bigstring += str(count)
print int(bigstring[1])*int(bigstring[10])*int(bigstring[100])*int(bigstring[1000])*int(bigstring[10000])*int(bigstring[100000])*int(bigstring[1000000])
