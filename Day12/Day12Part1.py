# -----------------------
#   Advent of Code 2021
#   Day 12 Part 1
#   Author: James Hess
# -----------------------

# Parse puzzle input file and store necessary data in list
pathSegmentList = []
with open("Day12Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        pathSegmentList.append(line.strip().split('-'))

pathList = []
START = 'start'
END = 'end'

def pathing(first,path):
    for segment in pathSegmentList:
        if segment[0] == first and (segment[1] not in path or segment[1][0].isupper()):
            newPath = path + [segment[1]]
            if segment[1] != END:
                pathing(segment[1],newPath)
            else:
                pathList.append(newPath)
        elif segment[1] == first and (segment[0] not in path or segment[0][0].isupper()):
            newPath = path +[segment[0]]
            if segment[0] != END:
                pathing(segment[0],newPath)
            else:
                pathList.append(newPath)

path = [START]
pathing(START,path)

for path in pathList:
    print(path)
print("Path Count: "+str(len(pathList)))
