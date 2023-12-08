import re

def ParseInput(lines):
    nodeDict = {}
    sequence = lines[0]
    lines.pop(0)
    lines.pop(0)
    for line in lines:
        split = re.findall(r"(\w+)", line)
        nodeDict[split[0]] = (split[1], split[2])
    return sequence, nodeDict

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


f = open("Day8/data8.txt", "r")
lines = f.readlines()
Part1(lines)
