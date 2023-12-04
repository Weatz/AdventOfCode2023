ignoreSymbols = [str(e) for e in range(0,10)]
ignoreSymbols.append(".")
ignoreSymbols.append("\n")


def createNeigbourMap(lines):
    correctCorrds = []
    for i, line, in enumerate(lines):
        for j, character in enumerate(line):
            if(character not in ignoreSymbols):
                for di in range(i-1,i+2):
                    for dj in range(j-1, j+2):
                        #correctCorrds[di,dj] = 1
                        correctCorrds.append((di,dj))
    return correctCorrds


def part1(lines):
    sum = 0
    coords = createNeigbourMap(lines)
    count = False
    currentStringNumber = ""
    for i, line, in enumerate(lines):
        if(currentStringNumber != ""):
            if not count:
                currentStringNumber = ""
            else:
                sum += int(currentStringNumber)
                currentStringNumber = ""
                count = False
        for j, character in enumerate(line):
            if(character.isdigit()):
                currentStringNumber = currentStringNumber + character
                if((i,j) in coords):
                    count = True
            else:
                if(currentStringNumber != ""):
                    if not count:
                        currentStringNumber = ""
                    else:
                        sum += int(currentStringNumber)
                        currentStringNumber = ""
                        count = False
    return sum


f = open("C:\\Users\\jeand\\Documents\\AdventOfCode2023\\Day3\\data3.txt", "r")
lines = f.readlines()

print(part1(lines))