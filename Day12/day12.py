import re

def ParseInput(lines):
    springSequence  = []
    for line in lines:
        seq = re.findall(r"(\d+)", line)
        springs = re.findall("(\D)", line.split(" ")[0])
        springSequence.append((springs, seq))
    return springSequence

def CleanSequence(sequences):
    groups = []
    for sequence in sequences:
        return 0


def Part1(lines):
    springSeq = ParseInput(lines)
    for seq in springSeq:
        print(seq)

f = open("Day12/data12Ex.txt", "r")
lines = f.readlines()
Part1(lines)