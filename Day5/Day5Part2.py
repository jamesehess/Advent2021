# -----------------------
#   Advent of Code 2021
#   Day 5 Part 2
#   Author: James Hess
# -----------------------

# Create list of lists(segments) of lists(points) from file
segments = []
with open("Day5Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip().split(" -> ")
        tempPoint = []
        for point in line:
            tempPoint.append([int(x) for x in point.split(",")])
        segments.append(tempPoint)

# Initialize diagram
diagram = []
for x in range(1000):
    innerList = []
    for y in range(1000):
        innerList.append(0)
    diagram.append(innerList)

# Add segments to the diagram
for segment in segments:
    # if X coordinate is the same, then it's a vertical segment.
    if segment[0][0] == segment[1][0]:
        xCoor = segment[0][0]
        if segment[0][1] > segment[1][1]:
            maxYCoor = segment[0][1]
            minYCoor = segment[1][1]
        else:
            maxYCoor = segment[1][1]
            minYCoor = segment[0][1]
        for yCoor in range(minYCoor,maxYCoor+1):
            diagram[yCoor][xCoor] +=1
    # if Y coordinate is the same, then it's a horizontal segment.
    elif segment[0][1] == segment[1][1]:
        yCoor = segment[0][1]
        if segment[0][0] > segment[1][0]:
            maxXCoor = segment[0][0]
            minXCoor = segment[1][0]
        else:
            maxXCoor = segment[1][0]
            minXCoor = segment[0][0]
        for xCoor in range(minXCoor,maxXCoor+1):
            diagram[yCoor][xCoor] +=1
    # if not horizontal or vertical, must be diagonal
    else:
        currentPoint = segment[0]
        #Ex: 1,1 -> 3,3
        if segment[0][0] < segment[1][0] and segment[0][1] < segment[1][1]:
            #slanted forward, down
            slant = [1,1]
        #Ex: 1,4 -> 3,1
        elif segment[0][0] < segment[1][0] and segment[0][1] > segment[1][1]:
            #slant forward, up
            slant = [1,-1]
        #Ex: 5,1 -> 2,3
        elif segment[0][0] > segment[1][0] and segment[0][1] < segment[1][1]:
            #slant back, down
            slant = [-1, 1]
        #Ex: 5,5 -> 2,2
        elif segment[0][0] > segment[1][0] and segment[0][1] > segment[1][1]:
            # slant back, up
            slant = [-1, -1]
        while True:
            diagram[currentPoint[1]][currentPoint[0]] += 1
            if currentPoint == segment[1]:
                break
            currentPoint[0] += slant[0]
            currentPoint[1] += slant[1]

# Print diagram
#for line in diagram:
#    for point in line:
#        print(str(point)+" ", end='')
#    print("")

score = 0
for line in diagram:
    for point in line:
        if point > 1:
            score += 1
print(score)