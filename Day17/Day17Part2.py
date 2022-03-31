# -----------------------
#   Advent of Code 2021
#   Day 17 Part 2
#   Author: James Hess
# -----------------------

target = ((209,238),(-86,-59))
#target = ((20,30),(-10,-5))

# Identify valid X velocities
xVelocities = []
for vel in range(1,target[0][1]+1):
    currVel = vel
    xRange = 0
    while currVel > 0:
        xRange += currVel
        currVel -= 1
        if target[0][0] <= xRange <= target[0][1] and vel not in xVelocities:
            xVelocities.append(vel)

# Identify valid Y velocities for valid X velocities
validVelocities = []
for xVel in xVelocities:
    for yVel in range(target[1][0],100):
        currVel = [xVel, yVel]
        position = [0, 0]
        while position[0] < target[0][1] and position[1] > target[1][0]:
            # Update position
            position = [position[0] + currVel[0], position[1] + currVel[1]]
            # log initial velocities if target hit
            if target[0][0] <= position[0] <= target[0][1] and target[1][0] <= position[1] <= target[1][1] and [xVel,yVel] not in validVelocities:
                validVelocities.append([xVel,yVel])
            # Update velocities
            if currVel[0] > 0:
                currVel[0] -= 1
            elif currVel[0] < 0:
                currVel[0] += 1
            currVel[1] -= 1

print(len(validVelocities))