# -----------------------
#   Advent of Code 2021
#   Day 8 Part 2
#   Author: James Hess
# -----------------------

# Parse puzzle input file and store necessary data in list
entryList = []
with open("Day8Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        lineList = []
        for io in line.split(" | "):
            itemList = []
            for item in io.split():
                sortedItem = "".join(sorted(item))
                itemList.append(sortedItem)
            lineList.append(itemList)
        entryList.append(lineList)

digitalOutput = []
for entry in entryList:
    key = [0,0,0,0,0,0,0,0,0,0]
    # Identify 1s, 7s, 4s, 8s
    for input in entry[0]:
        inputLen = len(input)
        if inputLen == 2:
            key[1] = input
        elif inputLen == 3:
            key[7] =  input
        elif inputLen == 4:
            key[4] = input
        elif inputLen == 7:
            key[8] = input

    # Identify L segments
    lSegments = key[4]
    for char in key[1]:
        lSegments = lSegments.replace(char,"")

    # Identify 2s, 3s, 5s
    for input in entry[0]:
        if len(input) == 5:
            isThree = True
            isFive = True
            for segment in key[1]:
                if segment not in input:
                    isThree = False
            for segment in lSegments:
                if segment not in input:
                    isFive = False
            if isThree:
                key[3] = input
            elif isFive:
                key[5] = input
            else:
                key[2] = input

    # Identify 0s, 6s, 9s
        if len(input) == 6:
            isNine = True
            isSix = True
            for segment in key[4]:
                if segment not in input:
                    isNine = False
            for segment in lSegments:
                if segment not in input:
                    isSix = False
            if isNine:
                key[9] = input
            elif isSix:
                key[6] = input
            else:
                key[0] = input

    outputDigits = []
    for output in entry[1]:
        digit = key.index(output)
        outputDigits.append(str(key.index(output)))
    digitalOutput.append(int("".join(outputDigits)))

print(sum(digitalOutput))


