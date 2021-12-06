import time
import os
text = open('input.txt', 'r').readlines()


# Random numbers
numbers = text[0].replace('\n', '').split(',')
numbers = list(map(int, numbers))
# remove from text numbers
text.__delitem__(0)


# Part1
def checkBingo(line, cardsDuplicate):
    state = False
    for i in range(0, 5):
        sum = 0
        for j in range(0, 5):
            print(j)
    return state


cards, cardsDuplicate = {}, {}
pushIndex = -1

for item in text:
    if len(item) < 5:  # when line is empty
        pushIndex += 1
        # print('New: ')
    else:
        current = item.replace('\n', '').split()
        current = list(map(int, current))

        if not pushIndex in cards:
            cards[pushIndex] = current
        else:
            cards[pushIndex] += current
        # print(current)

    # time.sleep(2)
# print(cards)
cardsDuplicate = cards

os.system('cls' if os.name == 'nt' else 'clear')
print('Numbers: ', numbers, '\n')
for i, item in enumerate(cards):
    print(cards[i])
    for j in cards[i]:
        if j in numbers:
            print(j, ' exist')
            print(cards.index(22))
            # checkBingo(cards[i], cardsDuplicate)
    # time.sleep(20)

# Part2
