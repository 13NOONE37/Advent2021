import time
text = open('input.txt', 'r').readlines()

w, h = 0, 0
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
        if x1 > w:
            w = x1
        if y1 > h:
            h = y1


Matrix = [[0 for x in range(w)] for y in range(h)]

for i in Values:
    print(i)
    if i[0] == i[2]:
        range1 = i[1] if i[1] < i[3] else i[3]
        range2 = i[3] if i[3] > i[1] else i[1]

        for j in range(range1, range2+1):
            print(j)
            Matrix[i[0]][j] += 1
    if i[1] == i[3]:
        range1 = i[1] if i[1] < i[3] else i[3]
        range2 = i[3] if i[3] > i[1] else i[1]

        for j in range(range1, range2+1):
            print(j)
            Matrix[j][i[0]] += 1

    time.sleep(10)

print(Values)
# Matrix[0][0] = 1

# print(Matrix[0][0])  # prints 1
