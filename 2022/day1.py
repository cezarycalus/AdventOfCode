print("Start")
f = open("day1.txt", "r")

elfsDt = f.read()
elfsDt = elfsDt.replace('\n', ',')
elfsDt = elfsDt.replace(',,', ',0,')
elfsDt = elfsDt.split(',')

elfsDt = [int(i) for i in elfsDt]

print(elfsDt)

temp = 0
caloriesArr = []

for item in elfsDt:
    if item == 0:
        caloriesArr.append(int(temp))
        temp = 0
        continue
    temp += item


print("Best calories:", max(caloriesArr))

topElfs = []

for i in range(0, 3):
    max = 0

    for j in range(len(caloriesArr)):
        if caloriesArr[j] > max:
            max = caloriesArr[j]

    caloriesArr.remove(max)
    topElfs.append(max)

print(topElfs)
print(sum(topElfs))

print("End")
