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
cardsOriginal, preResult = {}, {}


def checkBingo(current, original, index, ii, lastAdded):
    isBingo = False
    for i in range(0, 5):  # cols
        if current[i] == 'filled' and current[i+5] == 'filled' and current[i+10] == 'filled' and current[i+15] == 'filled' and current[i+20] == 'filled':
            isBingo = True
    for i in range(0, 25, 5):  # rows
        if current[i] == 'filled' and current[i+1] == 'filled' and current[i+2] == 'filled' and current[i+3] == 'filled' and current[i+4] == 'filled':
            isBingo = True

    if isBingo:
        # if not ii in preResult:
        preResult[ii] = [index, lastAdded]


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

for i, item in enumerate(cards):
    index = 0
    for j in numbers:
        for k in range(0, len(cards[i])):
            if cards[i][k] == j:

                if not i in preResult:
                    lastAdded = cards[i][k]
                    cards[i][k] = 'filled'
                    index += 1
                    checkBingo(cards[i], cardsOriginal[i], index, i, lastAdded)

correctBingo = sorted(preResult.items(), key=lambda item: item[1])[0]
correctBingoLastNumber = correctBingo[1][1]
correctBingoIndex = correctBingo[0]
correctBingoValues = cardsOriginal[correctBingoIndex]

unMarked = 0

for i in range(0, len(correctBingoValues)):
    # print(cards[correctBingoIndex][i], cardsOriginal[correctBingoIndex][i])
    # time.sleep(1)
    if cards[correctBingoIndex][i] == cardsOriginal[correctBingoIndex][i]:
        unMarked += cards[correctBingoIndex][i]


print(unMarked, correctBingoLastNumber)
result = unMarked*correctBingoLastNumber
print('Result: ', result)

# for item in preResult:
#     print(preResult[item])
# print('\n Result: \n', cards, '\n', cardsOriginal)
# Part2
