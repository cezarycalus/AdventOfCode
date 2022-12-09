from string import ascii_letters

with open("day3.txt") as f:
    backpack_items = f.read().splitlines()

scoring = {letter: i for i, letter in enumerate(ascii_letters, start=1)}

points: list[int] = []

print(scoring)

counter = 0
for i in backpack_items:
    if counter % 3 == 0:
        first_line = backpack_items[counter]
        second_line = backpack_items[counter+1]
        third_line = backpack_items[counter+2]

        for first in first_line:
            for second in second_line:
                for third in third_line:
                    if first == second:
                        if second == third:
                            points.append(scoring[third])
                            break
                else:
                    continue
                break
            else:
                continue
            break

        counter += 1
    else:
        counter += 1

# print(sum(points))