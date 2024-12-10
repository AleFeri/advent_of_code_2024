from collections import Counter

list1 = []
list2 = []

with open('input.txt') as input_file:
    for line in input_file.readlines():
        cols = line.split('   ')
        list1.append(int(cols[0]))
        list2.append(int(cols[1]))

counter_list2 = Counter(list2)

score = 0
for elem in list1:
    if elem in counter_list2:
        score += elem * counter_list2[elem]

print(score)