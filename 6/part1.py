import time
text = open('input.txt', 'r').readlines()[0].split(',')

values = []
for i in text:
    values.append(int(i))

for i in range(0, 80):  # day loop
    for j in range(0, len(values)):
        if values[j] == 0:
            values.append(8)
            values[j] = 7
        values[j] -= 1

print(len(values))
