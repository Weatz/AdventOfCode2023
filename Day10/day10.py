


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
        

def SearchIntersections(lines, nonVerticalWalls, nonHorizontalWalls, mainLoop, pos):
    height = len(lines)
    width = len(lines[0])
    
    intersections = 0
    jMinus = 0
    jMax = 0
    iMinus = 0
    iMax = 0
    if(pos[1] < width / 2):
        jMinus = 0
        jMax = pos[1]
    else:
        jMinus = pos[1]
        jMax = width
    if(pos[0] < height / 2):
        iMinus = 0
        iMax = pos[0]
    else:
        iMinus = pos[0]
        iMax = height

    if(jMax - jMinus < iMax  - iMinus):
        for j in range(jMinus, jMax):
            if((pos[0], j) in mainLoop):
                if(lines[pos[0]][j] not in nonVerticalWalls):
                    intersections += 1
    else:
        for i in range(iMinus, iMax):
            if((i, pos[1]) in mainLoop):
                if(lines[i][pos[1]] not in nonHorizontalWalls):
                    intersections += 1

    return (intersections % 2 == 1)

def GetNonVerticalWalls(startingPos, maze):
    nonVerticalWalls = ["-", ".", "F", "7"]
    nextToStart = (startingPos[0] - 1, startingPos[1])
    if nextToStart in maze:
        if startingPos not in maze[nextToStart]:
            nonVerticalWalls.append("S")
    else:
        nonVerticalWalls.append("S")
    return nonVerticalWalls

def GetNonHorizontalWalls(startingPos, maze):
    nonHorizontalWalls = ["|", ".", "F", "L"]
    nextToStart = (startingPos[0], startingPos[1] + 1)
    if nextToStart in maze:
        if startingPos not in maze[nextToStart]:
            nonHorizontalWalls.append("S")
    else:
        nonHorizontalWalls.append("S")    
    return nonHorizontalWalls

def IsAdjacentTo(insideCases, outsideCases, pos):
    adjacentCases = [(pos[0] - 1, pos[1]), (pos[0] + 1, pos[1]), (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)]

    if(len(set(adjacentCases).intersection(insideCases))):
        return 1
    if(len(set(adjacentCases).intersection(outsideCases))):
        return 2
    return 0


def Part1(lines):
    maze, startingPos = CreateMaze(lines)
    ExploreMaze(maze, startingPos)

def Part2(lines):
    maze, startingPos = CreateMaze(lines)
    mainLoop = ExploreMaze(maze, startingPos)
    sum = 0

    nonVerticalWalls = GetNonVerticalWalls(startingPos, maze)
    nonHorizontalWalls = GetNonHorizontalWalls(startingPos, maze)
    
    insideCases = []
    outsideCases = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if (i, j) not in mainLoop:
                adjacent = IsAdjacentTo(insideCases, outsideCases, (i, j))
                if adjacent == 1: 
                    insideCases.append((i, j))
                    sum += 1
                elif adjacent == 2:
                    outsideCases.append((i, j))
                else:
                    if(SearchIntersections(lines, nonVerticalWalls, nonHorizontalWalls, mainLoop, (i, j))):
                        insideCases.append((i, j))
                        sum += 1
                    else:
                        outsideCases.append((i, j))

    print(sum)

f = open("Day10/data10.txt", "r")
lines = f.readlines()
Part1(lines)
Part2(lines) #269