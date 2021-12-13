# -----------------------
#   Advent of Code 2021
#   Day 11 Part 1
#   Author: James Hess
# -----------------------

# Parse puzzle input file and store necessary data in list
octoList = []
with open("Day11Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        tempList = []
        line = line.strip()
        for item in line:
            tempList.append(int(item))
        octoList.append(tempList)

class color:
   BLUE = '\033[94m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   END = '\033[0m'

maxLine = len(octoList)
maxItem = len(octoList[0])

flashCount = 0
steps = 100

def spread(idxLine,idxItem):
    #UP
    if idxLine != 0:
        octoList[idxLine-1][idxItem] += 1
        if octoList[idxLine-1][idxItem] == 10:
            spread(idxLine-1, idxItem)
    #DOWN
    if idxLine != maxLine-1:
        octoList[idxLine+1][idxItem] += 1
        if octoList[idxLine+1][idxItem] == 10:
            spread(idxLine+1, idxItem)
    #LEFT
    if idxItem != 0:
        octoList[idxLine][idxItem-1] += 1
        if octoList[idxLine][idxItem-1] == 10:
            spread(idxLine, idxItem-1)
    #RIGHT
    if idxItem != maxItem-1:
        octoList[idxLine][idxItem+1] += 1
        if octoList[idxLine][idxItem+1] == 10:
            spread(idxLine, idxItem+1)
    #UPLEFT
    if idxLine != 0 and idxItem != 0:
        octoList[idxLine-1][idxItem-1] += 1
        if octoList[idxLine-1][idxItem-1] == 10:
            spread(idxLine-1, idxItem-1)
    #UPRIGHT
    if idxLine != 0 and idxItem != maxItem-1:
        octoList[idxLine-1][idxItem+1] += 1
        if octoList[idxLine-1][idxItem+1] == 10:
            spread(idxLine-1, idxItem+1)
    #DOWNLEFT
    if idxLine != maxLine-1 and idxItem != 0:
        octoList[idxLine+1][idxItem-1] += 1
        if octoList[idxLine+1][idxItem-1] == 10:
            spread(idxLine+1, idxItem-1)
    #DOWNRIGHT
    if idxLine != maxLine-1 and idxItem != maxItem-1:
        octoList[idxLine+1][idxItem+1] += 1
        if octoList[idxLine+1][idxItem+1] == 10:
            spread(idxLine+1, idxItem+1)

for i in range(steps):
    for idxLine, line in enumerate(octoList):
        for idxItem, item in enumerate(line):
            item +=1
            octoList[idxLine][idxItem] = item
            if item == 10:
                spread(idxLine,idxItem)
    for idxLine, line in enumerate(octoList):
        for idxItem, item in enumerate(line):
            if item > 9:
                octoList[idxLine][idxItem] = 0
                flashCount +=1

    #print octoList
    print("Step: " + str(i+1))
    for line in octoList:
        for item in line:
            if item == 0:
                print(color.BLUE + str(item) + color.END,end='')
            else:
                print(str(item),end='')
        print('')
print("Flash Count: " + str(flashCount))