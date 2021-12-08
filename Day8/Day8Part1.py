# -----------------------
#   Advent of Code 2021
#   Day 8 Part 1
#   Author: James Hess
# -----------------------

# Parse puzzle input file and store necessary data in list
outputList = []
with open("Day8Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip().split(" | ")
        for item in line[1].split():
            outputList.append(item)
print(outputList)

count = 0
for item in outputList:
    if len(item) in (2,3,4,7):
        count += 1
print(count)
