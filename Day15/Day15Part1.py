# -----------------------
#   Advent of Code 2021
#   Day 15 Part 1
#   Author: James Hess
# -----------------------

import math

weightGrid = []
# Parse puzzle input file and store necessary data in list
with open("Day15Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        tempList = []
        for char in line.strip():
            tempList.append(int(char))
        weightGrid.append(tempList)

maxY = len(weightGrid)
maxX = len(weightGrid[0])

# Initialize a distance grid
distanceGrid = []
for i in range(0,maxX):
    tempLine = []
    for j in range(0,maxY):
        tempLine.append(math.inf)
    distanceGrid.append(tempLine)

# Initialize a path grid
pathGrid = []
for i in range(0,maxX):
    tempLine = []
    for j in range(0,maxY):
        tempLine.append([-1,-1])
    pathGrid.append(tempLine)

def printGrid(grid):
    for line in grid:
        for char in line:
            print(char,end='')
        print('')

START = (0, 0)
FINISH = (maxX-1, maxY-1)

# Initialize the start
distanceGrid[START[0]][START[1]] = 0
LastNode = [START[0],START[1]]

printGrid(weightGrid)


# Loop until a path is determined for the FINISH node
while pathGrid[FINISH[0]][FINISH[1]] == [-1,-1]:

    # Identify the shortest distance node aka the next node to evaluate
    minDisLine = min(distanceGrid, key=min)
    minDisValue = min(minDisLine)
    minDisY = distanceGrid.index(minDisLine)
    minDisX = distanceGrid[minDisY].index(minDisValue)
    CurrentNode = [minDisY,minDisX]

    # Update pathGrid to mark CurrentNode with its shortest path back to start
    pathGrid[CurrentNode[0]][CurrentNode[1]] = LastNode

    #RIGHT
    EvalNode = [CurrentNode[0],CurrentNode[1]+1]
    if EvalNode[1] < maxX and pathGrid[EvalNode[0]][EvalNode[1]] == [-1, -1]:
        newDistance = distanceGrid[CurrentNode[0]][CurrentNode[1]] + weightGrid[EvalNode[0]][EvalNode[1]]
        if newDistance < distanceGrid[EvalNode[0]][EvalNode[1]]:
            distanceGrid[EvalNode[0]][EvalNode[1]] = newDistance
    #DOWN
    EvalNode = [CurrentNode[0]+1,CurrentNode[1]]
    if EvalNode[0] < maxY and pathGrid[EvalNode[0]][EvalNode[1]] == [-1, -1]:
        newDistance = distanceGrid[CurrentNode[0]][CurrentNode[1]] + weightGrid[EvalNode[0]][EvalNode[1]]
        if newDistance < distanceGrid[EvalNode[0]][EvalNode[1]]:
            distanceGrid[EvalNode[0]][EvalNode[1]] = newDistance
    #LEFT
    EvalNode = [CurrentNode[0],CurrentNode[1]-1]
    if EvalNode[1] >= 0 and pathGrid[EvalNode[0]][EvalNode[1]] == [-1, -1]:
        newDistance = distanceGrid[CurrentNode[0]][CurrentNode[1]] + weightGrid[EvalNode[0]][EvalNode[1]]
        if newDistance < distanceGrid[EvalNode[0]][EvalNode[1]]:
            distanceGrid[EvalNode[0]][EvalNode[1]] = newDistance
    #UP
    EvalNode = [CurrentNode[0]-1,CurrentNode[1]]
    if EvalNode[0] >= 0 and pathGrid[EvalNode[0]][EvalNode[1]] == [-1, -1]:
        newDistance = distanceGrid[CurrentNode[0]][CurrentNode[1]] + weightGrid[EvalNode[0]][EvalNode[1]]
        if newDistance < distanceGrid[EvalNode[0]][EvalNode[1]]:
            distanceGrid[EvalNode[0]][EvalNode[1]] = newDistance

    lastDistance = distanceGrid[CurrentNode[0]][CurrentNode[1]]
    distanceGrid[CurrentNode[0]][CurrentNode[1]] = math.inf
    LastNode = CurrentNode

print(lastDistance)