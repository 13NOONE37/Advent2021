text = open('input.txt', 'r').readlines()

previous = None
count = 0

# Part1
# for i in text:
#     if previous != None:
#         if int(i) > previous:
#             count += 1

#     previous = int(i)

# Part2
for i, item in enumerate(text):
    if i <= len(text)-3:
        if previous != None:
            if int(text[i])+int(text[i+1])+int(text[i+2]) > previous:
                count += 1
        previous = int(text[i])+int(text[i+1])+int(text[i+2])

print(count)
