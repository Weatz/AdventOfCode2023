import re

digitWords = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def part1(str):
    firstDigit = None
    lastDigit = None
    for char in str:
        if(char.isdigit()):
            if(firstDigit == None):
                firstDigit = char
            lastDigit = char
    final = "" + firstDigit + lastDigit
    return int(final)

def part2(str):
    firstDigit = None
    lastDigit = None
    
    regex = re.compile(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', flags=re.I | re.X)
    regResult = regex.findall(str)
    print(regResult)
    if(regResult[0].isdigit()):
        firstDigit = regResult[0]
    else:
        firstDigit = digitWords[regResult[0]]

    if(regResult[len(regResult) - 1].isdigit()):
        lastDigit = regResult[len(regResult) - 1]
    else:
        lastDigit = digitWords[regResult[len(regResult) - 1]]

    
    final = "" + firstDigit + lastDigit
    return int(final)


f = open("Day1\\data1.txt", "r")
lines = f.readlines()
sum = 0

for line in lines:
    sum = sum + part2(line)

print(sum)





'''

'''