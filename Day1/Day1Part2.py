# -----------------------
#   Advent of Code 2021
#   Day 1 Part 2
#   Author: James Hess
# -----------------------

depths = []
windows = []
prevWindow = 0
increaseCount = 0


with open("Day1Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        depths.append(int(line.strip()))

depthsCount = len(depths)

for n in range(0, depthsCount - 2):
    windows.append(depths[n]+depths[n+1]+depths[n+2])

for window in windows:
    if prevWindow != 0 and window > prevWindow:
        increaseCount += 1
    prevWindow = window

print(increaseCount)