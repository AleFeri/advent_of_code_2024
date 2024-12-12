with open('input.txt') as input_file:
    stones = input_file.readline().strip().split(" ")

for _ in range(25):
    new_stones = []
    for stone in stones:
        stone_num = int(stone)

        if stone_num == 0:
            new_stones.append(1)
        elif len(str(stone_num)) % 2 == 0:
            mid = len(str(stone_num)) // 2
            left = int(str(stone_num)[:mid])
            right = int(str(stone_num)[mid:])
            new_stones.extend([left, right])
        else:
            new_stones.append(stone_num * 2024)
    stones = list(map(str, new_stones))

print(len(stones))
