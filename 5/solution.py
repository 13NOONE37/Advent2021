import time
text = open('input.txt', 'r').readlines()

w, h = 1000, 1000
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


Matrix = [[0 for x in range(w)] for y in range(h)]

for i in Values:
    if i[0] == i[2]:
        range1, range2 = i[1], i[3]
        for j in range(range1, range2+1):
            Matrix[i[0]][j] += 1

    if i[1] == i[3]:
        range1, range2 = i[0], i[2]
        for j in range(range1, range2+1):
            Matrix[j][i[1]] += 1


result = 0
for i in range(0, w):
    for j in range(0, h):
        if Matrix[i][j] >= 2:
            result += 1
print('Result: ', result)
