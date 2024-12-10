import re
from typing import Tuple, Set

def find_antennas_positions(matrix: list[list[str]], antenna: str) -> Set[Tuple[int, int]]:
    positions = set()
    for y, row in enumerate(matrix):
        for x, col in enumerate(row):
            if antenna == col:
                positions.add((x, y))

    return positions

with open('input.txt') as input_file:
    file_text = input_file.read()
    lines = file_text.splitlines()
    antennas = set(re.findall(r"\d+|\w+", file_text))
    matrix = [list(row) for row in lines]

result = 0
antinodes = set()
for a in antennas:
    positions = find_antennas_positions(matrix, a)
    for current_a in positions:
        for other_a in positions:
            if current_a == other_a:
                continue
            x, y = current_a
            ox, oy = other_a
            dx, dy = x-ox, y-oy
            if (
                (0 <= x+dx < len(matrix[0]) and 0 <= y+dy < len(matrix)) and
                (not (x+dx, y+dy) in antinodes)
            ):
                result += 1
                antinodes.add((x+dx, y+dy))
print(result)
