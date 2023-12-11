


def CreateMaze(lines):
    maze = {}
    startingPos = (0, 0)
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if(char == "|"):
                maze[(i, j)] = [(i - 1, j), (i + 1, j)]
            if(char == "-"):
                maze[(i, j)] = [(i, j - 1), (i, j + 1)]
            if(char == "L"):
                maze[(i, j)] = [(i - 1, j), (i, j + 1)]
            if(char == "J"):
                maze[(i, j)] = [(i - 1, j), (i, j - 1)]
            if(char == "7"):
                maze[(i, j)] = [(i, j - 1), (i + 1, j)]
            if(char == "F"):
                maze[(i, j)] = [(i, j + 1), (i + 1, j)]
            if(char == "S"):
                startingPos = (i, j)

    connectedToStart = []
    # Over
    nextToStart = (startingPos[0] - 1, startingPos[1])
    if nextToStart in maze:
        if startingPos in maze[nextToStart]:
            connectedToStart.append(nextToStart)

    #Under
    nextToStart = (startingPos[0] + 1, startingPos[1])
    if nextToStart in maze:
        if startingPos in maze[nextToStart]:
            connectedToStart.append(nextToStart)

    # Left
    nextToStart = (startingPos[0], startingPos[1] - 1)
    if nextToStart in maze:
        if startingPos in maze[nextToStart]:
            connectedToStart.append(nextToStart)

    # Right
    nextToStart = (startingPos[0], startingPos[1] + 1)
    if nextToStart in maze:
        if startingPos in maze[nextToStart]:
            connectedToStart.append(nextToStart)

    maze[startingPos] = connectedToStart
    return maze, startingPos


def ExploreMaze(maze, startingPos):
    e = 1 
    lastPos1 = startingPos
    lastPos2 = startingPos
    currentPos1 = maze[startingPos][0]
    currentPos2 = maze[startingPos][1]
    mainLoop = [startingPos, currentPos1, currentPos2]
    while(currentPos1 != currentPos2 and currentPos1 != lastPos2):
        if(lastPos1 == maze[currentPos1][0]):
            lastPos1 = currentPos1
            currentPos1 = maze[currentPos1][1]
        else:
            lastPos1 = currentPos1
            currentPos1 = maze[currentPos1][0]
        if(lastPos2 == maze[currentPos2][0]):
            lastPos2 = currentPos2
            currentPos2 = maze[currentPos2][1]
        else:
            lastPos2 = currentPos2
            currentPos2 = maze[currentPos2][0]
        mainLoop.append(currentPos1)
        mainLoop.append(currentPos2)
        e += 1
    print(e)
    return mainLoop
        

def SearchIntersections(lines, startingPos, maze, mainLoop, pos):
    nonVerticalWalls = ["-", ".", "F", "7"]
    width = len(lines[0])
    nextToStart = (startingPos[0] - 1, startingPos[1])
    if nextToStart in maze:
        if startingPos not in maze[nextToStart]:
            nonVerticalWalls.append("S")
    else:
        nonVerticalWalls.append("S")
        
    
    intersections = 0
    intersectionsTab = []
    for j in range(pos[1], width):
        if((pos[0], j) in mainLoop):
            if(lines[pos[0]][j] not in nonVerticalWalls):
                intersections += 1
                intersectionsTab.append([(pos[0], j), lines[pos[0]][j]])
    return (intersections % 2 == 1)

def SearchGround(lines):
    grounds = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if(char == "."):
                grounds.append((i, j))
    return grounds

def Part1(lines):
    maze, startingPos = CreateMaze(lines)
    ExploreMaze(maze, startingPos)

def Part2(lines):
    maze, startingPos = CreateMaze(lines)
    mainLoop = ExploreMaze(maze, startingPos)
    sum = 0
    internalGrounds = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if (i, j) not in mainLoop:
                if(SearchIntersections(lines, startingPos, maze, mainLoop, (i, j))):
                    sum += 1
                    internalGrounds.append((i, j))

    print(sum)
    print(internalGrounds)

f = open("Day10/data10.txt", "r")
lines = f.readlines()
Part1(lines)
Part2(lines)