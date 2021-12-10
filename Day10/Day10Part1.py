# -----------------------
#   Advent of Code 2021
#   Day 10 Part 1
#   Author: James Hess
# -----------------------

# Parse puzzle input file and store necessary data in list
inputList = []
with open("Day10Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        inputList.append(line.strip())

score = 0
for input in inputList:
    while True:
        oldInput = input
        input = input.replace('()','')
        input = input.replace('[]', '')
        input = input.replace('{}', '')
        input = input.replace('<>', '')
        if oldInput == input:
            break
    input = input.replace('(', '')
    input = input.replace('[', '')
    input = input.replace('{', '')
    input = input.replace('<', '')
    if len(input) > 0:
        if input[0] == ')':
            score += 3
        elif input[0] == ']':
            score += 57
        elif input[0] == '}':
            score += 1197
        elif input[0] == '>':
            score += 25137
print(score)
