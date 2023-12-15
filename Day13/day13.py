import re

def ParseInput(lines):
    tables = []
    currentTable = []
    for line in lines:
        if(line == "\n"):
            tables.append(currentTable)
            currentTable = []
        else:
            currentTable.append(line.split("\n")[0])
    tables.append(currentTable)
    return tables

def VerifySymetry(table, firstIndex, lastIndex):
    for i in range(int((lastIndex - firstIndex + 1) / 2)):
        if(table[firstIndex+i] != table[lastIndex - i]):
            return False
    return True

def FindHorzontalSymetry(table):
    print("FindSymetry")
    firstLine = table[0]
    lastLine = table[-1]

    for z in table:
        print(z)

    for i, line in enumerate(table):
        if(line == firstLine and i != 0):
            if((i + 1)% 2 != 1):
                print(i, 0)
                if(VerifySymetry(table, 0, i)):
                    # i = 15 
                    return int((i + 1) / 2)
        if(line == lastLine and i != len(table) -1):
            if((len(table) - i)%2 != 1):
                print(i, len(table) - 1)
                if(VerifySymetry(table, i, len(table) - 1)):
                    # i = 1 len(table) - 1 = 16  ==> 9
                    # 01234567 i = 4, len(table) = 8 ==> 6
                    # 4 + (8 - 4) / 2
                    return i + int((len(table) - i) / 2)
    return 0

def RotateTable(tab):
    newTab = []
    for j in range(len(tab[0])):
        newLine = ""
        for i in range(len(tab) -1, -1, -1):
            newLine = newLine + tab[i][j]
        newTab.append(newLine)

    return newTab

'''
123
456
789



369
258
147
'''

def FindAllSymetry(table):
    horizontal = FindHorzontalSymetry(table)
    print("horizontal", horizontal)
    rotatedTable = RotateTable(table)
    vertical = FindHorzontalSymetry(rotatedTable)
    print("vertical", vertical)
    return  100 * horizontal + vertical
    

def Part1(lines):
    sum = 0
    tables = ParseInput(lines)
    for table in tables:
        print("-----")
        sum += FindAllSymetry(table)
    print(sum)


f = open("Day13/data13.txt", "r")
lines = f.readlines()
Part1(lines)