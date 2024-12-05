from typing import Tuple

def find_sequence(sequence: list, matrix: list[list[str]], position: Tuple, direction: Tuple) -> bool:
    x, y = position
    dx, dy = direction
    for char in sequence:
        if not (0 <= x < len(matrix[0]) and 0 <= y < len(matrix)):
            return False
        if matrix[y][x] != char:
            return False
        x += dx
        y += dy
    return True

with open('input.txt') as input_file:
    lines = input_file.read().splitlines()
    matrix = [list(row) for row in lines]

sequence = ["X", "M", "A", "S"]
directions = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
result = 0

for y, row in enumerate(matrix):
    for x, col in enumerate(row):
        if col == "X":
            for direction in directions:
                if find_sequence(sequence, matrix, (x, y), direction):
                    result += 1
print(result)
