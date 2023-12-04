import re

nbRed = 12
nbGreen = 13
nbBlue = 14


# 2679
def part1(l):

    extractGameID = re.compile(r"Game (\d+):")
    gameID = extractGameID.findall(l)
    
    extractRed = re.findall(r"(\d+) red", l)
    extractBlue = re.findall(r"(\d+) blue", l)
    extractGreen = re.findall(r"(\d+) green", l)

    if(extractRed != []):
        redBalls = [int(e) for e in extractRed]
        if(max(redBalls) > nbRed):
            return 0
    
    if(extractBlue != []):
        blueBalls = [int(e) for e in extractBlue]
        if(max(blueBalls) > nbBlue):
            return 0
            
    if(extractGreen != []):
        greenBalls = [int(e) for e in extractGreen]
        if(max(greenBalls) > nbGreen):
            return 0
            
    return gameID[0]



def maxBalls(strTab):
    if(strTab != []):
        balls = [int(e) for e in strTab]
        return max(balls)

def part2(l):
    extractGameID = re.compile(r"Game (\d+):")
    gameID = extractGameID.findall(l)
    
    extractRed = re.findall(r"(\d+) red", l)
    extractBlue = re.findall(r"(\d+) blue", l)
    extractGreen = re.findall(r"(\d+) green", l)
    return maxBalls(extractRed) * maxBalls(extractBlue) * maxBalls(extractGreen)


f = open("Day2/data2.txt", "r")
lines = f.readlines()
sum = 0
sum2 = 0

for line in lines:
    sum += int(part1(line))
    sum2 += part2(line)

print("part 1 : ", sum)
print("part 2 : ", sum2)