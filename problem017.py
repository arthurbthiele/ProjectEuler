#this counts the length of a string, but doesn't include the whitespaces
#I'm going to then write a function that prints a word in letters with whitespace, and then use this to count its length in letters
units = {"0": "", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine",}
teens = {"0": "ten", "1": "eleven", "2": "twelve", "3": "thirteen", "4": "fourteen", "5": "fifteen", "6": "sixteen", "7": "seventeen", "8": "eighteen", "9": "nineteen",}
tens = {"0": "", "1": "ten", "2": "twenty", "3": "thirty", "4": "forty", "5": "fifty", "6": "sixty", "7": "seventy", "8": "eighty", "9": "ninety",}


def lengthCounter(input):
    if input == "":
        return 0
    if input[0] == " ":
        return lengthCounter(input[1:])
    else:
        return lengthCounter(input[1:]) + 1

#print lengthCounter('apples')
#print lengthCounter('oranges')
#print lengthCounter('apples and oranges')
#here, number is the input number, word is that number as a string and build is the number written out so far
def numberWriter(number):
    word = str(number)
    if number < 100:
        word = "0" + word
    if number < 10:
        word = "0" + word
    if number == 1000:
        return "one thousand"
    build = ""
    if number >= 100:
        build += units[word[0]]
        if number % 100 != 0:
            build += " hundred and "
        else:
            build += " hundred"
            return build
    if word[1] == "0":
        build += units[word[2]]
        return build
    if word[1] == "1":
        build += teens[word[2]]
        return build
    build += tens[word[1]] + " "
    build += units[word[2]]
    return build

sum = 0
for count in range (1, 1001):
    sum += lengthCounter(numberWriter(count))
print sum
#yay! Angus says to name functions more carefully:
#write them as things like "length" or "text form" respectively
