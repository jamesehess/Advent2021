# -----------------------
#   Advent of Code 2021
#   Day 3 Part 2
#   Author: James Hess
# -----------------------

o2binarys = []
co2binarys = []

with open("Day3Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        o2binarys.append(line.strip())
        co2binarys.append(line.strip())

binaryLen = len(o2binarys[0])

for n in range(0, binaryLen):
    binarysLen = len(o2binarys)
    if binarysLen == 1:
        break
    digitTotal = 0
    for i in range(0,binarysLen):
        digitTotal += int(o2binarys[i][n])

    if digitTotal / binarysLen >= 0.5:
        mostCommon = 1
    else:
        mostCommon = 0

    for j in reversed(range(0, binarysLen)):
        if int(o2binarys[j][n]) != mostCommon:
            o2binarys.pop(j)

for n in range(0, binaryLen):
    binarysLen = len(co2binarys)
    if binarysLen == 1:
        break
    digitTotal = 0
    for i in range(0,binarysLen):
        digitTotal += int(co2binarys[i][n])

    if digitTotal / binarysLen >= 0.5:
        mostCommon = 1
    else:
        mostCommon = 0

    for j in reversed(range(0, binarysLen)):
        if int(co2binarys[j][n]) == mostCommon:
            co2binarys.pop(j)

print(int(o2binarys[0],2)*int(co2binarys[0],2))