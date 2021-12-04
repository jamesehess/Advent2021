# -----------------------
#   Advent of Code 2021
#   Day 4 Part 2
#   Author: James Hess
# -----------------------

bingoDraws = []
bingoBoards = []
tempBoard = []
winner = []
lastWinner = False
score = 0


with open("Day4Input.txt") as file:
    lines = file.readlines()
    bingoDraws = lines[0].split(",")
    lines.pop(0)
    lines.pop(0)

    for line in lines:
        if line.strip() != "":
            tempBoard.append(line.split())
        else:
            bingoBoards.append(tempBoard)
            tempBoard = []

boardCount = len(bingoBoards)

for draw in bingoDraws:
    print(draw)
    # Mark new draws
    b = 0
    for board in bingoBoards:
        l = 0
        for line in board:
            i = 0
            for item in line:
                if item == draw:
                    bingoBoards[b][l][i] = "_" + item
                i+=1
            l+=1
        b+=1

    # Test for winner
    for board in reversed(bingoBoards):
        winner = []
        # Check for horizontal winner
        for line in board:
            lineWinner = True
            for item in line:
                if item[0] != "_":
                    lineWinner = False
            if lineWinner == True:
                winner = board
        # Check for vertical winner
        for v in range(0,5):
            vertWinner = True
            for l in range(0,5):
                if board[l][v][0] != "_":
                    vertWinner = False
            if vertWinner == True:
                winner = board
        if winner != [] and len(bingoBoards) == 1:
            lastWinner = True
            break

        if winner != []:
            bingoBoards.remove(board)

    if lastWinner == True:
        lastDraw = draw
        break

print("Last Winner!")
print(winner)

# Score
for line in winner:
    for item in line:
        if item[0] != "_":
            score += int(item)
print("Score: " + str(int(score) * int(lastDraw)))


