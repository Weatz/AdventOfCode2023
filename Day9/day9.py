import re

def ParseData(lines):
    data = []
    for line in lines:
        data.append([int(e) for e in re.findall(r"(-?\d+)", line)])
    return data

def FindAllZero(tab):
    computedTab = [tab]
    level = 0
    while(max(computedTab[level]) != 0 or min(computedTab[level]) != 0):
        newLevel = []
        for i in range(1, len(computedTab[level])):
            newLevel.append(computedTab[level][i] - computedTab[level][i - 1])
        computedTab.append(newLevel)
        level += 1
    return computedTab

# len(allZeroTab-2)
def ExtrapolateAfter(allZeroTab):
    allZeroTab[-1].append(0)
    for i in reversed(range(len(allZeroTab[0:-1]))):
        prediction = allZeroTab[i][-1] + allZeroTab[i+1][-1]
        allZeroTab[i].append(prediction)
    return prediction

def ExtrapolateBefore(allZeroTab):
    allZeroTab[-1].insert(0, 0)
    for i in reversed(range(len(allZeroTab[0:-1]))):
        prediction = allZeroTab[i][0] - allZeroTab[i+1][0]
        allZeroTab[i].insert(0, prediction)
    return prediction

def Part1(lines):
    data = ParseData(lines)
    sum = 0
    for tab in data:
        allZero = FindAllZero(tab)
        sum += ExtrapolateAfter(allZero)
    print(sum)

def Part2(lines):
    data = ParseData(lines)
    sum = 0
    for tab in data:
        allZero = FindAllZero(tab)
        sum += ExtrapolateBefore(allZero)
    print(sum)

f = open("Day9/data9.txt", "r")
lines = f.readlines()
Part1(lines)
Part2(lines)