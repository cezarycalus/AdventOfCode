print("Start")
f = open("day2.txt", "r")

gameDt = f.read()
gameDt = gameDt.replace(' ', ',')
gameDt = gameDt.replace('\n', '-')
gameDt = gameDt.split('-')


elfOneScore = 0
elfTwoScore = 0


for game in gameDt:
    if game == "A,X":
        elfOneScore += 4
        elfTwoScore += 4
    elif game == "A,Y":
        elfOneScore += 1
        elfTwoScore += 8
    elif game == "A,Z":
        elfOneScore += 7
        elfTwoScore += 3
    elif game == "B,X":
        elfOneScore += 8
        elfTwoScore += 1
    elif game == "B,Y":
        elfOneScore += 5
        elfTwoScore += 5
    elif game == "B,Z":
        elfOneScore += 2
        elfTwoScore += 9
    elif game == "C,X":
        elfOneScore += 3
        elfTwoScore += 7
    elif game == "C,Y":
        elfOneScore += 9
        elfTwoScore += 2
    elif game == "C,Z":
        elfOneScore += 6
        elfTwoScore += 6


print("My win score:", elfTwoScore)
print("Elf win score:", elfOneScore)

print("End of part one...")

elfOneScore = 0
elfTwoScore = 0

for game in gameDt:
    if game == "A,X":
        elfOneScore += 7
        elfTwoScore += 3
    elif game == "A,Y":
        elfOneScore += 4
        elfTwoScore += 4
    elif game == "A,Z":
        elfOneScore += 1
        elfTwoScore += 8
    elif game == "B,X":
        elfOneScore += 8
        elfTwoScore += 1
    elif game == "B,Y":
        elfOneScore += 5
        elfTwoScore += 5
    elif game == "B,Z":
        elfOneScore += 2
        elfTwoScore += 9
    elif game == "C,X":
        elfOneScore += 9
        elfTwoScore += 2
    elif game == "C,Y":
        elfOneScore += 6
        elfTwoScore += 6
    elif game == "C,Z":
        elfOneScore += 3
        elfTwoScore += 7


print("My win score 2nd game:", elfTwoScore)
print("Elf win score 2nd game:", elfOneScore)

print("End of part two...")
print("End")
