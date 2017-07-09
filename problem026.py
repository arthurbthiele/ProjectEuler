#should check the length of the recurrence cycle for any unital fraction
#trying to teach the computer long division should be fun and useful

maxlength = 0
maxnum = 1
for count in range (1, 1000):
    remainders = [1]
    done = False
    while not done:
        for i in range (len(remainders) - 1):
            if remainders[-1] == remainders[i]:
                length = len(remainders) - i - 1
                if length > maxlength:
                    maxlength = length
                    maxnum = count
                done = True
        remainders.append((remainders[-1]*10)%count)

print maxlength, maxnum
