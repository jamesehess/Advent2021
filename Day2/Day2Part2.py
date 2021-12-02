# -----------------------
#   Advent of Code 2021
#   Day 2 Part 1
#   Author: James Hess
# -----------------------

# forward, up, down
commands = []
horizPos = 0
depthPos = 0
aim = 0

with open("Day2Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        commands.append(line.strip())

for command in commands:
    splitCommand = command.split()

    match splitCommand[0]:
        case 'down':
            aim += int(splitCommand[1])
        case 'up':
            aim += -int(splitCommand[1])
        case 'forward':
            horizPos += int(splitCommand[1])
            depthPos += aim * int(splitCommand[1])

print(horizPos*depthPos)