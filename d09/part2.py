def count_repetitions(string: list[str], start: int) -> int:
    counter = 0
    for c in string[start:]:
        if c != string[start]:
            break
        counter += 1
    return counter

with open('input.txt') as input_file:
    text = input_file.read().replace("\n", "")

fs_format: list[str] = []
for i, digit in enumerate(text):
    if i % 2 == 0:
        for x in range(0, int(digit)):
            fs_format.append(str(i//2))
    else:
        for x in range(0, int(digit)):
            fs_format.append(".")

fs_format_list = fs_format
#print(''.join(fs_format_list))

last_moved = None
reverse = fs_format_list[::-1]
y = 0
while y < len(reverse):
    if reverse[y] == '.' or (last_moved != None and int(last_moved) <= int(reverse[y])):
        y += 1
        continue
    y_rep = count_repetitions(reverse, y)

    i = 0
    while i < len(fs_format_list)-y:
        digit = fs_format_list[i]
        if digit != '.':
            i += 1
            continue

        dot_count = count_repetitions(fs_format_list, i)
        if dot_count >= y_rep:
            for z in range(0, y_rep):
                fs_format_list[i] = reverse[y+z]
                fs_format_list[-(y+z+1)] = '.'
                i += 1
            last_moved = int(reverse[y])
            reverse = fs_format_list[::-1]
            break
        i += dot_count
    y += y_rep
    #print(''.join(fs_format_list))

result = 0
#print(fs_format_list)
for i, digit in enumerate(fs_format_list):
    if digit == '.':
        continue
    digit = int(digit)
    result += digit*i

print(result)

exit()

i = 0
last_moved = None
while i < len(fs_format_list):
    digit = fs_format_list[i]
    if digit == '.':
        dot_count = count_repetitions(fs_format_list, i)
        print(f"{dot_count=}, {i=}")

        reverse = fs_format_list[::-1]
        print('r:'+''.join(reverse))
        y = 0
        while y < len(reverse):
            print(f"{y=}")
            print()
            if reverse[y] == '.' or (last_moved != None and int(last_moved) <= int(reverse[y])) or i >= len(fs_format_list)-y:
                y += 1
                continue
            print(f"{last_moved=}")
            y_rep = count_repetitions(reverse, y)
            print(f"{y_rep=}")
            if y_rep <= dot_count:
                print(f"file={reverse[y]}")
                for z in range(0, y_rep):
                    print(f"r_:{reverse[y+z]}, y-1:{-y-1}, f_:{fs_format_list[-(y+z+1)]}")
                    fs_format_list[i] = reverse[y+z]
                    fs_format_list[-(y+z+1)] = '.'
                    i += 1
                last_moved = int(reverse[y])
                break
            y += y_rep
        print('n:'+''.join(fs_format_list))
    i += 1

result = 0
print(fs_format_list)
for i, digit in enumerate(fs_format_list):
    if digit == '.':
        continue
    digit = int(digit)
    result += digit*i

print(result)
