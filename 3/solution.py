import time
text = open('input.txt', 'r').readlines()

# Part1
# calcsTable = {
#     '0': [0, 0],  # first index is about 0 secound about 1
#     '1': [0, 0],
#     '2': [0, 0],
#     '3': [0, 0],
#     '4': [0, 0],
#     '5': [0, 0],
#     '6': [0, 0],
#     '7': [0, 0],
#     '8': [0, 0],
#     '9': [0, 0],
#     '10': [0, 0],
#     '11': [0, 0],
# }

# for item in text:
#     for i in range(0, len(item)-1):
#         if int(item[i]) == 1:
#             calcsTable[str(i)][1] += 1
#         else:
#             calcsTable[str(i)][0] += 1


# gammaRate, epsilonRate = '', ''

# print('calcs table: ', calcsTable)
# for item in calcsTable:
#     print(calcsTable[item])
#     if calcsTable[item][0] > calcsTable[item][1]:
#         gammaRate += '0'
#     elif calcsTable[item][1] > calcsTable[item][0]:
#         gammaRate += '1'

#     if calcsTable[item][0] < calcsTable[item][1]:
#         epsilonRate += '0'
#     elif calcsTable[item][1] < calcsTable[item][0]:
#         epsilonRate += '1'


# print(int(gammaRate, 2)*int(epsilonRate, 2))

# Part 2
# calcsTable = {
#     '0': [0, 0],  # first index is about 0 secound about 1
#     '1': [0, 0],
#     '2': [0, 0],
#     '3': [0, 0],
#     '4': [0, 0],
#     '5': [0, 0],
#     '6': [0, 0],
#     '7': [0, 0],
#     '8': [0, 0],
#     '9': [0, 0],
#     '10': [0, 0],
#     '11': [0, 0],
# }
# oxygenRate, co2Rate = [], []

# # Count the 1 and 0
# for item in text:
#     for i in range(0, len(item)-1):
#         if int(item[i]) == 1:
#             calcsTable[str(i)][1] += 1
#         else:
#             calcsTable[str(i)][0] += 1


# for x in range(0, len(text[0])-1):
#     for item in calcsTable:
#         # oxygen
#         if calcsTable[item][0] > calcsTable[item][1]:
#             for i, item2 in enumerate(text):
#                 if item2[x] == '0':
#                     oxygenRate.append(i)
#         elif calcsTable[item][1] > calcsTable[item][0]:
#             for i, item2 in enumerate(text):
#                 if item2[x] == '1':
#                     oxygenRate.append(i)
#         # co2
#         # if calcsTable[item][0] < calcsTable[item][1]:
#         #     epsilonRate += '0'
#         # elif calcsTable[item][1] < calcsTable[item][0]:
#         #     epsilonRate += '1'


# print('Oxygen: ', oxygenRate, len(oxygenRate))

# print('Solution: ', int(oxygenRate[0], 2)*int(co2Rate[0], 2))
textCopy = text
oxygenRate, co2Rate, temp = [], [], []

# Oxygen
for x in range(0, len(textCopy[0])-1):
    num0, num1, delete = 0, 0, ''
    for item in textCopy:
        if item[x] == '0':
            num0 += 1
        else:
            num1 += 1
    if num1 >= num0:
        delete = '1'
    else:
        delete = '0'
    for item in textCopy:
        if item[x] == delete:
            temp.append(item)
    if len(temp) < 1:
        break
    textCopy = temp
    temp = []

print('oxygenRate: ', textCopy)
oxygenRate = int(textCopy[0], 2)
textCopy = text

# co2
for x in range(0, len(textCopy[0])-1):
    num0, num1, delete = 0, 0, ''
    for item in textCopy:
        if item[x] == '0':
            num0 += 1
        else:
            num1 += 1
    if num1 < num0:
        delete = '1'
    else:
        delete = '0'
    for item in textCopy:
        if item[x] == delete:
            temp.append(item)

    if len(temp) < 1:
        break
    textCopy = temp
    temp = []
print('Co2: ', textCopy)
co2Rate = int(textCopy[0], 2)
textCopy = text

print(oxygenRate, co2Rate, '\nResult:', oxygenRate*co2Rate)
