print("Start")

f = open("day3.txt", "r")

backpackDt = f.read()

backpackDt = backpackDt.replace('\n', ',')
backpackDt = backpackDt.split(',')

letters = []

scroring = {chr(i+96): i for i in range(1, 27)}
scoring2 = {chr(i+64-26): i for i in range(27, 53)}

totalScoring = scroring
totalScoring.update(scoring2)

print(totalScoring)

for item in backpackDt:
    size = len(item)
    firstCompartment = item[0:int(size/2)]
    secondCompartmnet = item[int(size/2):size]

    for i in list(firstCompartment):
        for j in list(secondCompartmnet):
            if i == j:
                letters.append(i)
                break
        else:
            continue
        break


points = 0

for letter in letters:
    points = points + totalScoring[letter]

print(points)
# print(letters)
# print(backpackDt)
