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
        conversionDict[(values[1], values[1] + values[2] - 1)] = values[0] - values[1]
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

def ApplyConversionOnOneRange(interval, conversionDict):
    for conversionRange in conversionDict:
        if(conversionRange[0] <= interval[0] and conversionRange[1] >= interval[1]):
            return [(interval[0] + conversionDict[conversionRange],interval[1] + conversionDict[conversionRange])]
        elif(conversionRange[0] > interval[0] and conversionRange[0] <= interval[1] <= conversionRange[1]):
            return [(conversionRange[0] + conversionDict[conversionRange],interval[1] + conversionDict[conversionRange])] + ApplyConversionOnOneRange((interval[0], conversionRange[0] - 1), conversionDict)
        elif(conversionRange[0] <= interval[0] <= conversionRange[1] and conversionRange[1] < interval[1]):
            return [(interval[0] + conversionDict[conversionRange],conversionRange[1] + conversionDict[conversionRange])] + ApplyConversionOnOneRange((conversionRange[1] + 1, interval[1]), conversionDict)
        elif(conversionRange[0] > interval[0] and conversionRange[1] < interval[1]):
            return [(conversionRange[0] + conversionDict[conversionRange],conversionRange[1] + conversionDict[conversionRange])] + ApplyConversionOnOneRange((interval[0], conversionRange[0] - 1), conversionDict) + ApplyConversionOnOneRange((conversionRange[0] + 1, interval[1]), conversionDict)
    return [interval]

def ApplyRangeConversions(seedRange, conversionDicts):
    intervals = [seedRange]
    for conversionDict in conversionDicts:
        #print("interval state : ", intervals)
        tmpResultRanges = []
        for interval in intervals:
            tmpResultRanges = tmpResultRanges + ApplyConversionOnOneRange(interval, conversionDict)
        intervals = tmpResultRanges
    return intervals


def Part2(lines):
    splittedData = SplitData(lines)
    conversionDicts = []
    for i in range(1, len(splittedData)):
        conversionDicts.append(CreateConversion(splittedData[i]))

    splitSeeds = [int(e) for e in re.findall(r"(\d+)", splittedData[0][0])]
    seedRanges = []
    for i in range(0, int(len(splitSeeds) / 2)):
        seedRanges.append((splitSeeds[2 * i], splitSeeds[2 * i] + splitSeeds[2*i +1] - 1))

    resultRanges = []
    for seedRange in seedRanges:
        resultRanges = resultRanges + ApplyRangeConversions(seedRange, conversionDicts)

    for resultRange in resultRanges:
        print(resultRange)
    mintuple = min(resultRanges)
    print("minLocation : " + str(mintuple[0]))


f = open("Day5\\data5.txt", "r")
lines = f.readlines()
Part2(lines)