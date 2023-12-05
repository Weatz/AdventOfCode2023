import re

def CheckIfWon(line):
    nbMatchingNumbers = 0
    data = line.split(":")[1]
    winningNumbersStr, cardNumbersStr = data.split("|")


    extractNumbers = re.compile(r"\d+")
    winningNumbers = extractNumbers.findall(winningNumbersStr)
    cardNumbers = extractNumbers.findall(cardNumbersStr)

    for number in cardNumbers:
        if(number in winningNumbers):
            nbMatchingNumbers += 1
    
    return nbMatchingNumbers

def Part1(lines):
    sum = 0
    for line in lines:
        winningNumbers = CheckIfWon(line)
        sum += pow(2, winningNumbers - 1) if winningNumbers > 0 else 0
    print(sum)


def Part2(lines):
    sum = 0
    listOfCards = {}
    for i, line in enumerate(lines):
        winningNumbers = CheckIfWon(line)

        nbOfCard = 1
        if(i in listOfCards):
            nbOfCard += listOfCards[i]

        if(winningNumbers > 0):
            for e in range (0, winningNumbers):
                if(i+e+1 in listOfCards):
                    listOfCards[i+e+1] = listOfCards[i+e+1] + nbOfCard
                else:
                    listOfCards[i+e+1] = nbOfCard
        
        sum += nbOfCard

    print(sum)


f = open("Day4\\data4.txt", "r")
lines = f.readlines()
Part2(lines)
