import re

def ParseInput(lines):
    l = lines
    nodeDict = {}
    sequence = l[0]
    l.pop(0)
    l.pop(0)
    for line in l:
        split = re.findall(r"(\w+)", line)
        nodeDict[split[0]] = (split[1], split[2])
    return sequence, nodeDict


def ParseInput2(lines):
    print(len(lines))
    l = lines
    nodeDict = {}
    sequence = lines[0]
    startingNodes = []
    finishNodes = []
    l.pop(0)
    l.pop(0)
    for line in l:
        split = re.findall(r"(\w+)", line)
        nodeDict[split[0]] = (split[1], split[2])
        if(split[0][2] == "A"):
            startingNodes.append(split[0])
        elif(split[0][2] == "Z"):
            finishNodes.append("Z")
    return sequence, nodeDict, startingNodes, finishNodes



def ConvertSeq(sequence):
    convertedSeq = []
    for char in sequence:
        if(char == "R"):
            convertedSeq.append(1)
        elif(char == "L"):
            convertedSeq.append(0)
    return convertedSeq

def Part1(lines):
    seq, nodeDict = ParseInput(lines)
    convertedSeq = ConvertSeq(seq)
    e = 0
    currentNode = "AAA"
    while (currentNode != "ZZZ"):
        currentNode = (nodeDict[currentNode])[convertedSeq[e % len(convertedSeq)]]
        e += 1
    print(e)

def Part2(lines):
    seq, nodeDict, startingNodes, finishNodes = ParseInput2(lines)
    convertedSeq = ConvertSeq(seq)
    stepsToFinish = []
    prod = len(convertedSeq)
    print(startingNodes)
    for start in startingNodes:
        e = 0
        currentNode = start
        print(currentNode)
        while (currentNode[2] != "Z"):
            currentNode = (nodeDict[currentNode])[convertedSeq[e % len(convertedSeq)]]
            e += 1
        prod *= e / len(convertedSeq) 
    print(prod)



f = open("Day8/data8.txt", "r")
lines = f.readlines()
#Part1(lines)
print("-----")
Part2(lines)