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

sequence = ["M", "A", "S"]
directions = [(-1, 1), (1, 1), (-1, -1), (1, -1)]
result = 0

for y, row in enumerate(matrix):
    for x, col in enumerate(row):
        if col == "A":
            mas_counter = 0
            for direction in directions:
                dx, dy = direction
                if find_sequence(sequence, matrix, (x+dx, y+dy), (-dx, -dy)):
                    mas_counter += 1
            result += 1 if mas_counter >= 2 else 0
print(result)
