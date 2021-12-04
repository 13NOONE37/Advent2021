text = open('input.txt', 'r').readlines()

# Part 1
# horizontal, depth = 0, 0

# for item in text:
#     a = item.split(' ')
#     direction, value = a[0], a[1]

#     if direction == 'forward':
#         horizontal += int(value)
#     elif direction == 'up':
#         depth -= int(value)
#     elif direction == 'down':
#         depth += int(value)


# print('Result: ', horizontal*depth)

# Part 2
horizontal, depth, aim = 0, 0, 0

for item in text:
    a = item.split(' ')
    direction, value = a[0], a[1]

    if direction == 'forward':
        horizontal += int(value)
        depth += aim*int(value)
    elif direction == 'up':
        aim -= int(value)
    elif direction == 'down':
        aim += int(value)


print('Result: ', horizontal*depth)
