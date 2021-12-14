# -----------------------
#   Advent of Code 2021
#   Day 14 Part 1
#   Author: James Hess
# -----------------------

template = ''
rulesList = []

# Parse puzzle input file and store necessary data in list
with open("Day14Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        if '->' in line:
            rulesList.append(line.strip().split(' -> '))
        elif line != '\n':
            template = line.strip()

# Find rule function
def match(segment):
    for rule in rulesList:
        if rule[0] == segment:
            return rule[1]

print("Template: " + template)

steps = 10
for i in range(steps):
    templateLen = len(template)
    newTemplate = ''
    for idx in range(0,templateLen-1):
        segment = template[idx:idx+2]
        insert = match(segment)
        newTemplate = newTemplate + segment[0] + insert
    newTemplate = newTemplate + template[-1]
    print("After step " + str(i+1) + " (Len: " + str(len(newTemplate)) + "): " + newTemplate)
    template = newTemplate

charFreq = {}
for char in template:
    if char in charFreq:
        charFreq[char] += 1
    else:
        charFreq[char] = 1
counts = charFreq.values()
print("Score: " + str(max(counts)-min(counts)))
