# -----------------------
#   Advent of Code 2021
#   Day 3 Part 1
#   Author: James Hess
# -----------------------

binarys = []
gammaBinary = ""
epsilonBinary = ""

with open("Day3Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        binarys.append(line.strip())

binarysLen = len(binarys)
binaryLen = len(binarys[0])

for n in range(0,binaryLen):
    digitTotal = 0
    for i in range(0,binarysLen):
        digitTotal += int(binarys[i][n])
    if digitTotal/binarysLen > 0.5:
        gammaBinary = gammaBinary + "1"
        epsilonBinary = epsilonBinary + "0"
    else:
        gammaBinary = gammaBinary + "0"
        epsilonBinary = epsilonBinary + "1"

print(int(gammaBinary,2)*int(epsilonBinary,2))