# -----------------------
#   Advent of Code 2021
#   Day 17 Part 1
#   Author: James Hess
# -----------------------

target = ((209,238),(-86,-59))
#target = ((20,30),(-10,-5))

# Identify valid X velocities
xVelocities = []
for vel in range(1,target[0][1]):
    initVel = vel
    xRange = 0
    while vel > 0:
        xRange += vel
        vel -= 1
    if target[0][0] <= xRange <= target[0][1]:
        xVelocities.append(initVel)

# Identify MAX height using valid X velocities
maxHeights = []
for xVel in xVelocities:
    for yVel in range(1,100):
        maxHeight = 0
        currVel = [xVel,yVel]
        position = [0,0]
        while position[0] < target[0][1] and position[1] > target[1][0]:
            # Update position
            position = [position[0]+currVel[0],position[1]+currVel[1]]
            # Record max height
            if position[1] > maxHeight:
                maxHeight = position[1]
            # log max height if target hit
            if target[0][0] <= position[0] <= target[0][1] and target[1][0] <= position[1] <= target[1][1]:
                maxHeights.append(maxHeight)
            # Update velocities
            if currVel[0] > 0:
                currVel[0] -= 1
            elif currVel[0] < 0:
                currVel[0] += 1
            currVel[1] -= 1

print(max(maxHeights))