list = []
with open("numbers.txt", "r") as data:
    for t in data:
        A = t[0]
        B = int(t[1:])
        list.append((A,B))

index = 50
Part1Answer = 0
Part2Answer = 0
for direction, distance in list:
    Part2Answer += distance // 100
    distance %= 100
    if direction == "R":
        index += distance
    else:
        index -= distance
    if ((index <= 0 and distance > abs(index)) or index >= 100) and distance != 0:
        Part2Answer += 1
    index %= 100
    if index == 0:
        Part1Answer += 1
    print(direction, distance, index, Part2Answer)

print(f"{Part1Answer = }")
print(f"{Part2Answer = }")
