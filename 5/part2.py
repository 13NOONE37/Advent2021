import time
text = open('input.txt', 'r').readlines()

w, h = 10, 10
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
        Values.append([x1, y1, x2, y2])
        # ValuesDiagonals.append([x1, y1, x2, y2])
    elif (y1 == x2 and x1 == y2) or (x1 == y1 and x2 == y2):
        ValuesDiagonals.append([x1, y1, x2, y2])

Matrix = [[0 for x in range(w)] for y in range(h)]

for i in Values:
    if i[0] == i[2]:
        range1, range2 = None, None
        if i[1] < i[3]:
            range1 = i[1]
            range2 = i[3]
        else:
            range1 = i[3]
            range2 = i[1]

        for j in range(range1, range2+1):
            Matrix[i[0]][j] += 1

    if i[1] == i[3]:
        range1, range2 = None, None
        if i[0] < i[2]:
            range1 = i[0]
            range2 = i[2]
        else:
            range1 = i[2]
            range2 = i[0]

        for j in range(range1, range2+1):
            Matrix[j][i[1]] += 1

for i in ValuesDiagonals:
    if i[0] == i[1] and i[2] == i[3]:
        range1, range2 = None, None
        if i[0] < i[2]:
            range1 = i[0]
            range2 = i[2]
        else:
            range1 = i[2]
            range2 = i[0]

        for j in range(range1, range2+1):
            Matrix[j][j] += 1

    if i[0] == i[3] and i[1] == i[2]:
        range1, range2, range3, range4 = None, None, None, None
        if i[0] < i[1]:
            range1 = i[0]
            range2 = i[1]
            range3 = i[1]
            range4 = i[0]
        else:
            range1 = i[1]
            range2 = i[0]
            range3 = i[0]
            range4 = i[1]

        for j in range(range1, range2+1):
            print(j, (range2+range1)-j)
            Matrix[j][(range2+range1)-j] += 1
        print('\n')

result = 0
for i in range(0, w):
    for j in range(0, h):
        if Matrix[i][j] >= 2:
            result += 1
print('Result: ', result)
print('\n\n', Matrix)
