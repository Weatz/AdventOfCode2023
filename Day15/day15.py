import re

def ParseInput(line):
    return line[0].split(",")

def Hash(step):
    result = 0
    for char in step:
        result = ((result + ord(char)) * 17) % 256
    return result

def Part1(line):
    sum = 0
    steps = ParseInput(line)
    for i, step in enumerate(steps):
        sum += Hash(step)
    print(sum)


def DoStep(step, boxes):
    split = [z for z in re.findall(r"([a-z]+)(=?-?)(\d?)", step)[0]]
    hash = Hash(split[0])
    lensLabel = [t[0] for t in boxes[hash]]
    if(split[1] == "="):
        if split[0] in lensLabel:
            boxes[hash][lensLabel.index(split[0])] = (split[0], int(split[2]))
        else:
            boxes[hash].append((split[0], int(split[2])))
    else:
        if split[0] in lensLabel:
            boxes[hash].pop(lensLabel.index(split[0]))
    print(split)

def Part2(line):
    boxes = [[] for i in range(256)]
    steps = ParseInput(line)
    for step in steps:
        DoStep(step, boxes)
    
    sum = 0
    for i, box in enumerate(boxes):
        for j, lens in enumerate(box):
            sum += (i + 1) * (j + 1) * lens[1]
    print(sum)

f = open("Day15/data15.txt", "r")
lines = f.readlines()
Part1(lines)
Part2(lines)