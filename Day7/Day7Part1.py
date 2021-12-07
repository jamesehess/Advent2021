# -----------------------
#   Advent of Code 2021
#   Day 7 Part 1
#   Author: James Hess
# -----------------------

# Parse input file and store in list
crabList = []
with open("Day7Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip().split(",")
        for item in line:
            crabList.append(int(item))

# Print initial fish list state
crabStr = [str(item) for item in crabList]
#print("Initial State: "+",".join(crabStr))

# Find minimum and maximum crab postion
minCrab = min(crabList)
maxCrab =  max(crabList)
#print("Min: "+str(minCrab)+", Max: "+str(maxCrab))

fuelCosts = []
for position in range(minCrab,maxCrab):
    tempCost = 0
    for crab in crabList:
        tempCost += abs(crab-position)
    fuelCosts.append(tempCost)

print("Minimum Fuel Costs: "+str(min(fuelCosts)))