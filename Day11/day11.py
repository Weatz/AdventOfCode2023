
def ParseData(lines):
    space = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "#":
                space.append((i, j))
    return space

def ExpandSpace(space, height, width, columns):
    getX = lambda a : a[0] 
    getY = lambda a : a[1] 
    emptyLines = set([int(e) for e in range(height)]).difference([int(getX(f)) for f in space])
    emptyRows = set([int(e) for e in range(width)]).difference([int(getY(f)) for f in space])

    incrementX = lambda v : (v[0] + columns - 1, v[1])
    incrementY = lambda v : (v[0], v[1] + columns - 1)
    for i in reversed(sorted(list(emptyLines))):
        space = [incrementX(v) if getX(v) > i else v for v in space]

    for j in reversed(sorted(list(emptyRows))):
        space = [incrementY(v) if getY(v) > j else v for v in space]
    
    return space

def ComputeDistances(space):
    sum = 0
    for i in range(len(space) - 1):
        for j in range(i + 1, len(space)):
            sum += abs(space[j][0] - space[i][0]) + abs(space[j][1] - space[i][1])
    return sum

def Part1(lines):
    height = len(lines)
    width = len(lines[0])
    space = ParseData(lines)
    expandedSpace = ExpandSpace(space, height, width, 1)
    print(ComputeDistances(expandedSpace))

def Part2(lines):
    height = len(lines)
    width = len(lines[0])
    space = ParseData(lines)
    print(space)
    expandedSpace = ExpandSpace(space, height, width, 1000000)
    print(expandedSpace)
    print(ComputeDistances(expandedSpace))


f = open("Day11/data11.txt", "r")
lines = f.readlines()
Part1(lines)
Part2(lines)