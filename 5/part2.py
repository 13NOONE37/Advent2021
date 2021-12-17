import time
text = open('input.txt', 'r').readlines()

w, h = 1000, 1000
Values = []

for i in text:
    i.replace('\n', '')
    temp = i.split(' -> ')
    x1 = int(temp[0].split(',')[0])
    y1 = int(temp[0].split(',')[1])
    x2 = int(temp[1].split(',')[0])
    y2 = int(temp[1].split(',')[1])
    # print(temp, x1, y1, x2, y2)
    if x1 == x2 or y1 == y2:
        Values.append([x1, y1, x2, y2])
        # print(temp, x1, y1, x2, y2)
        # if x1 > w:
        #     w = x1+1
        # if y1 > h:
        #     h = y1+1


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
        print('Range when x1==x2: ', range1, range2)

        for j in range(range1, range2+1):
            print(i, j, i[0])
            # time.sleep(2)
            Matrix[i[0]][j] += 1

    if i[1] == i[3]:
        range1, range2 = None, None
        if i[0] < i[2]:
            range1 = i[0]
            range2 = i[2]
        else:
            range1 = i[2]
            range2 = i[0]
        print('Range when y1==y2: ', range1, range2)

        for j in range(range1, range2+1):
            print(i, j, i[1])
            Matrix[j][i[1]] += 1

    if i[0] == i[1] and i[2] == i[3]:
        print('b')
        time.sleep(10)
    if i[0] == i[3] and i[1] == i[2]:
        print('a')

result = 0
for i in range(0, w):
    for j in range(0, h):
        if Matrix[i][j] >= 2:
            result += 1
print('Result: ', result)
