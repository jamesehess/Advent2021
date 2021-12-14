# -----------------------
#   Advent of Code 2021
#   Day 14 Part 2
#   Author: James Hess
# -----------------------

template = ''
countRules = []
pairRules = []

# Parse puzzle input file and store necessary data in list
with open("Day14Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        if '->' in line:
            countRule = line.strip().split(' -> ')
            countRules.append(countRule)
            firstRule = [countRule[0],countRule[0][0]+countRule[1]]
            secondRule = [countRule[0],countRule[1]+countRule[0][1]]
            pairRules.append(firstRule)
            pairRules.append(secondRule)
        elif line != '\n':
            template = line.strip()
print("Count Rules List: ",end='')
print(countRules)
print("Pair Rules List: ",end='')
print(pairRules)

print('')

pairsDic = {}
for rule in countRules:
    pairsDic[rule[0]] = 0
for idx in range(0,len(template)-1):
    segment = template[idx:idx+2]
    pairsDic[segment] +=1
print("Initial Pairs Dic: ",end='')
print(pairsDic)

countsDic = {}
for rule in countRules:
    for char in rule[0]:
        countsDic[char] = 0
for char in template:
    countsDic[char] += 1
print("Initial Counts Dic: ",end='')
print(countsDic)

steps = 40
for i in range(steps):
    newPairsDic = {}
    print("Step " + str(i+1))
    # Update pairsDic
    for pair, value in pairsDic.items():
        # Update counts
        for rule in countRules:
            if rule[0] == pair:
                countsDic[rule[1]] += value
    for pair, value in pairsDic.items():
        # Update pairs
            for rule in pairRules:
                if rule[0] == pair:
                    if rule[1] in newPairsDic:
                        newPairsDic[rule[1]] += value
                    else:
                        newPairsDic[rule[1]] = value
    pairsDic = newPairsDic
    print(pairsDic)
    print(countsDic)

counts = countsDic.values()
print("Score: " + str(max(counts)-min(counts)))