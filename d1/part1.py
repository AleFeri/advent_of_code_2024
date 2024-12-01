list1 = []
list2 = []

with open('input.txt') as input_file:
    for line in input_file.readlines():
        cols = line.split('   ')
        list1.append(int(cols[0]))
        list2.append(int(cols[1]))

list1.sort()
list2.sort()

result = 0
for i, elem in enumerate(list1):
    result += abs(elem - list2[i])

print(result)
