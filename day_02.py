# Day 2
with open('day_02_input.txt') as file:
    lines = file.readlines()

horizontal = 0
depth = 0
count = 0
aim = 0

# Part 1
for line in lines:
    count += 1
    move = line.split()
    # print(f"line {count}: Move {move[0]} {move[1]} spaces ")
    if move[0] == 'down':
        depth += int(move[1])
    elif move[0] == 'up':
        depth -= int(move[1])
    elif move[0] == 'forward':
        horizontal += int(move[1])

horz_depth = horizontal * depth

# print(f"Horizontal: {horizontal}")
# print(f"Depth: {depth}")
print(f"Pt 1 Final Horizontal x Depth = {horz_depth}")


# Part 2
horizontal = 0
depth = 0
count = 0
aim = 0

for line in lines:
    count += 1
    move = line.split()
    # print(f"line {count}: Move {move[0]} {move[1]} spaces ")
    if move[0] == 'down':
        # depth += int(move[1])
        aim += int(move[1])
    elif move[0] == 'up':
        # depth -= int(move[1])
        aim -= int(move[1])
    elif move[0] == 'forward':
        horizontal += int(move[1])
        depth += (aim * int(move[1]))

horz_depth = horizontal * depth

# print(f"Horizontal: {horizontal}")
# print(f"Depth: {depth}")
print(f"Pt 2 Final Horizontal x Depth = {horz_depth}")


