# -----------------------
#   Advent of Code 2021
#   Day 10 Part 2
#   Author: James Hess
# -----------------------

import statistics

# Parse puzzle input file and store necessary data in list
inputList = []
with open("Day10Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        inputList.append(line.strip())

scores = []
scoreCharLists = []
for input in inputList:
    while True:
        oldInput = input
        input = input.replace('()','')
        input = input.replace('[]', '')
        input = input.replace('{}', '')
        input = input.replace('<>', '')
        if oldInput == input:
            break
    if input.find(')') == -1 and input.find(']') == -1 and input.find('}') == -1 and input.find('>') == -1:
        scoreCharLists.append(input)

for scoreChars in scoreCharLists:
    score = 0
    for char in reversed(scoreChars):
        score = score * 5
        if char == '(':
            score += 1
        elif char == '[':
            score += 2
        elif char == '{':
            score += 3
        elif char == '<':
            score += 4
    scores.append(score)
scores.sort()
print(statistics.median(scores))