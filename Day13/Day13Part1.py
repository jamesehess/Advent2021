# -----------------------
#   Advent of Code 2021
#   Day 13 Part 1
#   Author: James Hess
# -----------------------

dotList = []
foldList = []

# Parse puzzle input file and store necessary data in list
with open("Day13Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        if 'fold' in line:
            foldList.append(line.strip().strip('fold along ').split('='))
        elif line != '\n':
            tempDot = line.strip().split(',')
            tempDot = [int(i) for i in tempDot]
            dotList.append(tempDot)

print(dotList)
dotDiagram = []

def getMaxX(dotList):
    currentMax = 0
    for dot in dotList:
        if dot[0] > currentMax:
            currentMax = dot[0]
    return currentMax

def getMaxY(dotList):
    currentMax = 0
    for dot in dotList:
        if dot[1] > currentMax:
            currentMax = dot[1]
    return currentMax

maxX = getMaxX(dotList)
maxY = getMaxY(dotList)

def printDiagram(maxX,maxY,dotList):
    # Initialize the dot diagram
    dotDiagram = []
    for line in range(maxY + 1):
        tempLine = []
        for dot in range(maxX + 1):
            tempLine.append(0)
        dotDiagram.append(tempLine)

    # Add dots from input to diagram
    for dot in dotList:
        dotDiagram[dot[1]][dot[0]] = 1

    # Print initial dot diagram
    #for line in dotDiagram:
    #    for item in line:
    #        print(item, end='')
    #    print('')

    # Return dotDiagram
    return dotDiagram

printDiagram(maxX,maxY,dotList)

# First fold
fold = foldList[0]
# Horizontal fold line
newDotList = []
if fold[0] == 'y':
    for dot in dotList:
        # If dot is below the fold
        if dot[1] > int(fold[1]):
            # Move dot above fold
            tempDot = [dot[0],abs(dot[1]-maxY)]
            newDotList.append(tempDot)
        else:
            newDotList.append(dot)
    # Delete below the fold (include line)
    maxY = int(fold[1])-1
# Vertical fold line
elif fold[0] == 'x':
    for dot in dotList:
        # If dot is to the right of fold
        if dot[0] > int(fold[1]):
            # Move dot to the left of fold
            tempDot = [abs(dot[0]-maxX),dot[1]]
            newDotList.append(tempDot)
        else:
            newDotList.append(dot)
print(newDotList)

dotDiagram = printDiagram(maxX,maxY,newDotList)

# Count dots on diagram
count = 0
for line in dotDiagram:
    for item in line:
        count += item
print("Dot Count: "+str(count))