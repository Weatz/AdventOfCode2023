import re

def SplitData(lines):
    e = 0
    splittedData = [[]]
    for line in lines:
        if(line == "\n"):
            e += 1
            splittedData.append([])
        else:
            splittedData[e].append(line)
    return splittedData

def CreateConversion(group):
    conversionDict = {}
    for i in range(1, len(group)):
        values = [int(e) for e in re.findall(r"(\d+)", group[i])]
        conversionDict[(values[1], values[1] + values[2])] = values[0] - values[1]
    return conversionDict

def ApplyConversions(conversionDicts, seed):
    location = seed
    for conversionDict in conversionDicts:
        for conversionRange in conversionDict:
            if(conversionRange[0] <= location <= conversionRange[1]):
                location += conversionDict[conversionRange]
                break
            
    return location

def Part1(lines):
    splittedData = SplitData(lines)
    conversionDicts = []
    for i in range(1, len(splittedData)):
        conversionDicts.append(CreateConversion(splittedData[i]))
    
    splitSeeds = [int(e) for e in re.findall(r"(\d+)", splittedData[0][0])]
    locations = []
    for seed in splitSeeds:
        locations.append(ApplyConversions(conversionDicts, seed))
    
    print(min(locations))

f = open("Day5\\data5.txt", "r")
lines = f.readlines()
Part1(lines)