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

fs_format_list = list(fs_format)
for i, digit in enumerate(fs_format_list):
    if digit == '.':
        fs_format_list[i] = [d for d in fs_format_list[::-1] if d != '.'][0]
        while '.' == fs_format_list[-1]:
            del fs_format_list[-1]
        del fs_format_list[-1]


result = 0
print(fs_format_list)
for i, digit in enumerate(fs_format_list):
    if digit == '.':
        continue
    digit = int(digit)
    result += digit*i

print(result)
