# -----------------------
#   Advent of Code 2021
#   Day 6 Part 1
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

runDays = 80
for day in range(1,runDays+1):
    for idx, fish in enumerate(fishList):
        if fish == 0:
            fishList[idx] = 6
            fishList.append(9)
        else:
            fishList[idx] -= 1
    #fishStr = [str(item) for item in fishList]
    #print("After " + str(day) + " days: " + ",".join(fishStr))

fishCount = len(fishList)
print("Fish Count: "+str(fishCount))