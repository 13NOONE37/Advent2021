import time
import os
import copy


text = open('input.txt', 'r').readlines()


# Random numbers
numbers = text[0].replace('\n', '').split(',')
numbers = list(map(int, numbers))
# remove from text numbers
text.__delitem__(0)


# Part1
# cardsOriginal, preResult = {}, {}
# pushIndex = -1

# for item in text:
#     if len(item) < 5:  # when line is empty
#         pushIndex += 1
#         # print('New: ')
#     else:
#         current = item.replace('\n', '').split()
#         current = list(map(int, current))

#         if not pushIndex in cardsOriginal:
#             cardsOriginal[pushIndex] = current
#         else:
#             cardsOriginal[pushIndex] += current
#         # print(current)

#     # time.sleep(2)


# cards = copy.deepcopy(cardsOriginal)
# os.system('cls' if os.name == 'nt' else 'clear')


# def checkBingo(current, original, index, ii, lastAdded, stopExecuting):
#     isBingo = False
#     for i in range(0, 5):  # cols
#         if current[i] == 'filled' and current[i+5] == 'filled' and current[i+10] == 'filled' and current[i+15] == 'filled' and current[i+20] == 'filled':
#             isBingo = True
#     for i in range(0, 25, 5):  # rows
#         if current[i] == 'filled' and current[i+1] == 'filled' and current[i+2] == 'filled' and current[i+3] == 'filled' and current[i+4] == 'filled':
#             isBingo = True
#             stopExecuting = True

#     if isBingo:
#         # if not ii in preResult:
#         copiedLastAdded = copy.deepcopy(lastAdded)
#         if not stopExecuting:
#             preResult[ii] = [index, copiedLastAdded]


# for i, item in enumerate(cards):
#     stopExecuting = False
#     index = 0
#     for j in numbers:
#         for k in range(0, len(cards[i])):
#             if cards[i][k] == j:

#                 if not i in preResult:
#                     lastAdded = cards[i][k]
#                     cards[i][k] = 'filled'
#                     index += 1
#                     if not stopExecuting:
#                         checkBingo(cards[i], cardsOriginal[i],
#                                    index, i, lastAdded, stopExecuting)
# correctBingo = sorted(preResult.items(), key=lambda item: item[1])[0]

# correctBingoLastNumber = correctBingo[1][1]
# correctBingoIndex = correctBingo[0]
# correctBingoValues = cardsOriginal[correctBingoIndex]

# unMarked = 0

# for i in range(0, len(correctBingoValues)):
#     if cards[correctBingoIndex][i] == cardsOriginal[correctBingoIndex][i]:
#         unMarked += cards[correctBingoIndex][i]


# result = unMarked*correctBingoLastNumber
# print('Result: ', result)

# Part2
cardsOriginal, preResult = {}, {}
pushIndex = -1

for item in text:
    if len(item) < 5:  # when line is empty
        pushIndex += 1
        # print('New: ')
    else:
        current = item.replace('\n', '').split()
        current = list(map(int, current))

        if not pushIndex in cardsOriginal:
            cardsOriginal[pushIndex] = current
        else:
            cardsOriginal[pushIndex] += current
        # print(current)

    # time.sleep(2)


cards = copy.deepcopy(cardsOriginal)
os.system('cls' if os.name == 'nt' else 'clear')


def checkBingo(current, original, index, ii, lastAdded, stopExecuting):
    print(ii)
    isBingo = False
    for i in range(0, 5):  # cols
        if current[i] == 'filled' and current[i+5] == 'filled' and current[i+10] == 'filled' and current[i+15] == 'filled' and current[i+20] == 'filled':
            isBingo = True
    for i in range(0, 25, 5):  # rows
        if current[i] == 'filled' and current[i+1] == 'filled' and current[i+2] == 'filled' and current[i+3] == 'filled' and current[i+4] == 'filled':
            isBingo = True
            stopExecuting = True

    if isBingo:
        # if not ii in preResult:
        copiedLastAdded = copy.deepcopy(lastAdded)
        if stopExecuting == False:
            preResult[ii] = [index, copiedLastAdded]
            print(preResult, ii)
            time.sleep(10)


for i, item in enumerate(cards):
    stopExecuting = False
    index = 0
    for j in numbers:
        for k in range(0, len(cards[i])):
            if cards[i][k] == j:

                print('\n', len(preResult), 'i: ', i, '\n')
                if not i in preResult:
                    lastAdded = cards[i][k]
                    cards[i][k] = 'filled'
                    print('\n', 'i: ', i, '\n')
                    index += 1
                    if stopExecuting == False:
                        checkBingo(cards[i], cardsOriginal[i],
                                   index, i, lastAdded, stopExecuting)

print("Length of cards: ", len(cards),
      "\n Length of preResult: ", len(preResult))
correctBingo = sorted(preResult.items(), key=lambda item: item[1])[
    len(preResult)-1]

correctBingoLastNumber = correctBingo[1][1]
correctBingoIndex = correctBingo[0]
correctBingoValues = cardsOriginal[correctBingoIndex]

unMarked = 0

for i in range(0, len(correctBingoValues)):
    if cards[correctBingoIndex][i] == cardsOriginal[correctBingoIndex][i]:
        unMarked += cards[correctBingoIndex][i]


result = unMarked*correctBingoLastNumber
print('Result: ', result)
