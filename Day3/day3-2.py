

def ComputeTable(lines):
    numbers = []
    table = []
    e = 0
    currentStringNumber = ""
    for i, line, in enumerate(lines):
        table.append([])
        for j, character in enumerate(line):
            if(character.isdigit()):
                table[i].append(str(e))
                currentStringNumber = currentStringNumber + character
            else:
                if(currentStringNumber != ""):
                    numbers.append(int(currentStringNumber))
                    currentStringNumber = ""
                    e += 1
                if(character != "\n"):
                    table[i].append(character)
    return table, numbers


def ComputeGears(table, numbers):
    sum = 0
    for i, line, in enumerate(table):
        for j, character in enumerate(line):
            if(character ==  "*"):
                connectedNumbers = []
                for di in range(i-1,i+2):
                    for dj in range(j-1, j+2):
                        if(table[di][dj].isdigit()):
                            if(table[di][dj] not in connectedNumbers):
                                connectedNumbers.append(table[di][dj])
                if(len(connectedNumbers) == 3):
                    print("------------------333333--------------------")
                if(len(connectedNumbers) == 2):
                    sum += numbers[int(connectedNumbers[0])] * numbers[int(connectedNumbers[1])]
    print(sum)




f = open("Day3\\buffer.txt", "r")
lines = f.readlines()

tab, num = ComputeTable(lines)
ComputeGears(tab, num)
