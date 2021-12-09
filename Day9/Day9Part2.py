# -----------------------
#   Advent of Code 2021
#   Day 9 Part 2
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
            # Strip non-nine heights
            if int(item) == 9:
                lineList.append(-1)
            else:
                lineList.append(0)
        heightList.append(lineList)

maxLine = len(heightList)
maxItem = len(heightList[0])

# Recursive basin filling function
def fillBasin(basinNum,idxLine,idxItem):
    if idxItem != 0:
        if heightList[idxLine][idxItem-1] == 0:
            heightList[idxLine][idxItem-1] = basinNum
            fillBasin(basinNum,idxLine,idxItem-1)
    if idxLine != 0:
        if heightList[idxLine-1][idxItem] == 0:
            heightList[idxLine-1][idxItem] = basinNum
            fillBasin(basinNum,idxLine-1,idxItem)
    if idxItem != maxItem - 1:
        if heightList[idxLine][idxItem+1] == 0:
            heightList[idxLine][idxItem+1] = basinNum
            fillBasin(basinNum,idxLine,idxItem+1)
    if idxLine != maxLine - 1:
        if heightList[idxLine+1][idxItem] == 0:
            heightList[idxLine+1][idxItem] = basinNum
            fillBasin(basinNum,idxLine+1,idxItem)

basinCount = 0
for idxLine, line in enumerate(heightList):
    for idxItem, item in enumerate(line):
        if item == 0:
            basinCount += 1
            heightList[idxLine][idxItem] = basinCount
            fillBasin(basinCount,idxLine,idxItem)

# Print height map
#for line in heightList:
#    printLine = []
#    for item in line:
#        printLine.append(str(item))
#    print("".join(printLine))

# Initialize basin count list
basinSizes = []
for basin in range(0,basinCount+1):
    basinSizes.append(0)

# Count basin sizes
for line in heightList:
    for item in line:
        if item != -1:
            basinSizes[item] += 1

basinSizes.sort(reverse=True)

print(basinSizes[0]*basinSizes[1]*basinSizes[2])