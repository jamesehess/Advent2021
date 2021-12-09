# -----------------------
#   Advent of Code 2021
#   Day 9 Part 1
#   Author: James Hess
# -----------------------

# Parse puzzle input file and store necessary data in list
heightList = []
with open("Day9Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        lineList = []
        line = line.strip()
        for item in line:
            lineList.append(int(item))
        heightList.append(lineList)

maxLine = len(heightList)
maxItem = len(heightList[0])
risks = []
for idxLine, line in enumerate(heightList):
    for idxItem, item in enumerate(line):
        lowPoint = True
        if idxItem != 0:
            if heightList[idxLine][idxItem-1] <= item:
                lowPoint = False
        if idxLine != 0:
            if heightList[idxLine-1][idxItem] <= item:
                lowPoint = False
        if idxItem != maxItem-1:
            if heightList[idxLine][idxItem+1] <= item:
                lowPoint = False
        if idxLine != maxLine-1:
            if heightList[idxLine+1][idxItem] <= item:
                lowPoint = False
        if lowPoint == True:
            risks.append(item+1)

print(sum(risks))
