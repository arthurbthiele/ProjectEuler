#this counts the length of a string, but doesn't include the whitespaces
#I'm going to then write a function that prints a word in letters with whitespace, and then use this to count its length in letters
dict1 = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}

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
    if number == "1000":
        return "one thousand"
    build = ""
    if number >= 100:
        build += dict1[number[0]]
    
