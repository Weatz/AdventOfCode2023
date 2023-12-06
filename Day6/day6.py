import re
import math

def ParseInput(lines):
    times = [int(e) for e in re.findall(r"(\d+)", lines[0])]
    distances = [int(e) for e in re.findall(r"(\d+)", lines[1])]
    races = []
    for i in range(len(times)):
        races.append((times[i], distances[i]))

    return races

#time : 7 dist : 9
# d = time * time - 4 * dist
# y1 = (n - sqrt(d)) / 2
# y2 = (n + sqrt(d) / 2)

def CalculateWinningsWays(race):
    delta = race[0] * race[0] - 4 * race[1]
    y1 = (race[0] - math.sqrt(delta)) / 2
    y2 = (race[0] + math.sqrt(delta)) / 2
    loosing1 = math.floor(y1) + 1
    loosing2 = race[0] - math.ceil(y2) + 1
    return race[0] - loosing1 - loosing2 + 1

def Part1(lines):
    prod = 1
    races = ParseInput(lines)
    for race in races:
        prod *= CalculateWinningsWays(race)
    print(prod)
    

f = open("Day6/data6.txt", "r")
lines = f.readlines()
Part1(lines)