# -----------------------
#   Advent of Code 2021
#   Day 6 Part 2
#   Author: James Hess
# -----------------------

# Parse input file and store in list
fishList = []
with open("Day6Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip().split(",")
        for item in line:
            fishList.append(int(item))

# Print initial fish list state
fishStr = [str(item) for item in fishList]
print("Initial State: "+",".join(fishStr))

# Initialize fish lists
fishStateCounts = [0]
for state in range(0,8):
    fishStateCounts.append(0)
for fish in fishList:
    fishStateCounts[fish] += 1

fishStr = [str(item) for item in fishStateCounts]
print("Initial Fish State Counts: "+",".join(fishStr))

runDays = 256
for day in range(1,runDays+1):
    newStateCounts = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for state in range(0,9):
        if state == 0:
            newStateCounts[6] += fishStateCounts[0]
            newStateCounts[8] += fishStateCounts[0]
        else:
            newStateCounts[state-1] += fishStateCounts[state]
    fishStateCounts = newStateCounts

    #fishStr = [str(item) for item in fishStateCounts]
    #print("After " + str(day) + " days: " + ",".join(fishStr))

fishCount = sum(fishStateCounts)
print("Fish Count: "+str(fishCount))