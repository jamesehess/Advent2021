# -----------------------
#   Advent of Code 2021
#   Day 1 Part 1
#   Author: James Hess
# -----------------------

depths = []
prevDepth = 0
increaseCount = 0

with open("Day1Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        depths.append(int(line.strip()))

for depth in depths:
    if prevDepth != 0 and depth > prevDepth:
        increaseCount += 1
    prevDepth = depth

print(increaseCount)