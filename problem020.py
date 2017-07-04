def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)
word = str(factorial(100))
summ = 0
for count in range (0, len(word)):
    summ += int(word[count])
print summ
