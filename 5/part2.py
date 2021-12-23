import time
text = open('input.txt', 'r').readlines()

w = 1000
Values = []
ValuesDiagonals = []

for i in text:
    i.replace('\n', '')
    temp = i.split(' -> ')
    x1 = int(temp[0].split(',')[0])
    y1 = int(temp[0].split(',')[1])
    x2 = int(temp[1].split(',')[0])
    y2 = int(temp[1].split(',')[1])
    if x1 == x2 or y1 == y2:
        Values.append([min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)])
    if abs(x2-x1) != 0 and abs(y2-y1) != 0:
        ValuesDiagonals.append([x1, y1, x2, y2])


Matrix = [[0 for x in range(w)] for y in range(w)]

for i in Values:
    if i[0] == i[2]:
        range1, range2 = i[1], i[3]
        for j in range(range1, range2+1):
            Matrix[i[0]][j] += 1
    if i[1] == i[3]:
        range1, range2 = i[0], i[2]
        for j in range(range1, range2+1):
            Matrix[j][i[1]] += 1
for i in ValuesDiagonals:
    print(i)
    range1, range2, range3, range4 = i[0], i[1], i[2], i[3]
    iterator1, iterator2 = 1 if range1 <= range3 else -1, 1 if range2 <= range4 else -1
    range3 += iterator1
    range4 += iterator2
    for x, y in zip(range(range1, range3, iterator1), range(range2, range4, iterator2)):
        # print(x, y)
        Matrix[x][y] += 1


# for y in range(0, w):
    # temp = ''
    # for x in range(0, w):
    #     temp += str((Matrix[x][y]))
    # print(temp)
    # temp = ''

result = 0
for i in range(0, w):
    for j in range(0, w):
        if Matrix[i][j] >= 2:
            result += 1
print('Result: ', result)
